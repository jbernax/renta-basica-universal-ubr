"""Iteration lifecycle: numbering, plan snapshots, reviewer bundles, rotation and checkpoints."""
from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from ubr.plan_model import load_manifest, load_sources, module_files
from ubr.project import Project, dump_yaml, load_yaml

ITER_PREFIX = "iter-"
FRONT_MATTER_DOCS = ("00-scope.md", "decisions.md", "methods.md")
BACK_MATTER_DOCS = ("paper-outline.md", "open-questions.md")


class IterationError(Exception):
    pass


@dataclass(frozen=True)
class Iteration:
    number: int
    path: Path

    @property
    def id(self) -> str:
        return format_id(self.number)

    @property
    def manifest(self) -> dict:
        return load_yaml(self.path / "manifest.yaml") or {}

    @property
    def reviewers(self) -> list[str]:
        return list(self.manifest.get("reviewers", []))

    @property
    def is_open(self) -> bool:
        return not (self.path / "scores.json").exists()

    @property
    def snapshot_plan(self) -> Path:
        return self.path / "snapshot" / "plan"


def format_id(number: int) -> str:
    return f"{ITER_PREFIX}{number:04d}"


def list_iterations(project: Project) -> list[Iteration]:
    if not project.iterations_dir.is_dir():
        return []
    found = []
    for path in project.iterations_dir.glob(f"{ITER_PREFIX}[0-9][0-9][0-9][0-9]"):
        if path.is_dir():
            found.append(Iteration(int(path.name[len(ITER_PREFIX):]), path))
    return sorted(found, key=lambda it: it.number)


def open_iteration(project: Project) -> Iteration | None:
    iterations = list_iterations(project)
    return iterations[-1] if iterations and iterations[-1].is_open else None


def resolve_iteration(project: Project, ref: str | None) -> Iteration:
    iterations = list_iterations(project)
    if not iterations:
        raise IterationError("No iterations exist yet; run `ubr iteration start`.")
    if ref in (None, "", "latest"):
        return iterations[-1]
    raw = ref[len(ITER_PREFIX):] if ref.startswith(ITER_PREFIX) else ref
    try:
        number = int(raw)
    except ValueError as exc:
        raise IterationError(f"Not an iteration reference: {ref!r}") from exc
    for it in iterations:
        if it.number == number:
            return it
    raise IterationError(f"{format_id(number)} does not exist.")


def select_reviewers(reviewers_cfg: dict, number: int) -> list[str]:
    """Deterministic rotation: always-on reviewers plus a sliding window over the rest of the panel."""
    panel: list[str] = list(reviewers_cfg["panel"])
    always = set(reviewers_cfg.get("always_include", []))
    full_every = int(reviewers_cfg.get("full_panel_every") or 0)
    if (reviewers_cfg.get("first_iteration_full_panel") and number == 1) or (full_every and number % full_every == 0):
        return panel
    pool = [p for p in panel if p not in always]
    window = max(int(reviewers_cfg["rotation"]) - len(always), 0)
    window = min(window, len(pool))
    start = ((number - 1) * window) % len(pool) if pool else 0
    rotating = {pool[(start + i) % len(pool)] for i in range(window)}
    return [p for p in panel if p in always or p in rotating]


def build_bundle(project: Project, number: int) -> str:
    """Concatenate the whole plan into one reviewer-friendly document."""
    manifest = load_manifest(project)
    parts = [
        f"# Research plan bundle — {format_id(number)}\n",
        "Read-only snapshot for reviewers. File boundaries are marked with `<!-- FILE: path -->`.\n",
        _file_part(project, project.plan_dir / "plan.yaml", fenced="yaml"),
    ]
    included: set[Path] = {project.plan_dir / "plan.yaml"}
    for name in FRONT_MATTER_DOCS:
        parts.append(_file_part(project, project.plan_dir / name))
        included.add(project.plan_dir / name)
    for path in _modules_in_manifest_order(project, manifest):
        parts.append(_file_part(project, path))
        included.add(path)
    for name in BACK_MATTER_DOCS:
        parts.append(_file_part(project, project.plan_dir / name))
        included.add(project.plan_dir / name)
    for extra in sorted(project.plan_dir.rglob("*.md")):
        if extra not in included:
            parts.append(_file_part(project, extra))
    parts.append(_sources_table(project))
    return "\n".join(p for p in parts if p)


def _modules_in_manifest_order(project: Project, manifest: dict) -> list[Path]:
    files = module_files(project)
    order = {mid: i for i, mid in enumerate(manifest.get("modules", []))}
    return sorted(files, key=lambda p: (order.get(p.name[:3], len(order)), p.name))


def _file_part(project: Project, path: Path, fenced: str | None = None) -> str:
    if not path.is_file():
        return ""
    rel = path.relative_to(project.root).as_posix()
    text = path.read_text(encoding="utf-8").rstrip()
    if fenced:
        text = f"```{fenced}\n{text}\n```"
    return f"\n<!-- FILE: {rel} -->\n{text}\n"


def _sources_table(project: Project) -> str:
    rows = ["\n<!-- FILE: plan/sources.yaml (summary) -->", "## Source registry", "",
            "| id | authors | year | title | locator | verified |", "|---|---|---|---|---|---|"]
    for s in load_sources(project):
        authors = "; ".join(s.get("authors", [])[:3])
        locator = s.get("doi") and f"doi:{s['doi']}" or s.get("url") or s.get("isbn", "")
        rows.append(f"| {s['id']} | {authors} | {s.get('year', '')} | {s.get('title', '')} | {locator} | "
                    f"{'yes' if s.get('verified') else 'no'} |")
    return "\n".join(rows) + "\n"


def start_iteration(project: Project, now: datetime | None = None) -> Iteration:
    current = open_iteration(project)
    if current:
        raise IterationError(f"{current.id} is still open (no scores.json). Finish or score it first.")
    previous = list_iterations(project)
    number = previous[-1].number + 1 if previous else 1
    iteration = Iteration(number, project.iterations_dir / format_id(number))
    iteration.path.mkdir(parents=True)
    shutil.copytree(project.plan_dir, iteration.snapshot_plan)
    (iteration.path / "reviews").mkdir()
    (iteration.path / "bundle.md").write_text(build_bundle(project, number), encoding="utf-8")
    manifest = load_manifest(project)
    dump_yaml(iteration.path / "manifest.yaml", {
        "iteration": number,
        "id": iteration.id,
        "started_at": (now or datetime.now(timezone.utc)).isoformat(timespec="seconds"),
        "plan_version": str(manifest.get("version", "")),
        "reviewers": select_reviewers(project.config["reviewers"], number),
    })
    return iteration


def _checkpoints_path(project: Project) -> Path:
    return project.iterations_dir / "checkpoints.yaml"


def load_checkpoints(project: Project) -> list[dict]:
    path = _checkpoints_path(project)
    return (load_yaml(path) or {}).get("checkpoints", []) if path.is_file() else []


def last_checkpoint(project: Project) -> int:
    return max((int(c["iteration"]) for c in load_checkpoints(project)), default=0)


def record_checkpoint(project: Project, note: str = "", now: datetime | None = None) -> int:
    iterations = list_iterations(project)
    if not iterations:
        raise IterationError("Nothing to checkpoint: no iterations exist.")
    latest = iterations[-1]
    if latest.is_open:
        raise IterationError(f"{latest.id} is still open; score it before recording a checkpoint.")
    checkpoints = load_checkpoints(project)
    checkpoints.append({
        "iteration": latest.number,
        "at": (now or datetime.now(timezone.utc)).isoformat(timespec="seconds"),
        "note": note,
    })
    dump_yaml(_checkpoints_path(project), {"checkpoints": checkpoints})
    return latest.number
