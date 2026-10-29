---
id: M12
title: Administrative delivery, digital infrastructure, and take-up
status: draft
locked: false
depends_on: [M03, M06, M07, M10]
covers: [F13]
feeds_chapters: [6]
last_iteration: 0
---
# M12 · Administrative delivery, digital infrastructure, and take-up

## 1. Why this matters
The flagship lesson from Spain's *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]) is that statutory generosity fails when administrative delivery relies on ex-ante means testing, complex household cohabitation verification, and prior-year tax declarations: according to AIReF, over 55% of eligible households in deep poverty never receive IMV, while thousands of vulnerable families suffer sudden retrospective debt clawbacks (*cobros indebidos*). UBR's primary operational advantage is near-100% automatic delivery through joint AEAT–Seguridad Social infrastructure.

## 2. Research questions
- **RQ-M12-01**: How can Spain's *Agencia Estatal de Administración Tributaria* (AEAT), *Instituto Nacional de la Seguridad Social* (INSS), and INE *Padrón Continuo* execute monthly individual UBR disbursement and real-time IRPF withholding clearing with >98% take-up and zero retrospective debt traps?
  - *Hypothesis:* Operating a **Unified Monthly Tax-Transfer Clearing Account** (*Cuenta Única Tributaria-Social*) linked to DNI/NIE—where every resident receives the monthly UBR transfer (or nets it directly against monthly IRPF payroll withholding *retenciones a cuenta* for formal salaried workers) without application forms—raises take-up above 98% and reduces administrative overhead per beneficiary by >75% relative to IMV.
- **RQ-M12-02**: What outreach, banking-inclusion, and legal-guardianship protocols are required to reach the remaining 2% of residents (unbanked individuals, homeless persons, rural elderly without digital certificates, victims of domestic violence, and institutionalized minors)?
  - *Hypothesis:* Combining automatic *de oficio* enrollment via municipal social services and Correos prepaid basic payment accounts (*cuentas de pago básicas*) closes >80% of the residual exclusion gap without requiring digital literacy.

## 3. State of knowledge
Empirical public administration research demonstrates that application burdens, stigma, recertification requirements, and fear of retrospective overpayments are the primary drivers of welfare non-take-up [@hoynes-rothstein-2019; @arcelus-bade-2015-rgi]. In contrast, universal child benefits and automatic tax credits achieve 96–99% coverage [@van-parijs-vanderborght-2017]. Experimental evidence from B-MINCOME [@todeschini-bmincome-2020] and Finland [@kangas-2021-finland] shows that predictable, unconditional monthly disbursement on a fixed calendar day eliminates cognitive scarcity and short-term predatory borrowing.

## 4. Spain context & data sources
- **Existing Spanish Digital Spine:** AEAT (*Renta Web*, monthly SII and Form 111/190 payroll withholdings, Bizum/SEPA instant disbursement), TGSS/INSS (*Tarjeta Social Digital* integrated registry of all public cash benefits), and INE *Padrón Municipal Continuo*.
- **Legal & Privacy Constraints:** *Ley 58/2003 General Tributaria* Art. 95 (tax data sharing exceptions), *Ley 19/2021* [@boe-imv-2021] data-interoperability provisions, and EU GDPR Art. 6(1)(e) / *Ley Orgánica 3/2018 de Protección de Datos*.

## 5. Methods & identification
1. **Systems & Cash-Flow Architecture Design:** Specify two operational modes for formal employees: (i) *Gross-Flow Mode* (every resident receives €900 on the 1st of the month via SEPA transfer; employer withholds full IRPF rate $t$ on gross salary) vs. (ii) *Net-Withholding Mode* (UBR is credited directly inside the monthly payroll withholding formula, and AEAT transfers the net balance directly only when monthly withholding $< \text{UBR}$). Compare liquidity, visibility, and intra-household autonomy (`M14`).
2. **Administrative Cost-Savings Audit:** Benchmark INSS/AEAT FTE personnel and IT costs under UBR against current IMV + regional minimum income administrative overhead.

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Test automated SEPA + Correos basic-account disbursement and measure time-to-first-payment, error rates, and administrative cost per euro transferred.

## 7. Risks, counterarguments & open issues
- **Counterargument (Ghost Residents & Identity Fraud):** Automatic payment tied to *Padrón* registration could incentivize fraudulent registration of non-residents. *Mitigation:* Cross-verify *Padrón* entries against active healthcare card (*Tarjeta Sanitaria*), tax, school, or Social Security activity trails (`M13`) and periodic survival/presence checks (*fe de vida* for inactive records).

## 8. Deliverables & effort
- AEAT–INSS–Padrón Interoperability & Monthly Clearing Technical Specification.
- Last-Mile Inclusion Protocol (Unbanked, Homeless, Domestic Violence Survivors) for Chapter 6. (Effort: 4 person-weeks).
