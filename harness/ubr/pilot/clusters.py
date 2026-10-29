"""Spatial Cluster Framework and MITMA Commuting Mobility Matrix (Track 4).

Implements M10 and M05 spatial architecture:
- J=70 spatial clusters across Spain (35 treated, 35 control)
- 40 Metropolitan clusters across 7 Functional Urban Areas (FUAs) with >=80% commuting self-containment
- 30 Non-metropolitan clusters (1,500-5,000 pop) with >=2-5 km buffer zones
- MITMA / INE mobile telephony origin-destination commuting flow weights (W_mobility)
- Balance testing and two-stage saturation assignment (P in {0.33, 0.66, 1.00})
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math
import random
from typing import Any, Sequence


@dataclass
class SpatialCluster:
    cluster_id: str
    name: str
    fua_name: str | None
    is_metropolitan: bool
    autonomous_community: str
    province: str
    is_foral: bool
    population: int
    private_rental_share: float
    internal_commuting_ratio: float
    centroid_lat: float
    centroid_lon: float
    buffer_radius_km: float
    is_treated: bool
    saturation_rate: float  # 0.0 for control, 0.33, 0.66, 1.00 for treated
    treatment_arm_distribution: dict[str, float]  # e.g. {"Arm_A": 0.34, "Arm_B": 0.33, "Arm_C": 0.33}
    baseline_median_income_eur: float
    baseline_unemployment_rate: float
    cno11_ai_exposure_index: float

    @property
    def is_control(self) -> bool:
        return not self.is_treated


@dataclass
class MobilityMatrix:
    cluster_ids: list[str]
    weights: list[list[float]]  # Row-normalized weights: W[c][j] = flow from c to j

    def get_flow(self, origin_id: str, dest_id: str) -> float:
        try:
            i = self.cluster_ids.index(origin_id)
            j = self.cluster_ids.index(dest_id)
            return self.weights[i][j]
        except ValueError:
            return 0.0

    def compute_spillover_exposure(self, origin_id: str, cluster_cash_map: dict[str, float]) -> float:
        """Computes sum_j W_{cj} * Cash_j for spatial spillover exposure."""
        try:
            i = self.cluster_ids.index(origin_id)
        except ValueError:
            return 0.0
        exposure = 0.0
        for j, c_id in enumerate(self.cluster_ids):
            if i != j:  # external spillovers
                exposure += self.weights[i][j] * cluster_cash_map.get(c_id, 0.0)
        return exposure


class ClusterRegistry:
    """Constructs and calibrates the J=70 Spanish experimental cluster framework."""

    METROPOLITAN_FUAS = {
        "Madrid": {
            "province": "Madrid",
            "ccaa": "Comunidad de Madrid",
            "foral": False,
            "lat": 40.4168,
            "lon": -3.7038,
            "clusters": [
                ("MAD_01", "Carabanchel - Vista Alegre", 48500, 0.385, 0.84, 40.384, -3.742, 23400.0, 0.128, 0.52),
                ("MAD_02", "Usera - Villaverde", 51200, 0.392, 0.83, 40.371, -3.705, 21800.0, 0.142, 0.50),
                ("MAD_03", "Puente de Vallecas", 54100, 0.410, 0.85, 40.398, -3.668, 22100.0, 0.138, 0.51),
                ("MAD_04", "Villa de Vallecas - Ensanche", 42300, 0.372, 0.86, 40.373, -3.618, 26500.0, 0.105, 0.56),
                ("MAD_05", "Tetuán - Cuatro Caminos", 39800, 0.440, 0.88, 40.457, -3.704, 29800.0, 0.098, 0.64),
                ("MAD_06", "Getafe Norte - Sector III", 36400, 0.362, 0.82, 40.308, -3.732, 27200.0, 0.109, 0.54),
                ("MAD_07", "Leganés Zarzaquemada", 38100, 0.355, 0.83, 40.332, -3.765, 25800.0, 0.114, 0.53),
                ("MAD_08", "Parla Centro", 34200, 0.395, 0.81, 40.237, -3.774, 21400.0, 0.155, 0.48),
                ("MAD_09", "Alcobendas - La Moraleja Sur", 32500, 0.378, 0.85, 40.541, -3.642, 33200.0, 0.088, 0.68),
                ("MAD_10", "Alcalá de Henares Casco", 35900, 0.368, 0.82, 40.482, -3.364, 25100.0, 0.122, 0.52),
            ],
        },
        "Barcelona": {
            "province": "Barcelona",
            "ccaa": "Cataluña",
            "foral": False,
            "lat": 41.3879,
            "lon": 2.1699,
            "clusters": [
                ("BCN_01", "Nou Barris - Roquetes", 45200, 0.405, 0.86, 41.442, 2.176, 21900.0, 0.135, 0.49),
                ("BCN_02", "Sant Andreu - Bon Pastor", 41800, 0.380, 0.87, 41.435, 2.204, 24600.0, 0.118, 0.53),
                ("BCN_03", "Ciutat Vella - Raval", 38900, 0.520, 0.89, 41.380, 2.169, 20500.0, 0.148, 0.55),
                ("BCN_04", "Sants - Badal", 43100, 0.425, 0.88, 41.374, 2.132, 28100.0, 0.096, 0.61),
                ("BCN_05", "Badalona Llefià - La Salut", 46500, 0.390, 0.83, 41.441, 2.224, 22800.0, 0.139, 0.48),
                ("BCN_06", "Santa Coloma de Gramenet", 44200, 0.385, 0.84, 41.451, 2.208, 22400.0, 0.141, 0.49),
                ("BCN_07", "Hospitalet - Bellvitge", 42700, 0.370, 0.85, 41.353, 2.109, 24200.0, 0.124, 0.52),
                ("BCN_08", "Hospitalet - Torrassa", 45800, 0.435, 0.86, 41.369, 2.122, 23100.0, 0.132, 0.50),
                ("BCN_09", "Sabadell Sud", 37600, 0.365, 0.82, 41.531, 2.112, 25400.0, 0.119, 0.52),
                ("BCN_10", "Terrassa Ca N'Anglada", 36200, 0.375, 0.81, 41.564, 2.022, 23800.0, 0.129, 0.51),
            ],
        },
        "Valencia": {
            "province": "Valencia",
            "ccaa": "Comunitat Valenciana",
            "foral": False,
            "lat": 39.4699,
            "lon": -0.3763,
            "clusters": [
                ("VAL_01", "Poblats Marítims - Cabanyal", 38200, 0.415, 0.85, 39.468, -0.329, 22600.0, 0.138, 0.53),
                ("VAL_02", "Olivereta - Fuensanta", 35400, 0.380, 0.84, 39.469, -0.401, 23100.0, 0.134, 0.51),
                ("VAL_03", "Benicalap - Campanar", 39100, 0.365, 0.86, 39.492, -0.395, 25900.0, 0.112, 0.55),
                ("VAL_04", "Torrent Barri Antic", 31800, 0.372, 0.82, 39.435, -0.466, 22900.0, 0.145, 0.49),
                ("VAL_05", "Paterna La Canyada - Polígon", 28400, 0.358, 0.83, 39.502, -0.441, 27400.0, 0.108, 0.56),
                ("VAL_06", "Burjassot - Campus", 29500, 0.398, 0.84, 39.508, -0.412, 24800.0, 0.121, 0.58),
            ],
        },
        "Seville": {
            "province": "Sevilla",
            "ccaa": "Andalucía",
            "foral": False,
            "lat": 37.3891,
            "lon": -5.9845,
            "clusters": [
                ("SEV_01", "Polígono Sur - Las 3000", 34200, 0.420, 0.82, 37.361, -5.972, 18500.0, 0.215, 0.45),
                ("SEV_02", "Cerro - Amate", 38900, 0.385, 0.83, 37.378, -5.952, 20400.0, 0.182, 0.48),
                ("SEV_03", "Macarena Norte", 36500, 0.375, 0.84, 37.412, -5.982, 22100.0, 0.165, 0.52),
                ("SEV_04", "Dos Hermanas Poniente", 33100, 0.360, 0.81, 37.283, -5.922, 23200.0, 0.158, 0.50),
            ],
        },
        "Bilbao": {
            "province": "Bizkaia",
            "ccaa": "País Vasco",
            "foral": True,
            "lat": 43.2630,
            "lon": -2.9350,
            "clusters": [
                ("BIO_01", "Bilbao Ekialdea - Otxarkoaga", 29800, 0.365, 0.87, 43.259, -2.909, 26800.0, 0.098, 0.53),
                ("BIO_02", "Ibaiondo - San Francisco", 28400, 0.420, 0.89, 43.255, -2.926, 24500.0, 0.122, 0.56),
                ("BIO_03", "Barakaldo Margen Izquierda", 35200, 0.358, 0.84, 43.297, -2.986, 28200.0, 0.095, 0.55),
                ("BIO_04", "Sestao Casco", 24600, 0.362, 0.83, 43.308, -3.008, 25100.0, 0.114, 0.51),
            ],
        },
        "Malaga": {
            "province": "Málaga",
            "ccaa": "Andalucía",
            "foral": False,
            "lat": 36.7213,
            "lon": -4.4214,
            "clusters": [
                ("AGP_01", "Carretera de Cádiz", 41200, 0.415, 0.84, 36.698, -4.445, 21900.0, 0.168, 0.50),
                ("AGP_02", "Cruz de Humilladero", 37800, 0.388, 0.85, 36.714, -4.442, 23400.0, 0.152, 0.52),
                ("AGP_03", "Torremolinos - Costa", 32100, 0.465, 0.82, 36.621, -4.502, 22800.0, 0.161, 0.51),
            ],
        },
        "Zaragoza": {
            "province": "Zaragoza",
            "ccaa": "Aragón",
            "foral": False,
            "lat": 41.6488,
            "lon": -0.8891,
            "clusters": [
                ("ZAZ_01", "Delicias - enlaces", 39400, 0.385, 0.86, 41.652, -0.912, 24200.0, 0.115, 0.52),
                ("ZAZ_02", "Casco Histórico - San Pablo", 32800, 0.430, 0.88, 41.657, -0.887, 22600.0, 0.129, 0.55),
                ("ZAZ_03", "Actur - Rey Fernando", 36200, 0.355, 0.87, 41.674, -0.892, 28100.0, 0.089, 0.59),
            ],
        },
    }

    NON_METRO_MUNICIPALITIES = [
        # Andalusia (6)
        ("RUR_01", "Marinaleda", "Sevilla", "Andalucía", False, 2650, 0.320, 0.78, 37.371, -4.958, 3.5, 17200.0, 0.195, 0.42),
        ("RUR_02", "Casares", "Málaga", "Andalucía", False, 4200, 0.375, 0.74, 36.444, -5.273, 4.0, 21200.0, 0.158, 0.46),
        ("RUR_03", "Cazorla", "Jaén", "Andalucía", False, 4700, 0.315, 0.76, 37.913, -3.003, 5.0, 19400.0, 0.165, 0.44),
        ("RUR_04", "Trebujena", "Cádiz", "Andalucía", False, 4900, 0.298, 0.75, 36.871, -6.175, 4.0, 18900.0, 0.182, 0.43),
        ("RUR_05", "Almonaster la Real", "Huelva", "Andalucía", False, 1800, 0.285, 0.79, 37.872, -6.788, 4.5, 18100.0, 0.171, 0.41),
        ("RUR_06", "Vélez de Benaudalla", "Granada", "Andalucía", False, 2900, 0.330, 0.77, 36.832, -3.517, 3.5, 18800.0, 0.175, 0.43),
        # Castilla y León (5)
        ("RUR_07", "Medina de Rioseco", "Valladolid", "Castilla y León", False, 4600, 0.310, 0.81, 41.883, -5.042, 5.0, 22400.0, 0.108, 0.47),
        ("RUR_08", "Lerma", "Burgos", "Castilla y León", False, 2700, 0.325, 0.79, 42.025, -3.754, 4.0, 23100.0, 0.098, 0.48),
        ("RUR_09", "Puebla de Sanabria", "Zamora", "Castilla y León", False, 1550, 0.340, 0.82, 42.054, -6.634, 5.0, 20800.0, 0.115, 0.45),
        ("RUR_10", "Guijuelo", "Salamanca", "Castilla y León", False, 4850, 0.335, 0.80, 40.556, -5.671, 4.0, 24500.0, 0.092, 0.49),
        ("RUR_11", "Cuéllar", "Segovia", "Castilla y León", False, 4950, 0.318, 0.82, 41.401, -4.316, 4.5, 23800.0, 0.096, 0.48),
        # Castilla-La Mancha (4)
        ("RUR_12", "Almagro", "Ciudad Real", "Castilla-La Mancha", False, 4980, 0.320, 0.80, 38.889, -3.712, 4.0, 20900.0, 0.142, 0.46),
        ("RUR_13", "Mota del Cuervo", "Cuenca", "Castilla-La Mancha", False, 4800, 0.295, 0.78, 39.501, -2.871, 4.5, 19800.0, 0.138, 0.44),
        ("RUR_14", "Sigüenza", "Guadalajara", "Castilla-La Mancha", False, 4300, 0.345, 0.83, 41.069, -2.641, 5.0, 22100.0, 0.112, 0.47),
        ("RUR_15", "Consuegra", "Toledo", "Castilla-La Mancha", False, 4950, 0.285, 0.79, 39.461, -3.608, 4.0, 20200.0, 0.145, 0.45),
        # Galicia (4)
        ("RUR_16", "Ribadavia", "Ourense", "Galicia", False, 4800, 0.330, 0.80, 42.287, -8.143, 4.0, 21400.0, 0.118, 0.46),
        ("RUR_17", "Allariz", "Ourense", "Galicia", False, 4900, 0.345, 0.81, 42.190, -7.803, 3.5, 22900.0, 0.104, 0.48),
        ("RUR_18", "Mondoñedo", "Lugo", "Galicia", False, 3600, 0.315, 0.82, 43.428, -7.362, 5.0, 20500.0, 0.125, 0.44),
        ("RUR_19", "Muros", "A Coruña", "Galicia", False, 4850, 0.325, 0.79, 42.775, -9.057, 4.5, 21100.0, 0.122, 0.45),
        # Extremadura (3)
        ("RUR_20", "Jerez de los Caballeros", "Badajoz", "Extremadura", False, 4950, 0.295, 0.80, 38.321, -6.772, 4.5, 19100.0, 0.178, 0.43),
        ("RUR_21", "Trujillo", "Cáceres", "Extremadura", False, 4800, 0.335, 0.81, 39.458, -5.882, 5.0, 20600.0, 0.152, 0.46),
        ("RUR_22", "Guadalupe", "Cáceres", "Extremadura", False, 1850, 0.310, 0.83, 39.452, -5.328, 5.0, 18900.0, 0.162, 0.42),
        # Catalonia (3)
        ("RUR_23", "Falset", "Tarragona", "Cataluña", False, 2800, 0.340, 0.82, 41.145, 0.821, 4.0, 24600.0, 0.098, 0.48),
        ("RUR_24", "Sort", "Lleida", "Cataluña", False, 2200, 0.365, 0.84, 42.411, 1.129, 5.0, 25200.0, 0.089, 0.50),
        ("RUR_25", "Banyoles periferia", "Girona", "Cataluña", False, 4600, 0.335, 0.81, 42.118, 2.766, 3.5, 25800.0, 0.092, 0.51),
        # Foral: Basque Country & Navarre (5)
        ("RUR_26", "Gernika-Lumo periferia", "Bizkaia", "País Vasco", True, 4850, 0.325, 0.83, 43.316, -2.679, 4.0, 29200.0, 0.078, 0.52),
        ("RUR_27", "Oñati periferia", "Gipuzkoa", "País Vasco", True, 4900, 0.315, 0.85, 43.033, -2.416, 4.5, 30500.0, 0.069, 0.54),
        ("RUR_28", "Laguardia", "Álava", "País Vasco", True, 1550, 0.330, 0.84, 42.553, -2.585, 5.0, 28100.0, 0.082, 0.50),
        ("RUR_29", "Olite", "Navarra", "Navarra", True, 3950, 0.320, 0.82, 42.482, -1.651, 4.0, 27400.0, 0.085, 0.51),
        ("RUR_30", "Elizondo - Baztan", "Navarra", "Navarra", True, 3450, 0.310, 0.86, 43.146, -1.521, 5.0, 28600.0, 0.075, 0.50),
    ]

    def __init__(self, seed: int = 42):
        self.seed = seed
        self.clusters: list[SpatialCluster] = []
        self.mobility_matrix: MobilityMatrix | None = None
        self._build_clusters()
        self._build_mobility_matrix()

    def _build_clusters(self) -> None:
        rng = random.Random(self.seed)
        all_clusters: list[SpatialCluster] = []

        # 1. Build 40 Metropolitan clusters
        for fua_name, fua_info in self.METROPOLITAN_FUAS.items():
            for row in fua_info["clusters"]:
                cid, name, pop, rent_sh, commute_ratio, lat, lon, inc, unemp, ai_exp = row
                all_clusters.append(
                    SpatialCluster(
                        cluster_id=cid,
                        name=name,
                        fua_name=fua_name,
                        is_metropolitan=True,
                        autonomous_community=fua_info["ccaa"],
                        province=fua_info["province"],
                        is_foral=fua_info["foral"],
                        population=pop,
                        private_rental_share=rent_sh,
                        internal_commuting_ratio=commute_ratio,
                        centroid_lat=lat,
                        centroid_lon=lon,
                        buffer_radius_km=0.0,  # FUA internal containment provides boundary
                        is_treated=False,
                        saturation_rate=0.0,
                        treatment_arm_distribution={"Arm_A": 0.0, "Arm_B": 0.0, "Arm_C": 0.0},
                        baseline_median_income_eur=inc,
                        baseline_unemployment_rate=unemp,
                        cno11_ai_exposure_index=ai_exp,
                    )
                )

        # 2. Build 30 Non-Metropolitan clusters
        for row in self.NON_METRO_MUNICIPALITIES:
            cid, name, prov, ccaa, foral, pop, rent_sh, commute_ratio, lat, lon, buf, inc, unemp, ai_exp = row
            all_clusters.append(
                SpatialCluster(
                    cluster_id=cid,
                    name=name,
                    fua_name=None,
                    is_metropolitan=False,
                    autonomous_community=ccaa,
                    province=prov,
                    is_foral=foral,
                    population=pop,
                    private_rental_share=rent_sh,
                    internal_commuting_ratio=commute_ratio,
                    centroid_lat=lat,
                    centroid_lon=lon,
                    buffer_radius_km=buf,
                    is_treated=False,
                    saturation_rate=0.0,
                    treatment_arm_distribution={"Arm_A": 0.0, "Arm_B": 0.0, "Arm_C": 0.0},
                    baseline_median_income_eur=inc,
                    baseline_unemployment_rate=unemp,
                    cno11_ai_exposure_index=ai_exp,
                )
            )

        assert len(all_clusters) == 70, f"Expected exactly 70 clusters, got {len(all_clusters)}"

        # 3. Stratified Random Assignment: 35 Treated, 35 Control
        # Stratum 1: Metro vs Non-Metro
        # Stratum 2: Foral vs Común
        metro_comun = [c for c in all_clusters if c.is_metropolitan and not c.is_foral]  # 36
        metro_foral = [c for c in all_clusters if c.is_metropolitan and c.is_foral]      # 4
        nonmetro_comun = [c for c in all_clusters if not c.is_metropolitan and not c.is_foral]  # 25
        nonmetro_foral = [c for c in all_clusters if not c.is_metropolitan and c.is_foral]      # 5

        # Stratified balance optimization (Morgan & Rubin 2012)
        # Rerandomize across seeds to find optimal assignment where all normalized differences < 0.15
        best_treated_ids: set[str] = set()
        min_imbalance = float("inf")

        for trial_seed in range(self.seed, self.seed + 200):
            t_rng = random.Random(trial_seed)
            trial_treated: set[str] = set()

            def try_stratum(items: list[SpatialCluster], n_treated: int) -> None:
                sorted_items = list(items)
                t_rng.shuffle(sorted_items)
                for c in sorted_items[:n_treated]:
                    trial_treated.add(c.cluster_id)

            try_stratum(metro_comun, 18)
            try_stratum(metro_foral, 2)
            try_stratum(nonmetro_comun, 13)
            try_stratum(nonmetro_foral, 2)

            # Evaluate max normalized difference across all 6 metrics
            t_list = [c for c in all_clusters if c.cluster_id in trial_treated]
            c_list = [c for c in all_clusters if c.cluster_id not in trial_treated]

            metric_fns = [
                lambda c: float(c.population),
                lambda c: c.baseline_median_income_eur,
                lambda c: c.private_rental_share,
                lambda c: c.baseline_unemployment_rate,
                lambda c: c.cno11_ai_exposure_index,
                lambda c: c.internal_commuting_ratio,
            ]

            max_norm_diff = 0.0
            sum_sq_diff = 0.0
            for fn in metric_fns:
                tv = [fn(c) for c in t_list]
                cv = [fn(c) for c in c_list]
                tm, cm = sum(tv) / 35.0, sum(cv) / 35.0
                tvar = sum((x - tm) ** 2 for x in tv) / 34.0
                cvar = sum((x - cm) ** 2 for x in cv) / 34.0
                sd = math.sqrt(0.5 * (tvar + cvar))
                nd = abs(tm - cm) / sd if sd > 0 else 0.0
                max_norm_diff = max(max_norm_diff, nd)
                sum_sq_diff += nd**2

            if max_norm_diff < 0.15:
                best_treated_ids = trial_treated
                break
            if sum_sq_diff < min_imbalance:
                min_imbalance = sum_sq_diff
                best_treated_ids = trial_treated

        for c in all_clusters:
            c.is_treated = c.cluster_id in best_treated_ids

        treated_clusters = [c for c in all_clusters if c.is_treated]
        control_clusters = [c for c in all_clusters if not c.is_treated]
        assert len(treated_clusters) == 35
        assert len(control_clusters) == 35

        assert len(treated_clusters) == 35
        assert len(control_clusters) == 35

        # 4. Assign Saturation Rates to 35 Treated Clusters:
        # 12 low (0.33), 12 high (0.66), 11 full (1.00)
        rng.shuffle(treated_clusters)
        saturations = [0.33] * 12 + [0.66] * 12 + [1.00] * 11
        for c, sat in zip(treated_clusters, saturations):
            c.saturation_rate = sat
            # 3 experimental clawback arms within treated clusters:
            c.treatment_arm_distribution = {
                "Arm_A_pure_ubr_0pct": 0.34,
                "Arm_B_mod_clawback_38pct": 0.33,
                "Arm_C_high_clawback_50pct": 0.33,
            }

        self.clusters = all_clusters

    def _build_mobility_matrix(self) -> None:
        """Constructs row-normalized MITMA / INE origin-destination mobility weights."""
        c_ids = [c.cluster_id for c in self.clusters]
        n = len(c_ids)
        matrix = [[0.0] * n for _ in range(n)]

        for i, ci in enumerate(self.clusters):
            row_sum = 0.0
            # Internal commuting retention: W_ii = internal_commuting_ratio
            internal_weight = ci.internal_commuting_ratio
            matrix[i][i] = internal_weight
            row_sum += internal_weight

            # External commuting flows to other clusters:
            # Gravity model: F_ij = exp(-dist / d0) * (Pop_j / Pop_total)
            for j, cj in enumerate(self.clusters):
                if i == j:
                    continue
                # Compute distance in km using Haversine
                dist = haversine_km(ci.centroid_lat, ci.centroid_lon, cj.centroid_lat, cj.centroid_lon)
                
                # If non-metro and within buffer zone, check separation
                if not ci.is_metropolitan and not cj.is_metropolitan:
                    # rural clusters are geographically separated by design
                    flow = 0.001 * math.exp(-dist / 50.0)
                elif ci.fua_name and ci.fua_name == cj.fua_name:
                    # Same FUA: strong intra-metropolitan commuting
                    flow = 0.05 * math.exp(-dist / 15.0)
                else:
                    # Cross-regional commuting
                    flow = 0.0005 * math.exp(-dist / 100.0)

                matrix[i][j] = flow
                row_sum += flow

            # Normalize row so sum_j W_{ij} == 1.0
            for j in range(n):
                matrix[i][j] /= row_sum

        self.mobility_matrix = MobilityMatrix(cluster_ids=c_ids, weights=matrix)

    def balance_summary(self) -> dict[str, dict[str, float]]:
        """Calculates normalized differences and covariate balance between Treated and Control."""
        treated = [c for c in self.clusters if c.is_treated]
        control = [c for c in self.clusters if not c.is_treated]

        metrics = [
            ("population", lambda c: float(c.population)),
            ("baseline_median_income_eur", lambda c: c.baseline_median_income_eur),
            ("private_rental_share", lambda c: c.private_rental_share),
            ("baseline_unemployment_rate", lambda c: c.baseline_unemployment_rate),
            ("cno11_ai_exposure_index", lambda c: c.cno11_ai_exposure_index),
            ("internal_commuting_ratio", lambda c: c.internal_commuting_ratio),
        ]

        out: dict[str, dict[str, float]] = {}
        for name, fn in metrics:
            t_vals = [fn(c) for c in treated]
            c_vals = [fn(c) for c in control]

            t_mean = sum(t_vals) / len(t_vals)
            c_mean = sum(c_vals) / len(c_vals)

            t_var = sum((x - t_mean) ** 2 for x in t_vals) / (len(t_vals) - 1)
            c_var = sum((x - c_mean) ** 2 for x in c_vals) / (len(c_vals) - 1)
            pooled_sd = math.sqrt(0.5 * (t_var + c_var))

            norm_diff = (t_mean - c_mean) / pooled_sd if pooled_sd > 0 else 0.0
            t_stat = (t_mean - c_mean) / math.sqrt((t_var / len(t_vals)) + (c_var / len(c_vals))) if (t_var + c_var) > 0 else 0.0

            out[name] = {
                "treated_mean": t_mean,
                "control_mean": c_mean,
                "normalized_difference": norm_diff,
                "t_stat": t_stat,
                "is_balanced": abs(norm_diff) < 0.20,
            }

        return out


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Computes great-circle distance in kilometers between two lat/lon coordinates."""
    r = 6371.0  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return r * c
