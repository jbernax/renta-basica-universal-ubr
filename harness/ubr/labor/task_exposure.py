"""Task Exposure Calibration: Mapping CNO-11 Occupations to AI Exposure Scores."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List
from ubr.labor.cno_taxonomy import CNOTaxonomy, CNOGroup


@dataclass(frozen=True)
class ExposureScore:
    """Calculated AI exposure metrics for a specific CNO occupation."""
    cno_code: str
    alpha_direct: float
    beta_augmented: float
    cognitive_share: float
    eticce_adoption_rate: float
    net_exposure: float


class TaskExposureEngine:
    """Engine mapping O*NET / Eloundou et al. (2024) / Felten et al. (2021) task metrics to CNO-11."""

    # Baseline task parameters by 2-digit CNO code
    # (alpha_direct, beta_augmented, cognitive_share, eticce_adoption_rate)
    _CALIBRATED_PARAMS: Dict[str, tuple[float, float, float, float]] = {
        # Managers: moderate direct, high augmented, high cognitive, high firm adoption
        "11": (0.32, 0.65, 0.88, 0.42),
        "12": (0.28, 0.58, 0.82, 0.38),
        # Professionals: high direct, very high augmented, pure cognitive
        "21": (0.48, 0.85, 0.94, 0.52),  # Tech / engineering
        "22": (0.22, 0.45, 0.75, 0.30),  # Health professionals
        "23": (0.35, 0.62, 0.85, 0.35),  # Teaching
        "24": (0.52, 0.88, 0.92, 0.48),  # Business / admin specialists
        # Technicians: moderate-to-high
        "31": (0.30, 0.60, 0.72, 0.36),
        "33": (0.45, 0.78, 0.85, 0.40),
        # Clerical: the highest direct displacement hazard in Europe
        "41": (0.68, 0.92, 0.90, 0.45),  # Back-office / finance / archive
        "43": (0.55, 0.82, 0.80, 0.38),  # Receptionists / travel / phone
        # Services & sales: physical / interpersonal buffer
        "51": (0.12, 0.28, 0.35, 0.22),  # Hospitality / retail
        "56": (0.10, 0.22, 0.40, 0.25),  # Security
        "57": (0.05, 0.15, 0.30, 0.18),  # Personal care / nursing aides
        # Agriculture: physical constraint
        "61": (0.04, 0.12, 0.15, 0.12),
        # Craft & trades: manual manipulation
        "71": (0.03, 0.10, 0.18, 0.15),  # Construction
        "75": (0.08, 0.22, 0.30, 0.20),  # Mechanics / electricians
        # Operators: robotics / computer vision
        "81": (0.15, 0.38, 0.35, 0.28),  # Factory operators
        "84": (0.18, 0.45, 0.32, 0.25),  # Drivers
        # Elementary: purely physical / manual
        "91": (0.02, 0.08, 0.10, 0.12),  # Cleaners
        "94": (0.06, 0.18, 0.20, 0.18),  # Food prep / warehouse helpers
        # Military
        "01": (0.15, 0.35, 0.45, 0.25),
    }

    def compute_exposure(self, taxonomy: CNOTaxonomy) -> List[ExposureScore]:
        """Calculates exposure scores for all occupations in the taxonomy."""
        scores: List[ExposureScore] = []
        for group in taxonomy.all_groups():
            params = self._CALIBRATED_PARAMS.get(group.cno_code, (0.20, 0.40, 0.50, 0.25))
            alpha, beta, cog, adopt = params
            
            # Net exposure accounts for augmented tooling, cognitive intensity, and firm adoption
            # net_exposure = beta * cog * (0.6 + 0.4 * adopt / 0.5)
            adoption_scale = (adopt / 0.30) ** 0.5
            net = min(0.95, beta * (0.4 + 0.6 * cog) * (0.7 + 0.3 * adoption_scale))
            
            scores.append(
                ExposureScore(
                    cno_code=group.cno_code,
                    alpha_direct=alpha,
                    beta_augmented=beta,
                    cognitive_share=cog,
                    eticce_adoption_rate=adopt,
                    net_exposure=round(net, 4),
                )
            )
        return scores
