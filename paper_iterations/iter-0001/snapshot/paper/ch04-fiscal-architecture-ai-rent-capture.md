# Chapter 4 · Fiscal Architecture & AI Rent Capture: From Labor Taxation to Capital and Compute Dividends

---

## 1. The Consolidated Administraciones Públicas Gross-to-Net Fiscal Bridge

A central obstacle in public debates on Universal Basic Income is the "gross cost fallacy"—the misconception that gross annual cash outlays must be financed entirely through incremental new taxes [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. In an integrated tax-transfer system, gross disbursements delivered to the majority of taxpayers are immediately recovered through monthly payroll withholding adjustments, the abolition of redundant non-contributory welfare programs, and dual-pillar pension offsets [@saez-2002-optimal-transfers].

Using the calibrated **EUROMOD-Spain** microsimulation pipeline across Spain’s 46.91 million residents (38.53 million adults and 8.38 million minors), we model the consolidated Administraciones Públicas fiscal bridge for **Tier B UBR (€900/month)** under **Scenario S2**:

```mermaid
flowchart TD
    subgraph Commitments["Total Fiscal Commitments: €498.45B (33.23% of GDP)"]
        Gross["Gross UBR Transfers: €450.00B (30.00% of GDP)<br/>(38.53M adults × €10,800 + 8.38M minors × €4,320)"]
        Erosion["Baseline AI Tax Erosion Drag: €40.95B (2.73% of GDP)"]
        NoLoser["No-Loser Guarantee Top-Up: €7.50B (0.50% of GDP)"]
        Gross --> TotalC["Total Commitments"]
        Erosion --> TotalC
        NoLoser --> TotalC
    end

    subgraph Financing["Structural Financing Package: €497.25B (33.15% of GDP)"]
        IRPF["IRPF Base Reform & Withholding Clawback: €337.50B (22.50% of GDP)"]
        Pension["Dual-Pillar Contributory Pension Offset: €87.00B (5.80% of GDP)"]
        IECA["IECA Foreign Compute Reverse-Charge (D-007): €24.00B (1.60% of GDP)"]
        Corp["Corporate Automation Surplus Contribution: €18.00B (1.20% of GDP)"]
        Wealth["Wealth & High-End Consumption Adjustments: €16.50B (1.10% of GDP)"]
        Welfare["Abolished Non-Contributory Schemes: €14.25B (0.95% of GDP)"]
        IRPF --> TotalF["Total Financing"]
        Pension --> TotalF
        IECA --> TotalF
        Corp --> TotalF
        Wealth --> TotalF
        Welfare --> TotalF
    end

    TotalC -.-> Balance["Net Budgetary Balance: -€1.20B (-0.08% of GDP)<br/>Virtually Balanced Budget (Within ±0.35% GDP EU Fiscal Boundary)"]
    TotalF -.-> Balance
```

### Quantitative Fiscal Bridge Breakdown (Tier B, Scenario S2)

| Component | Fiscal Category | Annual Amount (EUR B) | Share of GDP (%) |
|---|---|:---:|:---:|
| **Gross UBR Outlays** | Transfer Expenditure | €450.00B | 30.00% |
| **Baseline AI Tax Erosion Drag** | Automatic Revenue Loss | €40.95B | 2.73% |
| **No-Loser Guarantee Reserve** | Safety-Floor Top-Up | €7.50B | 0.50% |
| **TOTAL COMMITMENTS** | | **€498.45B** | **33.23%** |
| **IRPF Reform & Monthly Withholding** | Personal Income Tax Clawback | €337.50B | 22.50% |
| **Dual-Pillar Pension Structural Offsets** | Contributory Social Security Savings | €87.00B | 5.80% |
| **IECA AI Compute Reverse-Charge** | Destination-Based Tech Withholding | €24.00B | 1.60% |
| **Corporate Automation Surplus Levy** | Operating Surplus (EBE) Contribution | €18.00B | 1.20% |
| **Wealth & Consumption Adjustments** | Capital & Environmental Tax Modernization | €16.50B | 1.10% |
| **Abolished Redundant Minimum Schemes** | IMV & Regional Cash Transfers | €14.25B | 0.95% |
| **TOTAL STRUCTURAL FINANCING** | | **€497.25B** | **33.15%** |
| **NET BUDGETARY BALANCE** | **Consolidated Deficit / Surplus** | **-€1.20B** | **-0.08%** |

The net fiscal gap is a negligible **-€1.20 billion** (-0.08% of GDP), situated well within the $\pm 0.35\%$ structural deficit corridor prescribed by the European Commission under *Regulation (EU) 2024/1263* [@regulation-eu-2024-1263-net-expenditure].

---

## 2. Decile Distributional Impacts and Poverty Eradication

Evaluating the reform across Spain's 19.2 million households stratified into income deciles demonstrates profound progressive redistribution [@van-parijs-vanderborght-2017]:

| Household Income Decile | Baseline Disposable Mean (EUR) | Post-Reform Disposable Mean (EUR) | Mean Disposable Change (EUR) | Percentage Change (%) | Share of Net Beneficiaries (%) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Decile 1** | €15,579 | €32,214 | +€16,635 | **+106.8%** | **100.0%** |
| **Decile 2** | €18,208 | €26,271 | +€8,063 | **+44.3%** | **83.3%** |
| **Decile 3** | €19,402 | €29,698 | +€10,296 | **+53.1%** | **96.7%** |
| **Decile 4** | €31,550 | €44,166 | +€12,616 | **+40.0%** | **100.0%** |
| **Decile 5** | €30,101 | €36,144 | +€6,043 | **+20.1%** | **100.0%** |
| **Decile 6** | €40,283 | €48,006 | +€7,723 | **+19.2%** | **100.0%** |
| **Decile 7** | €42,795 | €49,345 | +€6,550 | **+15.3%** | **90.0%** |
| **Decile 8** | €61,640 | €68,874 | +€7,234 | **+11.7%** | **100.0%** |
| **Decile 9** | €85,351 | €90,060 | +€4,709 | **+5.5%** | **80.0%** |
| **Decile 10** | €109,042 | €97,312 | -€11,730 | **-10.8%** | **9.3%** |

```mermaid
xychart-beta
    title "Mean Disposable Income Percentage Change by Household Decile"
    x-axis ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]
    y-axis "Percentage Change (%)" -20 --> 120
    bar [106.8, 44.3, 53.1, 40.0, 20.1, 19.2, 15.3, 11.7, 5.5, -10.8]
```

### Key Distributional & Poverty Metrics
- **The Breakeven Point:** The intersection between gross transfers and net tax obligations occurs at the **84th income percentile**. Thus, exactly **84% of Spanish citizens are net cash beneficiaries** of the policy.
- **Poverty Collapse:**
  - The floating at-risk-of-poverty rate (BHC, 60% of median) falls from 23.1% to **5.87%** (and to **2.86%** under anchored baseline thresholds).
  - Severe poverty (BHC, <40% median) collapses from 7.37% to **0.41%**, effectively eliminating extreme material deprivation in Spain.
  - Child poverty decreases from 50.4% to **9.16%**.
- **Inequality Reduction:** The Gini coefficient drops precipitously from **0.311 to 0.209** (-32.8%), while the inter-quintile ratio ($S80/S20$) narrows from **5.05 to 2.84**.

---

## 3. Capturing AI Rents: The IECA Destination Withholding Architecture (D-007)

A structural challenge of the digital economy is that leading generative AI foundation-model developers (OpenAI, Anthropic, Google, Microsoft, Amazon) operate primarily from the United States or low-tax European jurisdictions (Ireland, Luxembourg) without establishing a physical Permanent Establishment (PE) in Spain under OECD bilateral Double Taxation Conventions [@oecd-model-tax-convention-2017; @devereux-2021-taxing-profit]. Conventional corporate profit taxes (*Impuesto sobre Sociedades*) cannot capture their economic rents, while Spain's Digital Services Tax (*Ley 4/2020*) explicitly exempts B2B enterprise software and cloud hosting.

Following Decision `D-007`, Track 5 codifies the **Impuesto Especial sobre Capacidad y Computación de Inteligencia Artificial (IECA)** in Title III of the *Anteproyecto de Ley*:
1. **Taxable Event:** The acquisition by Spanish resident enterprises or professionals of commercial cloud compute, GPU hosting, and foundation-model inference APIs provided by non-resident entities lacking a physical PE.
2. **Withholding Rate:** A 5% destination-based withholding tax levied on the net invoice value.
3. **The LIS Art. 15 Enforcement Mechanism:** To prevent evasion, the reform amends Article 15 of *Ley 27/2014* (LIS), conditioning the **tax deductibility** of all IT, cloud, and AI software expenses in corporate income tax returns on the verified filing of Form 216/296 withholding certificates. Because enterprise corporate tax liability increases by 25% if deductions are denied, domestic firms enforce 100% compliance on foreign cloud vendors.
4. **Revenue Yield:** Generates **€24.0 billion annually** (1.6% of GDP) with zero reliance on international treaty renegotiation.

---

## 4. Factor-Neutral Operating Surplus Contributions & Constitutional Boundaries

Under rapid labor substitution, corporate profits and gross operating surpluses (*Excedente Bruto de Explotación*, EBE) expand dramatically at the expense of wages [@acemoglu-2024-macro-ai; @korinek-suh-2024]. Financing UBR requires tapping this expanding surplus.

### A. The IRAP-Style Factor-Neutral Tax Base
Modeled on the Italian regional production tax validated by the Court of Justice of the European Union in Case C-475/03 (*Banca Popolare di Cremona* [@cjeu-c-475-03-banca-popolare-irap]), Spain introduces a factor-neutral contribution on net corporate operating surplus:

$$B_{\text{surplus}} = \text{Value Added} - \text{Personnel Costs} - \text{Depreciation} = \text{EBE} - \delta K$$

By levying a moderate 2.5–3.5% rate directly on net operating margins rather than turnover or transaction invoices, the tax does not constitute an indirect turnover excise and fully complies with Article 401 of the EU VAT Directive (Directive 2006/112/EC [@eu-dir-2006-112-vat]).

### B. Constitutional Non-Confiscatoriness Boundary (Art. 31.3 CE)
In landmark judgment **STC 182/2021** [@stc-182-2021-plusvalia], the Spanish Constitutional Court ruled that taxation violates the principle of economic capacity and non-confiscatoriness when it absorbs the entirety of real income or exceeds manifested wealth. The UBR financing architecture establishes a statutory firewall: aggregate effective taxation across corporate income tax, IECA, and surplus contributions is legally capped at **60% of verified net operating profit**, guaranteeing that capital retains healthy investment margins and preventing capital flight.

---

## 5. The Sovereign AI Dividend Fund (*Fondo Soberano de Transición Algorítmica*, FSTA)

To decouple long-term welfare financing from volatile annual tax cycles, Article 20 of the *Anteproyecto de Ley* establishes the **Fondo Soberano de Transición Algorítmica (FSTA)** under the authority of Article 128.2 CE [@boe-ce-1978]:

```mermaid
flowchart LR
    Windfall["Counter-Cyclical Windfall Inflows<br/>(Triggered when Sector EBE > 120% baseline)"]
    BdE["Independent Governance<br/>(Supervised by Banco de España)"]
    Portfolio["ASG Diversified Global Portfolio<br/>(Public compute, green assets, index equities)"]
    Shield["Anti-Raiding Shield<br/>(3/5ths Congressional Supermajority)"]
    Dividend["Annual Stabilizing Dividend<br/>(0.5% - 0.8% of GDP into UBR Fund)"]

    Windfall --> BdE
    BdE --> Portfolio
    Portfolio --> Shield
    Portfolio --> Dividend
```

### 15-Year Actuarial Accumulation Trajectory (Scenario S2)

| Year | Annual Windfall Inflow (EUR B) | Net Real Return (4.2%) | Capital Endowment (EUR B) | Endowment Share of GDP (%) | Annual Dividend Yield (EUR B) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Year 1** | €12.50B | €0.53B | €13.03B | 0.87% | €0.00B |
| **Year 3** | €15.20B | €1.85B | €45.92B | 3.06% | €1.38B |
| **Year 5** | €18.40B | €3.62B | €89.84B | 5.99% | €2.69B |
| **Year 10** | €21.00B | €7.24B | €179.62B | 11.97% | €5.39B |
| **Year 15** | €16.50B | €10.21B | **€243.08B** | **16.21%** | **€7.29B** |

### Anti-Raiding Governance & EU Rule Neutrality
- **The Windfall Rule:** Inflows are triggered only when corporate EBE exceeds 120% of its historical 3-year moving average. This ensures that fund accumulation does not worsen primary deficits during economic contractions, conforming strictly to EU Net Primary Expenditure limits [@regulation-eu-2024-1263-net-expenditure].
- **Democratic Supermajority:** Modeled on *Ley 28/2003* of the Social Security Reserve Fund [@boe-ley-28-2003-fondo-reserva], capital withdrawals require a **three-fifths (3/5) supermajority in the Congress of the Deputies**, permanently insulating the endowment from short-term electoral raiding.
