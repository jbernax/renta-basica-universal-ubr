"""CNO-11 (Clasificación Nacional de Ocupaciones 2011) Taxonomy and Spanish EPA Calibration."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CNOGroup:
    """Represents an occupation group in the Spanish CNO-11 taxonomy."""
    cno_code: str
    title: str
    major_group: int
    fte_employment: float
    avg_monthly_gross_wage: float
    wage_deciles: List[float] = field(default_factory=list)
    female_share: float = 0.50
    fixed_discontinuous_share: float = 0.05
    sector: str = "Services"

    @property
    def annual_wage_bill(self) -> float:
        """Annual gross wage bill for this occupation (in EUR)."""
        return self.fte_employment * self.avg_monthly_gross_wage * 12.0


class CNOTaxonomy:
    """Registry of calibrated Spanish CNO-11 occupational groups."""

    def __init__(self, groups: List[CNOGroup]):
        self._groups = {g.cno_code: g for g in groups}

    def all_groups(self) -> List[CNOGroup]:
        return list(self._groups.values())

    def get_group(self, code: str) -> Optional[CNOGroup]:
        return self._groups.get(code)

    def total_employment_fte(self) -> float:
        return sum(g.fte_employment for g in self._groups.values())

    def total_aggregate_wage_bill(self) -> float:
        return sum(g.annual_wage_bill for g in self._groups.values())

    @classmethod
    def load_default(cls) -> CNOTaxonomy:
        """Loads default Spanish EPA-calibrated CNO-11 occupational groups (21.5M FTEs)."""
        groups = [
            # Group 1: Directors and managers
            CNOGroup(
                cno_code="11",
                title="Directores de departamentos administrativos y comerciales",
                major_group=1,
                fte_employment=420_000,
                avg_monthly_gross_wage=3_950.0,
                wage_deciles=[2_200, 2_600, 3_000, 3_400, 3_800, 4_100, 4_500, 5_100, 6_000, 7_800],
                female_share=0.38,
                fixed_discontinuous_share=0.01,
                sector="Services",
            ),
            CNOGroup(
                cno_code="12",
                title="Directores de producción y operaciones",
                major_group=1,
                fte_employment=430_000,
                avg_monthly_gross_wage=3_750.0,
                wage_deciles=[2_100, 2_500, 2_850, 3_250, 3_600, 3_950, 4_350, 4_900, 5_600, 7_200],
                female_share=0.32,
                fixed_discontinuous_share=0.01,
                sector="Industry",
            ),
            # Group 2: Scientific and intellectual professionals
            CNOGroup(
                cno_code="21",
                title="Profesionales en ciencias físicas, químicas, matemáticas y de la ingeniería",
                major_group=2,
                fte_employment=950_000,
                avg_monthly_gross_wage=3_200.0,
                wage_deciles=[1_850, 2_150, 2_450, 2_750, 3_050, 3_350, 3_700, 4_200, 4_900, 6_200],
                female_share=0.29,
                fixed_discontinuous_share=0.02,
                sector="Technology",
            ),
            CNOGroup(
                cno_code="22",
                title="Profesionales de la salud",
                major_group=2,
                fte_employment=750_000,
                avg_monthly_gross_wage=3_350.0,
                wage_deciles=[1_950, 2_250, 2_550, 2_900, 3_200, 3_550, 3_900, 4_400, 5_100, 6_500],
                female_share=0.72,
                fixed_discontinuous_share=0.03,
                sector="Health",
            ),
            CNOGroup(
                cno_code="23",
                title="Profesionales de la enseñanza",
                major_group=2,
                fte_employment=980_000,
                avg_monthly_gross_wage=2_650.0,
                wage_deciles=[1_700, 1_950, 2_150, 2_350, 2_550, 2_750, 2_950, 3_200, 3_600, 4_300],
                female_share=0.68,
                fixed_discontinuous_share=0.06,
                sector="Education",
            ),
            CNOGroup(
                cno_code="24",
                title="Especialistas en organización de la administración pública y de empresas, y comercialización",
                major_group=2,
                fte_employment=1_420_000,
                avg_monthly_gross_wage=2_850.0,
                wage_deciles=[1_750, 2_000, 2_250, 2_500, 2_750, 3_000, 3_350, 3_800, 4_400, 5_500],
                female_share=0.54,
                fixed_discontinuous_share=0.02,
                sector="Services",
            ),
            # Group 3: Technicians and support professionals
            CNOGroup(
                cno_code="31",
                title="Técnicos de las ciencias y de las ingenierías",
                major_group=3,
                fte_employment=1_150_000,
                avg_monthly_gross_wage=2_350.0,
                wage_deciles=[1_550, 1_750, 1_950, 2_150, 2_350, 2_550, 2_800, 3_100, 3_550, 4_300],
                female_share=0.26,
                fixed_discontinuous_share=0.03,
                sector="Industry",
            ),
            CNOGroup(
                cno_code="33",
                title="Técnicos y profesionales de apoyo de gestión administrativa",
                major_group=3,
                fte_employment=1_350_000,
                avg_monthly_gross_wage=2_180.0,
                wage_deciles=[1_450, 1_650, 1_820, 2_000, 2_180, 2_360, 2_580, 2_850, 3_250, 3_900],
                female_share=0.59,
                fixed_discontinuous_share=0.04,
                sector="Services",
            ),
            # Group 4: Clerical support workers
            CNOGroup(
                cno_code="41",
                title="Empleados de oficina que no atienden al público (contabilidad, finanzas, archivo)",
                major_group=4,
                fte_employment=1_200_000,
                avg_monthly_gross_wage=1_850.0,
                wage_deciles=[1_350, 1_450, 1_580, 1_700, 1_820, 1_960, 2_120, 2_320, 2_600, 3_100],
                female_share=0.66,
                fixed_discontinuous_share=0.03,
                sector="Services",
            ),
            CNOGroup(
                cno_code="43",
                title="Empleados de agencias de viajes, recepcionistas y telefonistas",
                major_group=4,
                fte_employment=1_050_000,
                avg_monthly_gross_wage=1_650.0,
                wage_deciles=[1_250, 1_350, 1_450, 1_550, 1_650, 1_750, 1_880, 2_050, 2_300, 2_700],
                female_share=0.71,
                fixed_discontinuous_share=0.08,
                sector="Services",
            ),
            # Group 5: Service and sales workers
            CNOGroup(
                cno_code="51",
                title="Trabajadores de los servicios de restauración y comercio",
                major_group=5,
                fte_employment=2_900_000,
                avg_monthly_gross_wage=1_420.0,
                wage_deciles=[1_150, 1_220, 1_290, 1_360, 1_420, 1_490, 1_580, 1_700, 1_880, 2_250],
                female_share=0.58,
                fixed_discontinuous_share=0.18,
                sector="Services",
            ),
            CNOGroup(
                cno_code="56",
                title="Trabajadores de los servicios de protección y seguridad",
                major_group=5,
                fte_employment=450_000,
                avg_monthly_gross_wage=1_950.0,
                wage_deciles=[1_400, 1_520, 1_640, 1_760, 1_880, 2_000, 2_150, 2_350, 2_650, 3_150],
                female_share=0.18,
                fixed_discontinuous_share=0.02,
                sector="Public",
            ),
            CNOGroup(
                cno_code="57",
                title="Trabajadores de los cuidados a las personas en servicios de salud y afines",
                major_group=5,
                fte_employment=1_450_000,
                avg_monthly_gross_wage=1_480.0,
                wage_deciles=[1_180, 1_250, 1_320, 1_400, 1_480, 1_560, 1_660, 1_780, 1_980, 2_350],
                female_share=0.84,
                fixed_discontinuous_share=0.09,
                sector="Health",
            ),
            # Group 6: Skilled agricultural, forestry, and fishery
            CNOGroup(
                cno_code="61",
                title="Trabajadores cualificados en actividades agrícolas y ganaderas",
                major_group=6,
                fte_employment=450_000,
                avg_monthly_gross_wage=1_280.0,
                wage_deciles=[1_050, 1_120, 1_180, 1_240, 1_290, 1_350, 1_420, 1_520, 1_680, 2_050],
                female_share=0.22,
                fixed_discontinuous_share=0.28,
                sector="Agriculture",
            ),
            # Group 7: Craft and related trades
            CNOGroup(
                cno_code="71",
                title="Trabajadores en obras estructurales de construcción y afines",
                major_group=7,
                fte_employment=1_150_000,
                avg_monthly_gross_wage=1_780.0,
                wage_deciles=[1_320, 1_420, 1_520, 1_630, 1_740, 1_860, 2_000, 2_180, 2_450, 2_950],
                female_share=0.04,
                fixed_discontinuous_share=0.06,
                sector="Construction",
            ),
            CNOGroup(
                cno_code="75",
                title="Mecánicos y ajustadores de maquinaria, electricistas y afines",
                major_group=7,
                fte_employment=1_250_000,
                avg_monthly_gross_wage=1_880.0,
                wage_deciles=[1_380, 1_490, 1_600, 1_720, 1_840, 1_980, 2_140, 2_340, 2_650, 3_200],
                female_share=0.06,
                fixed_discontinuous_share=0.03,
                sector="Industry",
            ),
            # Group 8: Plant and machine operators
            CNOGroup(
                cno_code="81",
                title="Operadores de instalaciones fijas y maquinaria industrial",
                major_group=8,
                fte_employment=650_000,
                avg_monthly_gross_wage=1_750.0,
                wage_deciles=[1_300, 1_400, 1_500, 1_610, 1_720, 1_840, 1_980, 2_150, 2_420, 2_900],
                female_share=0.18,
                fixed_discontinuous_share=0.04,
                sector="Industry",
            ),
            CNOGroup(
                cno_code="84",
                title="Conductores y operadores de maquinaria móvil (transporte, camiones, buses)",
                major_group=8,
                fte_employment=1_100_000,
                avg_monthly_gross_wage=1_680.0,
                wage_deciles=[1_250, 1_350, 1_450, 1_550, 1_660, 1_770, 1_900, 2_080, 2_350, 2_800],
                female_share=0.08,
                fixed_discontinuous_share=0.05,
                sector="Transport",
            ),
            # Group 9: Elementary occupations
            CNOGroup(
                cno_code="91",
                title="Personal de limpieza de oficinas, hoteles y otros establecimientos",
                major_group=9,
                fte_employment=1_350_000,
                avg_monthly_gross_wage=1_220.0,
                wage_deciles=[1_000, 1_080, 1_140, 1_200, 1_250, 1_310, 1_380, 1_470, 1_620, 1_950],
                female_share=0.82,
                fixed_discontinuous_share=0.12,
                sector="Services",
            ),
            CNOGroup(
                cno_code="94",
                title="Ayudantes de preparación de alimentos y peones del transporte/almacén",
                major_group=9,
                fte_employment=950_000,
                avg_monthly_gross_wage=1_260.0,
                wage_deciles=[1_020, 1_100, 1_160, 1_230, 1_290, 1_350, 1_430, 1_540, 1_700, 2_050],
                female_share=0.45,
                fixed_discontinuous_share=0.15,
                sector="Logistics",
            ),
            # Group 0: Armed forces
            CNOGroup(
                cno_code="01",
                title="Ocupaciones militares",
                major_group=0,
                fte_employment=110_000,
                avg_monthly_gross_wage=2_100.0,
                wage_deciles=[1_450, 1_600, 1_750, 1_900, 2_050, 2_200, 2_380, 2_600, 2_950, 3_600],
                female_share=0.13,
                fixed_discontinuous_share=0.00,
                sector="Public",
            ),
        ]
        return cls(groups)
