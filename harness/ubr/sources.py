"""Machine verification of the source registry: does each cited locator actually resolve?"""
from __future__ import annotations

from datetime import datetime, timezone

import requests

from ubr.project import Project, dump_yaml, load_yaml

DOI_HANDLE_API = "https://doi.org/api/handles/{doi}"
SOURCES_HEADER = (
    "Source registry. Every [@id] citation in plan/**/*.md must resolve to an entry here.\n"
    "verified / verified_by / check_status / checked_at are maintained by `python -m ubr sources verify`.\n"
    "Set `verified: true` + `verified_by: human` to vouch for a source that blocks automated checks."
)


def locator_url(source: dict) -> str | None:
    """DOIs are checked against the DOI registry (publishers often block bots); otherwise the URL itself."""
    if source.get("doi"):
        return DOI_HANDLE_API.format(doi=source["doi"])
    return source.get("url")


def probe(http, url: str, timeout: float, headers: dict) -> str:
    """Return the final HTTP status as a string, or 'error: <Type>' on network failure."""
    try:
        response = http.head(url, timeout=timeout, allow_redirects=True, headers=headers)
        status = response.status_code
        response.close()
        if status >= 400:
            response = http.get(url, timeout=timeout, allow_redirects=True, headers=headers, stream=True)
            status = response.status_code
            response.close()
        return str(status)
    except requests.RequestException as exc:
        return f"error: {type(exc).__name__}"


def _needs_check(source: dict, recheck: bool) -> bool:
    if source.get("verified") and source.get("verified_by") == "human":
        return False
    return recheck or not source.get("verified")


def verify_sources(project: Project, http=None, now: datetime | None = None,
                   offline: bool = False, recheck: bool = False) -> dict:
    cfg = project.config.get("sources", {})
    timeout = float(cfg.get("timeout_seconds", 15))
    headers = {"User-Agent": cfg.get("user_agent", "ubr-harness")}
    stamp = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    data = load_yaml(project.sources_path) or {"sources": []}
    summary = {"checked": 0, "verified": [], "failed": [], "no_locator": [], "skipped": 0}

    http = http or requests.Session()
    for source in data["sources"]:
        if offline or not _needs_check(source, recheck):
            summary["skipped"] += 1
            continue
        url = locator_url(source)
        if url is None:
            source.update(verified=False, check_status="no-locator", checked_at=stamp)
            source.pop("verified_by", None)
            summary["no_locator"].append(source["id"])
            continue
        status = probe(http, url, timeout, headers)
        ok = status.isdigit() and int(status) < 400
        source.update(verified=ok, check_status=status, checked_at=stamp)
        if ok:
            source["verified_by"] = "machine"
            summary["verified"].append(source["id"])
        else:
            source.pop("verified_by", None)
            summary["failed"].append(source["id"])
        summary["checked"] += 1

    if summary["checked"] or summary["no_locator"]:
        dump_yaml(project.sources_path, data, header=SOURCES_HEADER)
    return summary
