"""A uniform result type for checks that produce errors and warnings."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Finding:
    level: str  # "error" | "warning"
    where: str
    message: str

    def __str__(self) -> str:
        return f"{self.level.upper():7} {self.where}: {self.message}"


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)

    def error(self, where: str, message: str) -> None:
        self.findings.append(Finding("error", where, message))

    def warn(self, where: str, message: str) -> None:
        self.findings.append(Finding("warning", where, message))

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def render(self) -> str:
        lines = [str(f) for f in self.errors + self.warnings]
        lines.append(f"{len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return "\n".join(lines)
