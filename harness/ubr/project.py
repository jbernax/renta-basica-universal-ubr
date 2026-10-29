"""Locating the project on disk and loading its harness configuration."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

import yaml


class ProjectNotFound(Exception):
    pass


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def dump_yaml(path: Path, data, header: str | None = None) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    if header:
        text = "".join(f"# {line}\n" if line else "#\n" for line in header.splitlines()) + text
    path.write_text(text, encoding="utf-8")


@dataclass(frozen=True)
class Project:
    root: Path

    @property
    def plan_dir(self) -> Path:
        return self.root / "plan"

    @property
    def modules_dir(self) -> Path:
        return self.plan_dir / "modules"

    @property
    def harness_dir(self) -> Path:
        return self.root / "harness"

    @property
    def iterations_dir(self) -> Path:
        return self.root / "iterations"

    @property
    def sources_path(self) -> Path:
        return self.plan_dir / "sources.yaml"

    @cached_property
    def config(self) -> dict:
        return load_yaml(self.harness_dir / "config.yaml")

    @cached_property
    def rubric(self) -> list[dict]:
        return load_yaml(self.harness_dir / "rubric.yaml")["criteria"]

    @property
    def criterion_ids(self) -> list[str]:
        return [c["id"] for c in self.rubric]

    @cached_property
    def factors(self) -> list[dict]:
        return load_yaml(self.harness_dir / "reference-factors.yaml")["factors"]

    def schema(self, name: str) -> dict:
        return json.loads((self.harness_dir / "schemas" / f"{name}.schema.json").read_text(encoding="utf-8"))


def find_project(start: Path | None = None) -> Project:
    """Resolve the project root from $UBR_ROOT or by walking up to a dir containing harness/config.yaml."""
    env_root = os.environ.get("UBR_ROOT")
    if env_root:
        root = Path(env_root).resolve()
        if not (root / "harness" / "config.yaml").is_file():
            raise ProjectNotFound(f"UBR_ROOT={root} has no harness/config.yaml")
        return Project(root)
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "harness" / "config.yaml").is_file():
            return Project(candidate)
    raise ProjectNotFound(f"No harness/config.yaml found at or above {current}")
