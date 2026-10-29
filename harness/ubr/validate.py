"""Structural lint for the research plan, including locked-file enforcement during open iterations."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import jsonschema

from ubr.findings import Report
from ubr.iterations import open_iteration
from ubr.plan_model import (
    FrontmatterError,
    Module,
    citable_documents,
    extract_citations,
    load_manifest,
    load_sources,
    module_files,
    parse_module,
    section_order,
    split_frontmatter,
)
from ubr.project import Project, load_yaml


def validate_plan(project: Project) -> Report:
    report = Report()
    modules = _parse_modules(project, report)
    _check_manifest(project, modules, report)
    for module in modules:
        _check_module(project, module, report)
    _check_cross_module(project, modules, report)
    _check_sources_and_citations(project, report)
    _check_locks(project, report)
    return report


def _rel(project: Project, path: Path) -> str:
    return path.relative_to(project.root).as_posix()


def _parse_modules(project: Project, report: Report) -> list[Module]:
    schema = project.schema("module")
    modules = []
    for path in module_files(project):
        try:
            module = parse_module(path)
        except FrontmatterError as exc:
            report.error(_rel(project, path), f"frontmatter: {exc}")
            continue
        for err in jsonschema.Draft202012Validator(schema).iter_errors(module.meta):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            report.error(_rel(project, path), f"frontmatter {loc}: {err.message}")
        if module.id and not path.name.startswith(f"{module.id}-"):
            report.error(_rel(project, path), f"frontmatter id {module.id} does not match filename")
        modules.append(module)
    return modules


def _check_manifest(project: Project, modules: list[Module], report: Report) -> None:
    manifest_path = project.plan_dir / "plan.yaml"
    if not manifest_path.is_file():
        report.error("plan/plan.yaml", "manifest missing")
        return
    listed = list(load_manifest(project).get("modules") or [])
    for mid, count in Counter(listed).items():
        if count > 1:
            report.error("plan/plan.yaml", f"module {mid} listed {count} times in manifest")
    present = {m.id for m in modules}
    for mid in listed:
        if mid not in present:
            report.error("plan/plan.yaml", f"manifest lists {mid} but no module file exists")
    for mid in sorted(present - set(listed)):
        report.error("plan/plan.yaml", f"module {mid} exists but is not listed in the manifest")


def _check_module(project: Project, module: Module, report: Report) -> None:
    where = _rel(project, module.path)
    plan_cfg = project.config["plan"]
    headings = [h.casefold() for h in section_order(module.body)]
    positions = []
    for required in plan_cfg["required_sections"]:
        idx = next((i for i, h in enumerate(headings) if h.startswith(required.casefold())), None)
        if idx is None:
            report.error(where, f"missing required section '{required}'")
        else:
            positions.append(idx)
    if positions != sorted(positions):
        report.error(where, "required sections are out of order")

    rqs = module.research_questions
    minimum = int(plan_cfg.get("min_research_questions", 1))
    if len(rqs) < minimum:
        report.error(where, f"has {len(rqs)} research question(s); at least {minimum} required")
    for rq in rqs:
        if not rq.id.startswith(f"RQ-{module.id}-"):
            report.error(where, f"{rq.id} does not carry the module prefix RQ-{module.id}-")
        if not rq.has_hypothesis:
            report.error(where, f"{rq.id} has no 'Hypothesis:' line")


def _check_cross_module(project: Project, modules: list[Module], report: Report) -> None:
    ids = {m.id for m in modules}
    factor_ids = {f["id"] for f in project.factors}
    rq_counts = Counter(rq.id for m in modules for rq in m.research_questions)
    for rq_id, count in rq_counts.items():
        if count > 1:
            report.error("plan/modules", f"duplicate research question id {rq_id} ({count} occurrences)")
    for m in modules:
        where = _rel(project, m.path)
        for dep in m.meta.get("depends_on") or []:
            if dep == m.id:
                report.error(where, "module depends on itself")
            elif dep not in ids:
                report.error(where, f"depends_on references unknown module {dep}")
        for factor in m.meta.get("covers") or []:
            if factor not in factor_ids:
                report.error(where, f"covers unknown reference factor {factor}")


def _check_sources_and_citations(project: Project, report: Report) -> None:
    if not project.sources_path.is_file():
        report.error("plan/sources.yaml", "source registry missing")
        return
    raw = load_yaml(project.sources_path) or {}
    for err in jsonschema.Draft202012Validator(project.schema("sources")).iter_errors(raw):
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        report.error("plan/sources.yaml", f"{loc}: {err.message}")
    sources = load_sources(project)
    id_counts = Counter(s.get("id") for s in sources)
    for sid, count in id_counts.items():
        if count > 1:
            report.error("plan/sources.yaml", f"duplicate source id {sid}")
    known = set(id_counts)
    cited: set[str] = set()
    for doc in citable_documents(project):
        keys = extract_citations(doc.read_text(encoding="utf-8"))
        cited.update(keys)
        for key in sorted(set(keys) - known):
            report.error(_rel(project, doc), f"citation [@{key}] not found in sources.yaml")
    for sid in sorted(known - cited):
        report.warn("plan/sources.yaml", f"source {sid} is never cited")


def _is_locked_file(path: Path) -> bool:
    try:
        meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    except FrontmatterError:
        return False
    return bool(meta.get("locked"))


def _check_locks(project: Project, report: Report) -> None:
    """While an iteration is open, files locked in its snapshot must be byte-identical in the live plan."""
    iteration = open_iteration(project)
    if iteration is None or not iteration.snapshot_plan.is_dir():
        return
    snapshot = iteration.snapshot_plan
    always_locked = set(project.config["plan"].get("always_locked", []))
    for snap_file in sorted(snapshot.rglob("*.md")):
        rel = snap_file.relative_to(snapshot)
        if rel.as_posix() not in always_locked and not _is_locked_file(snap_file):
            continue
        live = project.plan_dir / rel
        label = f"plan/{rel.as_posix()}"
        if not live.is_file():
            report.error(label, f"locked file {label} was deleted during {iteration.id}")
        elif live.read_bytes() != snap_file.read_bytes():
            report.error(label, f"locked file {label} was modified during {iteration.id}; file a proposal instead")
