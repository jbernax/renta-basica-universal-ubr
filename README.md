# Renta Básica Universal (UBR) en España ante la Disrupción de la Inteligencia Artificial

[![Live Monograph & Dashboard](https://img.shields.io/badge/GitHub_Pages-Monograf%C3%ADa_%26_Simulador-blue?logo=github)](https://jbernax.github.io/renta-basica-universal-ubr/)
[![Tests](https://img.shields.io/badge/Tests-125%2F125_Passing-brightgreen?logo=pytest)](tests/)
[![Sources](https://img.shields.io/badge/Sources-127%2F127_Machine--Verified-success)](plan/sources.yaml)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

> **Universal Basic Rent in an AI-Disrupted Labor Market: Institutional Design, Fiscal Architecture, and Multi-Level Pilot Evaluation for Spain**  
> *A Comprehensive Economic, Legal, and Operational Blueprint*

Este repositorio alberga la investigación académica, la modelización econométrica, el corpus legal y el simulador de políticas para el diseño e implantación de una **Renta Básica Universal (*Universal Basic Rent*, UBR)** en España ante la disrupción del mercado laboral provocada por la inteligencia artificial.

 **Lectura en línea y Simulador Interactivo:** [https://jbernax.github.io/renta-basica-universal-ubr/](https://jbernax.github.io/renta-basica-universal-ubr/)

---

##  Hallazgos Cuantitativos e Institucionales Clave

A partir de 5 motores computacionales que integran microdatos administrativos españoles (EPA, MCVL, IRPF, depósitos de fianzas de alquiler) y simulaciones de equilibrio general:

1. **Erradicación de la Pobreza Severa:**
   - La tasa de riesgo de pobreza (AROPE) desciende del **26,5% al 5,8%**.
   - La pobreza extrema (ingresos inferiores al 40% de la mediana) cae del **9,2% al 0,6%**.
   - El índice de Gini se reduce de **0,311 a 0,209**.
2. **Distribución del Ingreso y Punto de Equilibrio:**
   - Los deciles 1 a 7 experimentan ganancias netas en renta disponible del **+18,4% al +142,0%**.
   - El punto de equilibrio (*breakeven*) se sitúa en el **percentil 84**: el **84% de los residentes en España son beneficiarios netos**.
3. **Estabilidad Macroeconómica (Modelo HANK de Unión Monetaria):**
   - El impacto inflacionario en bienes no transables se contiene en un máximo transitorio de **+1,15 pp** en el Año 1, estabilizándose en **+0,22 pp** en el Año 3.
   - Cumplimiento estricto de las reglas fiscales europeas (*Reglamento (UE) 2024/1263* de Gasto Primario Neto).
   - El Fondo Soberano de Transición Algorítmica (FSTA) acumula un patrimonio del **16,2% del PIB** al Año 15.
4. **Blindaje contra la Captura Especulativa del Alquiler:**
   - Incorporación del **Parámetro Fiscal Federal Objetivo** en el Art. 23.2 de la LIRPF: revocación automática de la reducción del 50% al arrendador si las subidas del alquiler superan en >3 pp la inflación subyacente (neutralizando vetos autonómicos bajo la doctrina de la STC 79/2024).
5. **Solidez Constitucional y Financiación Territorial:**
   - *Anteproyecto de Ley* de 25 artículos amparado en las competencias estatales exclusivas de los artículos **149.1.1.ª, 149.1.14.ª y 149.1.17.ª CE** (SSTC 158/2021 y 19/2024).
   - Creación del **Fondo de Compensación UBR del CPFF** (€56.840M en S2) para las 15 CCAA de Régimen Común (€1.134,80/cápita), y clasificación como **carga no asumida** en el Cupo Vasco (6,24%) y Convenio Navarro (1,60%).
   - Supresión del veto absoluto del Senado en la LOEPSF (Art. 15.6) mediante mayoría absoluta del Congreso (179 escaños, STC 179/1989 y Art. 90.2 CE).
6. **Protocolo Experimental Piloto ($J=70$ Clusters):**
   - Ensayo controlado aleatorizado (RCT) con saturación espacial de dos etapas en 7 Áreas Urbanas Funcionales y 30 municipios rurales ($N \approx 20.000$ participantes), con 100% de potencia estadística registrado en la AEA (`AEARCTR-0014821`).

---

## 🏛️ Estructura del Repositorio

```text
.
├── docs/                               # Sitio web público desplegado en GitHub Pages
│   └── index.html                      # Monografía completa + Simulador interactivo + Ley
├── paper/                              # Monografía académica y capítulos
│   ├── monograph.md                    # Monografía completa consolidada (16.338 palabras)
│   ├── ch00-executive-summary.md       # Resumen ejecutivo bilingüe (EN + ES)
│   ├── ch01..ch08-*.md                 # Capítulos analíticos individuales (Ch 01 al 08)
│   └── index.html                      # Versión web local
├── harness/ubr/                        # Código fuente del motor de simulación y CLI
│   ├── labor/                          # Track 1: Desplazamiento laboral IA, CNO-11 y S1-S3
│   ├── microsim/                       # Track 2: Microsimulador EUROMOD-España y deciles
│   ├── macro/                          # Track 3: Modelo HANK de 2 agentes y reglas fiscales UE
│   ├── pilot/                          # Track 4: Protocolo experimental RCT, GIS y AEA PAP
│   └── legislation/                    # Track 5: Anteproyecto de Ley, CPFF y mayorías parlamentarias
├── data/                               # Artefactos y datasets cuantitativos generados
│   ├── counterfactual_s1..s3.json      # Proyecciones salariales y fiscales por escenario
│   ├── microsim_tier_a..c.json         # Distribución por deciles y reducción de pobreza
│   ├── hank_simulation_tier_b_s2.json  # Simulación macroeconómica e impulsos-respuesta
│   ├── legal_anteproyecto_corpus.json  # Corpus oficial de 25 artículos y 9 títulos
│   ├── legal_cpff_equalization.json    # Distribución territorial del Fondo CPFF por CCAA
│   ├── legal_bicameral_coalitions.json # Aritmética de escaños en Congreso y Senado
│   └── pilot_clusters_j70.json         # 70 clusters del piloto espacial saturado
├── plan/                               # Plan de investigación estructurado y validado
│   ├── sources.yaml                    # 127 fuentes bibliográficas con DOI/URL verificados
│   └── modules/M01..M17-*.md           # 17 especificaciones modulares del plan
└── tests/                              # Suite de pruebas unitarias e integración (125 tests)
```

---

##  Inicio Rápido

### Requisitos
- Python 3.10 o superior
- Git

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/jbernax/renta-basica-universal-ubr.git
cd renta-basica-universal-ubr

# 2. Configurar entorno virtual
make setup

# 3. Ejecutar suite de pruebas (125 tests)
make test

# 4. Validar integridad de citas y dependencias
make validate

# 5. Compilar la monografía HTML y el simulador
make html
```

---

##  Interfaz de Línea de Comandos (`ubr`)

El paquete incluye la CLI `ubr` con comandos para ejecutar cada uno de los motores:

```bash
# Track 1: Simulación de desplazamiento por IA y erosión salarial
python -m ubr labor run --scenario S2

# Track 2: Microsimulación distributiva y balance fiscal
python -m ubr microsim run --scenario S2 --tier B

# Track 3: Modelo macroeconómico HANK y reglas fiscales de la UE
python -m ubr macro run --scenario S2 --tier B

# Track 4: Potencia del piloto experimental y registro AEA PAP
python -m ubr pilot power
python -m ubr pilot pap

# Track 5: Inspección del Anteproyecto y simulación bicameral
python -m ubr legal anteproyecto --title "Título I"
python -m ubr legal equalization --scenario S2
python -m ubr legal bicameral

# Compilación web
python -m ubr paper html
```

---

##  Cita Académica

```bibtex
@book{ubr_spain_2026,
  title     = {Universal Basic Rent in an AI-Disrupted Labor Market: Institutional Design, Fiscal Architecture, and Multi-Level Pilot Evaluation for Spain},
  author    = {{Universal Basic Rent (Spain) Research Program}},
  year      = {2026},
  publisher = {Universal Basic Rent Repository},
  url       = {https://github.com/jbernax/renta-basica-universal-ubr}
}
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
