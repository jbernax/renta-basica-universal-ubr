"""Spanish Labor Market Institutions: SMI Cost Floor, Collective Bargaining, and Duality."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class SpanishLaborInstitutions:
    """Models Spanish labor market institutional parameters and adjustment margins."""

    # Statutory SMI parameters (Real Decreto 145/2024)
    smi_monthly_14_payments: float = 1_134.0
    employer_ss_rate: float = 0.315  # Average employer Social Security wedge (contingencias comunes, desempleo, FOGASA, FP, MEI)
    
    # RDL 32/2021 labor reform: fixed-discontinuous inactivity parameter
    fijos_discontinuos_elasticity: float = 0.40

    def gross_smi_monthly_wage(self) -> float:
        """Monthly gross wage for full-time SMI worker normalized to 12 monthly payments."""
        return (self.smi_monthly_14_payments * 14.0) / 12.0

    def gross_smi_cost_floor(self) -> float:
        """Total gross employer labor cost floor per month (W_floor per RD 145/2024)."""
        # W_floor = SMI_12 * (1 + tau_SS_emp)
        return round(self.gross_smi_monthly_wage() * (1.0 + self.employer_ss_rate), 2)

    def evaluate_adjustment(
        self,
        wage_level: float,
        productivity_drop: float,
        allows_opt_out: bool = False,
    ) -> Tuple[bool, float, bool]:
        """Evaluates whether an institutional shock results in extensive displacement, wage cuts, or inactivity.
        
        Returns:
            (displaced: bool, wage_adjustment_rate: float, inactivity_spell: bool)
        """
        smi_gross = self.gross_smi_monthly_wage()
        
        # Binding minimum wage cliff: if current wage is near SMI (within 10%), wage cuts are legally impossible
        if wage_level <= smi_gross * 1.10:
            if productivity_drop > 0.05:
                # Extensive-margin displacement cliff
                return (True, 0.0, False)
            return (False, 0.0, False)
        
        # For wages above SMI:
        if allows_opt_out:
            # Art. 82.3 Estatuto de los Trabajadores: descuelgue salarial allows negotiated wage cuts
            # up to 60% of the productivity shock, bounded by the SMI floor
            max_allowed_cut = min(productivity_drop * 0.60, (wage_level - smi_gross) / wage_level)
            return (False, -max_allowed_cut, False)
        else:
            # Sectoral collective agreement is rigid: adjust via contract inactivity (fijos discontinuos)
            if productivity_drop > 0.15:
                # Transition to partial inactivity or redundancy
                return (False, 0.0, True)
            return (False, 0.0, False)
