import requests
import yaml
from conftest import FIXED_NOW

from ubr.sources import verify_sources


class FakeResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def close(self):
        pass


class FakeHttp:
    """Stands in for requests.Session at the network boundary."""

    def __init__(self, head=None, get=None, raises=None):
        self.head_status = head or {}
        self.get_status = get or {}
        self.raises = raises or {}
        self.calls = []

    def _respond(self, method, url, table):
        self.calls.append((method, url))
        if url in self.raises:
            raise self.raises[url]
        return FakeResponse(table.get(url, 404))

    def head(self, url, **kwargs):
        return self._respond("HEAD", url, self.head_status)

    def get(self, url, **kwargs):
        return self._respond("GET", url, self.get_status)


def load_sources(project):
    data = yaml.safe_load((project.plan_dir / "sources.yaml").read_text())
    return {s["id"]: s for s in data["sources"]}


def test_resolving_url_marks_source_verified(project):
    http = FakeHttp(head={"https://example.org/unused": 200, "https://doi.org/api/handles/10.1000/beta": 200})
    verify_sources(project, http=http, now=FIXED_NOW, recheck=True)
    sources = load_sources(project)
    assert sources["src-unused"]["verified"] is True
    assert sources["src-unused"]["verified_by"] == "machine"
    assert sources["src-unused"]["checked_at"].startswith("2026-10-29")


def test_doi_is_checked_through_doi_handle_api(project):
    http = FakeHttp(head={"https://doi.org/api/handles/10.1000/beta": 302})
    verify_sources(project, http=http, now=FIXED_NOW)
    assert ("HEAD", "https://doi.org/api/handles/10.1000/beta") in http.calls
    assert load_sources(project)["src-b"]["verified"] is True


def test_not_found_marks_source_unverified(project):
    http = FakeHttp(head={"https://doi.org/api/handles/10.1000/beta": 404}, get={"https://doi.org/api/handles/10.1000/beta": 404})
    summary = verify_sources(project, http=http, now=FIXED_NOW)
    assert load_sources(project)["src-b"]["verified"] is False
    assert load_sources(project)["src-b"]["check_status"] == "404"
    assert "src-b" in summary["failed"]


def test_head_rejection_falls_back_to_get(project):
    url = "https://doi.org/api/handles/10.1000/beta"
    http = FakeHttp(head={url: 405}, get={url: 200})
    verify_sources(project, http=http, now=FIXED_NOW)
    assert ("GET", url) in http.calls
    assert load_sources(project)["src-b"]["verified"] is True


def test_network_error_is_recorded_not_raised(project):
    url = "https://doi.org/api/handles/10.1000/beta"
    http = FakeHttp(raises={url: requests.Timeout("slow")})
    summary = verify_sources(project, http=http, now=FIXED_NOW)
    src = load_sources(project)["src-b"]
    assert src["verified"] is False
    assert src["check_status"].startswith("error")
    assert "src-b" in summary["failed"]


def test_human_verified_sources_are_never_overwritten(project):
    path = project.plan_dir / "sources.yaml"
    data = yaml.safe_load(path.read_text())
    data["sources"][1].update(verified=True, verified_by="human")
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    http = FakeHttp()
    verify_sources(project, http=http, now=FIXED_NOW, recheck=True)
    assert load_sources(project)["src-b"]["verified"] is True
    assert ("HEAD", "https://doi.org/api/handles/10.1000/beta") not in http.calls


def test_already_machine_verified_sources_skipped_unless_recheck(project):
    http = FakeHttp()
    verify_sources(project, http=http, now=FIXED_NOW)
    assert ("HEAD", "https://example.org/a") not in http.calls


def test_offline_mode_makes_no_requests(project):
    http = FakeHttp()
    summary = verify_sources(project, http=http, now=FIXED_NOW, offline=True)
    assert http.calls == []
    assert summary["checked"] == 0
