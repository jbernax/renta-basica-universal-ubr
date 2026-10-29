"""Parsing plan modules: frontmatter, sections, research questions and citations."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from ubr.project import Project, load_yaml

HEADING_RE = re.compile(r"^##\s+(?:\d+\.\s*)?(.+?)\s*$", re.MULTILINE)
RQ_RE = re.compile(r"\*\*(RQ-M\d{2}-\d{2})\*\*")
CITATION_BLOCK_RE = re.compile(r"\[(@[^\]]+)\]")
CITATION_KEY_RE = re.compile(r"@([A-Za-z0-9_][A-Za-z0-9_:.\-]*)")
HYPOTHESIS_RE = re.compile(r"hypothes[ie]s\s*[:*]", re.IGNORECASE)


class FrontmatterError(ValueError):
    pass


@dataclass
class ResearchQuestion:
    id: str
    text: str

    @property
    def has_hypothesis(self) -> bool:
        return bool(HYPOTHESIS_RE.search(self.text))


@dataclass
class Module:
    path: Path
    meta: dict
    body: str
    sections: dict[str, str] = field(default_factory=dict)

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))

    @property
    def locked(self) -> bool:
        return bool(self.meta.get("locked"))

    def section(self, title: str) -> str | None:
        wanted = title.casefold()
        for heading, text in self.sections.items():
            if heading.casefold().startswith(wanted):
                return text
        return None

    @property
    def research_questions(self) -> list[ResearchQuestion]:
        text = self.section("Research questions") or ""
        matches = list(RQ_RE.finditer(text))
        return [
            ResearchQuestion(m.group(1), text[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)
        ]


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise FrontmatterError("missing YAML frontmatter block")
    end = text.find("\n---", 4)
    if end == -1:
        raise FrontmatterError("unterminated YAML frontmatter block")
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        raise FrontmatterError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(meta, dict):
        raise FrontmatterError("frontmatter must be a mapping")
    return meta, text[end + 4:].lstrip("\n")


def split_sections(body: str) -> dict[str, str]:
    matches = list(HEADING_RE.finditer(body))
    return {
        m.group(1): body[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(body)]
        for i, m in enumerate(matches)
    }


def section_order(body: str) -> list[str]:
    return [m.group(1) for m in HEADING_RE.finditer(body)]


def parse_module(path: Path) -> Module:
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return Module(path=path, meta=meta, body=body, sections=split_sections(body))


def module_files(project: Project) -> list[Path]:
    return sorted(project.modules_dir.glob("M[0-9][0-9]-*.md"))


def load_modules(project: Project) -> list[Module]:
    """Parse every module file; raises FrontmatterError on the first unparseable file."""
    return [parse_module(p) for p in module_files(project)]


def extract_citations(text: str) -> list[str]:
    keys: list[str] = []
    for block in CITATION_BLOCK_RE.findall(text):
        keys.extend(k.rstrip(".") for k in CITATION_KEY_RE.findall(block))
    return keys


def load_manifest(project: Project) -> dict:
    return load_yaml(project.plan_dir / "plan.yaml") or {}


def load_sources(project: Project) -> list[dict]:
    data = load_yaml(project.sources_path) or {}
    return data.get("sources") or []


def citable_documents(project: Project) -> list[Path]:
    """Every markdown file in the plan whose citations must resolve."""
    return sorted(p for p in project.plan_dir.rglob("*.md"))


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", text))
