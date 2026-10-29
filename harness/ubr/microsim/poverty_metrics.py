"""Foster-Greer-Thorbecke Poverty Indices, Dual BHC/AHC Thresholds, and Inequality Metrics (Track 2).

Implements M09 (Distributional, Poverty, and Inequality Microsimulation) and M02.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence


@dataclass
class FGTResult:
    p0_headcount_ratio: float  # Fraction below threshold
    p1_poverty_gap: float      # Depth of poverty
    p2_poverty_severity: float # Severity / inequality among poor


@dataclass
class DistributionalSummary:
    # Median equivalized incomes
    median_equivalized_income_bhc: float
    median_equivalized_income_ahc: float
    poverty_threshold_60_bhc: float
    poverty_threshold_40_bhc: float
    poverty_threshold_60_ahc: float
    poverty_threshold_40_ahc: float

    # BHC Poverty metrics
    bhc_floating_60: FGTResult
    bhc_anchored_60: FGTResult
    bhc_severe_40: FGTResult
    bhc_child_poverty_rate: float

    # AHC Poverty metrics
    ahc_floating_60: FGTResult
    ahc_anchored_60: FGTResult
    ahc_severe_40: FGTResult
    ahc_child_poverty_rate: float

    # Inequality metrics
    gini_coefficient: float
    s80_s20_ratio: float
    theil_index: float
    atkinson_index_e1: float

    # Individualized & Disability Impairment metrics
    individualized_poverty_rate: float
    impairment_adjusted_poverty_rate: float


def compute_weighted_median(values: Sequence[float], weights: Sequence[float]) -> float:
    """Compute the weighted median of a series."""
    if not values or len(values) != len(weights):
        return 0.0
    pairs = sorted(zip(values, weights), key=lambda x: x[0])
    total_w = sum(weights)
    half_w = total_w / 2.0
    cum_w = 0.0
    for val, w in pairs:
        cum_w += w
        if cum_w >= half_w:
            return float(val)
    return float(pairs[-1][0])


def compute_fgt(
    values: Sequence[float],
    weights: Sequence[float],
    threshold: float,
) -> FGTResult:
    """Compute Foster-Greer-Thorbecke (P0, P1, P2) poverty indices."""
    total_w = sum(weights)
    if total_w <= 0.0 or threshold <= 0.0:
        return FGTResult(0.0, 0.0, 0.0)

    p0_sum = 0.0
    p1_sum = 0.0
    p2_sum = 0.0

    for val, w in zip(values, weights):
        if val < threshold:
            p0_sum += w
            gap = (threshold - val) / threshold
            p1_sum += w * gap
            p2_sum += w * (gap ** 2)

    return FGTResult(
        p0_headcount_ratio=p0_sum / total_w,
        p1_poverty_gap=p1_sum / total_w,
        p2_poverty_severity=p2_sum / total_w,
    )


def compute_gini(values: Sequence[float], weights: Sequence[float]) -> float:
    """Compute weighted Gini coefficient."""
    total_w = sum(weights)
    if total_w <= 0.0 or len(values) == 0:
        return 0.0

    pairs = sorted(zip(values, weights), key=lambda x: x[0])
    # Fast O(N log N) weighted Gini formula
    total_income = sum(val * w for val, w in pairs)
    if total_income <= 0.0:
        return 0.0

    cum_w = 0.0
    cum_inc = 0.0
    lorentz_sum = 0.0

    for val, w in pairs:
        inc = val * w
        # Area of trapezoid in Lorenz curve
        lorentz_sum += (2.0 * cum_inc + inc) * w
        cum_inc += inc
        cum_w += w

    gini = 1.0 - (lorentz_sum / (total_income * total_w))
    return max(0.0, min(1.0, float(gini)))


def compute_s80_s20(values: Sequence[float], weights: Sequence[float]) -> float:
    """Compute S80/S20 quintile income share ratio."""
    total_w = sum(weights)
    if total_w <= 0.0:
        return 1.0

    pairs = sorted(zip(values, weights), key=lambda x: x[0])
    q20_target = total_w * 0.20
    q80_target = total_w * 0.80

    cum_w = 0.0
    bottom_20_inc = 0.0
    top_20_inc = 0.0
    total_inc = sum(v * w for v, w in pairs)

    for val, w in pairs:
        cum_w_prev = cum_w
        cum_w += w
        if cum_w <= q20_target:
            bottom_20_inc += val * w
        elif cum_w_prev < q20_target:
            # Overlap into bottom 20%
            frac = (q20_target - cum_w_prev) / w
            bottom_20_inc += val * w * frac

        if cum_w > q80_target:
            if cum_w_prev >= q80_target:
                top_20_inc += val * w
            else:
                frac = (cum_w - q80_target) / w
                top_20_inc += val * w * frac

    if bottom_20_inc <= 0.0:
        return float("inf")
    return float(top_20_inc / bottom_20_inc)


def compute_theil(values: Sequence[float], weights: Sequence[float]) -> float:
    """Compute Theil entropy index of inequality."""
    total_w = sum(weights)
    if total_w <= 0.0:
        return 0.0
    mean_inc = sum(v * w for v, w in zip(values, weights)) / total_w
    if mean_inc <= 0.0:
        return 0.0

    theil_sum = 0.0
    for v, w in zip(values, weights):
        if v > 0.0:
            ratio = v / mean_inc
            theil_sum += w * ratio * math.log(ratio)

    return max(0.0, float(theil_sum / total_w))


def compute_atkinson(values: Sequence[float], weights: Sequence[float], epsilon: float = 1.0) -> float:
    """Compute Atkinson index for inequality aversion epsilon."""
    total_w = sum(weights)
    if total_w <= 0.0:
        return 0.0
    mean_inc = sum(v * w for v, w in zip(values, weights)) / total_w
    if mean_inc <= 0.0:
        return 0.0

    if abs(epsilon - 1.0) < 1e-4:
        # Limit as epsilon -> 1: geometric mean / arithmetic mean
        log_sum = sum(w * math.log(max(1.0, v)) for v, w in zip(values, weights))
        geom_mean = math.exp(log_sum / total_w)
        return max(0.0, 1.0 - (geom_mean / mean_inc))
    else:
        power_sum = sum(w * (max(0.0, v) ** (1.0 - epsilon)) for v, w in zip(values, weights))
        ede = (power_sum / total_w) ** (1.0 / (1.0 - epsilon))
        return max(0.0, 1.0 - (ede / mean_inc))
