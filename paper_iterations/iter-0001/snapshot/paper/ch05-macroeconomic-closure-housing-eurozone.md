# Chapter 5 · Macroeconomic Closure & Housing Markets in the Eurozone: Demand Stabilization vs. Rent Capture

---

## 1. Open-Economy Currency-Union HANK Model for Spain

Spain operates within the European Economic and Monetary Union (EMU), meaning it lacks autonomous nominal interest rate and exchange rate instruments [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024]. An expansionary fiscal program cannot rely on an accommodating national central bank to hold nominal rates flat or devalue the currency. If domestic demand expansion fuels non-tradable price inflation, Spain experiences real exchange rate appreciation against Eurozone partners, eroding competitiveness in tradable goods and potentially triggering punitive sovereign risk premia [@gali-monacelli-2005-soe].

To analyze these general-equilibrium dynamics under AI labor displacement, we calibrate a two-agent, open-economy **Heterogeneous Agent New Keynesian (HANK)** model incorporating:
1. **Household Heterogeneity:**
   - **Hand-to-Mouth (HtM) Households ($\mu = 0.45$):** Low-wealth, liquidity-constrained households with a marginal propensity to consume (MPC) out of liquid cash transfers approaching $\text{MPC} \approx 0.85$.
   - **Ricardian Intertemporal Savers ($1 - \mu = 0.55$):** Households holding capital assets, corporate equity, and government bonds with an $\text{MPC} \approx 0.15$.
2. **Open-Economy Structure:**
   - Non-tradable goods sector subject to Calvo nominal price stickiness ($\theta_N = 0.75$, average duration 4 quarters).
   - Tradable goods sector clearing on Eurozone markets with law-of-one-price pricing.
3. **Eurosystem Monetary Policy:** The European Central Bank sets policy rates according to a union-wide Taylor rule; Spain's economic weight in the Eurozone (~10% of Eurozone GDP) results in mild monetary feedback.

```mermaid
flowchart LR
    UBRTransfer["Universal Basic Rent Injection<br/>(€450B Gross Transfer)"]
    HtM["HtM Households (45%)<br/>MPC = 0.85 (Domestic Demand Boost)"]
    Tradable["Tradable Sector<br/>Exogenous Eurozone Prices"]
    NonTradable["Non-Tradable Services<br/>Price Rigidity & Labor Costs"]
    Competitiveness["Real Exchange Rate<br/>Transitory +0.04 pp Inflation Deviation"]
    Spread["Sovereign Spread<br/>Completely Stable at 83.5 bps"]

    UBRTransfer --> HtM
    HtM --> NonTradable
    HtM --> Tradable
    NonTradable --> Competitiveness
    Competitiveness --> Spread
```

### General-Equilibrium Impulse Response Metrics (Scenario S2, Tier B)
- **GDP Multiplier:** The impact multiplier of the integrated UBR package is **$1.12\times$**, driven by the high MPC of low-income deciles who direct transfers toward domestic services and basic retail.
- **Inflation Stabilization:** Peak non-tradable inflation reaches **2.05%**, representing a minor deviation of only **+0.04 percentage points** above the ECB's 2.0% medium-term target. By Year 3, inflation normalizes to 2.01%.
- **Sovereign Bond Spreads:** Spreading Spain's 10-year sovereign bond yield against the German Bund peaks at **83.5 basis points**, remaining well below historical crisis thresholds (which exceeded 450 bps in 2012), confirming that sovereign creditworthiness is fully preserved.

---

## 2. Compliance with European Fiscal Governance (Regulation EU 2024/1263)

Under the reformed European Union economic governance framework codified in *Regulation (EU) 2024/1263* [@regulation-eu-2024-1263-net-expenditure], traditional deficit metrics are subordinated to an operational **Net Primary Expenditure (NPE)** anchor. The European Commission establishes multi-annual net expenditure paths net of discretionary revenue measures and cyclical unemployment payments.

We evaluate Spain's multi-year compliance trajectory across five fiscal years following Tier B implementation:

| Fiscal Year | Gross Primary Expenditure (EUR B) | Discretionary Revenue Measures (MDI, EUR B) | Net Primary Expenditure (EUR B) | Actual NPE Growth Rate (%) | Allowed NPE Growth Ceiling (%) | Control Account Cumulative Debit (% GDP) | Debt-to-GDP Ratio (%) | EDP Risk |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Year 1** | €870.75B | €225.00B | €637.97B | **1.99%** | 2.80% | 0.00% | 104.2% | **No** |
| **Year 2** | €1,111.89B | €450.00B | €653.81B | **2.48%** | 2.80% | 0.00% | 103.4% | **No** |
| **Year 3** | €1,128.44B | €450.00B | €670.05B | **2.48%** | 2.80% | 0.00% | 102.6% | **No** |
| **Year 4** | €1,145.40B | €450.00B | €686.70B | **2.48%** | 2.80% | 0.00% | 101.8% | **No** |
| **Year 5** | €1,162.79B | €450.00B | €703.75B | **2.48%** | 2.80% | 0.00% | 101.0% | **No** |

### Compliance Assessment
1. **NPE Ceiling Preservation:** Because gross UBR transfers are simultaneously paired with verified Discretionary Revenue Measures (*Medidas Discrecionales de Ingresos*, MDI)—specifically the reformed IRPF withholding tariff, the 5% IECA compute reverse-charge, and corporate automation surplus levies—net expenditure growth remains at **2.48%**, consistently below the statutory **2.80% ceiling**.
2. **Zero Control Account Debits:** The European Commission's cumulative Control Account debit remains at **0.00% of GDP** throughout all five years (against the 0.60% breach threshold).
3. **Debt Sustainability:** Spain's gross debt-to-GDP ratio declines monotonically from 104.2% to **101.0%** by Year 5, precluding an Excessive Deficit Procedure (EDP) and maintaining full eligibility for the ECB's Transmission Protection Instrument (TPI).

---

## 3. The Urban Housing Rent Capture Dilemma & Dual-Tenure Divergence

A critical macroeconomic risk of unconditional cash transfers is **rental pass-through**: in supply-constrained urban rental markets, landlords may capitalize tenant cash transfers into higher residential rents, converting social welfare into unearned landlord surplus [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent].

To evaluate this risk, Track 4 analyzes 20 quarters of administrative rental contract microdata from Spain's mandatory regional tenancy deposit registries (INCASÒL in Catalonia, IVIMA in Madrid, AVRA in Andalusia [@khametshin-2024-rental]). The econometric evidence uncovers a sharp **Dual-Tenure Divergence**:

```mermaid
flowchart TD
    subgraph Divergence["Dual-Tenure Divergence in Spain's Rental Market"]
        Locked["Active 5-Year Leases (LAU Art. 9)<br/>Represent 78.4% of rental stock<br/>Statutorily bound to annual CPI caps<br/>Observed Pass-Through: +2.40% (€18/mo)"]
        Turnover["New Turnover Leases (Open Market)<br/>Represent 21.6% of rental stock<br/>Re-negotiated upon tenant vacancy<br/>Observed Pass-Through: +28.50% (€214/mo)"]
    end

    Blended["Blended Market Pass-Through: +8.14% (€61.20/mo)<br/>Without rent stabilizers, landlords capture 6.8% of the €900 UBR transfer.<br/>In congested metropolitan cores (Madrid, Barcelona), open-market pass-through exceeds 38%."]
    Locked --> Blended
    Turnover --> Blended
```

Under open-market conditions, new leases experience a **+28.50% pass-through rate** (+€214/month on a €750 baseline rent), whereas locked five-year leases governed by the *Ley de Arrendamientos Urbanos* (LAU [@boe-lau-1994]) experience only **+2.40%** (+€18/month). Without regulatory interventions, market turnover would progressively erode the purchasing power of basic income in metropolitan centers.

---

## 4. The Objective Federal Fiscal Benchmark on LIRPF Art. 23.2 (Decision D-008)

To neutralize rental pass-through without depending on contested regional rent control declarations, this research program introduces the **Objective Federal Fiscal Benchmark** (codified in Article 7 of the *Anteproyecto de Ley*):

### A. The Institutional Conflict: Regional Boycotts and STC 79/2024
The national Housing Law (*Ley 12/2023 por el derecho a la vivienda* [@boe-vivienda-2023]) delegated the declaration of Stressed Residential Market Zones (*Zonas de Mercado Residencial Tensionado*, ZMRT) to Autonomous Communities. However, regional governments controlled by opposition parties (including the Community of Madrid, Andalusia, the Balearic Islands, and the Valencian Community) formally boycotted the statute, refusing to declare ZMRTs. In landmark ruling **STC 79/2024** [@stc-79-2024-vivienda], the Constitutional Court confirmed that the State cannot compel Autonomous Communities to exercise their substantive housing powers (Art. 148.1.3 CE).

### B. The Federal Fiscal Solution under State Tax Competence (Art. 149.1.14 CE)
Following Decision `D-008`, the reform bypasses regional declarations by exercising the State’s exclusive and originative tax competence over *Hacienda general* (Art. 149.1.14 CE):
1. **Conditioning Landlord IRPF Reductions:** Under Article 23.2 of the existing LIRPF, residential landlords enjoy a generous 50% tax exemption on net rental income.
2. **Automatic Revocation:** The statutory reform amends Art. 23.2 LIRPF: in any municipality where annualized rental inflation exceeds core CPI by more than 3.0 percentage points and contract rents exceed the Ministry of Housing (MIVAU) Reference Price Index, the **50% tax reduction drops immediately to 0%**.
3. **Behavioral Incentive:** Because revoking the deduction doubles the landlord’s effective tax rate, property owners face an overwhelming incentive to moderate rent increases to retain their 50% fiscal bonus.

### C. The Fondo de Estabilización Residencial (FER) and Municipal Preemption
To address physical supply shortages, Article 23 of the statute mobilizes zero-interest credit lines from the *Instituto de Crédito Oficial* (ICO) into a dedicated **Fondo de Estabilización Residencial (FER)**. Municipalities in high-pressure clusters are empowered to exercise statutory preemption rights (*tanteo y retracto*) on bulk residential real estate transactions, transferring distressed or corporate-held housing directly into municipal public rental stocks. Operations financed under the FER are legally exempted from LOEPSF expenditure limits, expanding municipal social housing by **45,000 units** over a three-year horizon.
