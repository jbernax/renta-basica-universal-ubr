"""Stopping rules: decide whether the loop continues, pauses for a human, or proposes SOTA."""
from __future__ import annotations

from dataclasses import dataclass, field

CONTINUE = "continue"
CHECKPOINT = "checkpoint"
REGRESSION = "regression"
PLATEAU = "plateau"
SOTA_CANDIDATE = "sota-candidate"
STOPPING_OUTCOMES = {CHECKPOINT, REGRESSION, PLATEAU, SOTA_CANDIDATE}


@dataclass
class Decision:
    outcome: str
    reasons: list[str] = field(default_factory=list)

    @property
    def stops_loop(self) -> bool:
        return self.outcome in STOPPING_OUTCOMES


def decide(history: list[dict], config: dict, last_checkpoint: int = 0) -> Decision:
    """Precedence: regression > sota-candidate > plateau > checkpoint > continue."""
    if not history:
        return Decision(CONTINUE, ["no scored iterations yet"])
    rules = config["stopping"]
    latest = history[-1]

    if latest.get("delta") is not None and latest["delta"] <= rules["regression_alert"]:
        return Decision(REGRESSION, [f"weighted score changed by {latest['delta']:+.2f} "
                                     f"(alert at {rules['regression_alert']:+.2f}); inspect the last changelog"])

    plateaued, plateau_reason = _plateau(history, rules)
    gaps = _sota_gaps(latest, rules)
    if plateaued and not gaps:
        return Decision(SOTA_CANDIDATE, ["all SOTA gates pass", plateau_reason,
                                         "human sign-off required before declaring SOTA"])
    if plateaued:
        return Decision(PLATEAU, [plateau_reason, *gaps, "loop is not converging on its own; human steering needed"])

    since = latest["iteration"] - last_checkpoint
    per_checkpoint = int(config["cycle"]["iterations_per_checkpoint"])
    if since >= per_checkpoint:
        return Decision(CHECKPOINT, [f"{since} iteration(s) since last checkpoint (limit {per_checkpoint})", *gaps])
    return Decision(CONTINUE, [f"{since}/{per_checkpoint} iterations in this cycle", *gaps])


def _plateau(history: list[dict], rules: dict) -> tuple[bool, str]:
    window = int(rules["plateau_window"])
    deltas = [h.get("delta") for h in history[-window:]]
    if len(history) < window + 1 or any(d is None for d in deltas):
        return False, ""
    if all(abs(d) < rules["plateau_delta"] for d in deltas):
        return True, f"plateau: last {window} deltas {[round(d, 3) for d in deltas]} all < {rules['plateau_delta']}"
    return False, ""


def _sota_gaps(latest: dict, rules: dict) -> list[str]:
    gaps = []
    metrics = latest.get("metrics", {})
    if latest["weighted"] < rules["sota_weighted_min"]:
        gaps.append(f"weighted {latest['weighted']:.2f} < {rules['sota_weighted_min']}")
    if latest["min_criterion"] < rules["sota_criterion_min"]:
        gaps.append(f"weakest criterion {latest['min_criterion']:.2f} < {rules['sota_criterion_min']}")
    if latest.get("open_critical", 0) > 0:
        gaps.append(f"{latest['open_critical']} open critical issue(s)")
    if metrics.get("coverage", 0.0) < rules["min_coverage"]:
        gaps.append(f"coverage {metrics.get('coverage', 0.0):.0%} < {rules['min_coverage']:.0%}")
    if metrics.get("verified_ratio", 0.0) < rules["min_verified_sources_ratio"]:
        gaps.append(f"verified sources {metrics.get('verified_ratio', 0.0):.0%} "
                    f"< {rules['min_verified_sources_ratio']:.0%}")
    return gaps
