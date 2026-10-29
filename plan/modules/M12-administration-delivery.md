---
id: M12
title: Administrative delivery, digital infrastructure, and take-up
status: locked
locked: true
depends_on: [M03, M06, M07, M10]
covers: [F13]
feeds_chapters: [6]
last_iteration: 3
---
# M12 · Administrative delivery, digital infrastructure, and take-up

## 1. Why this matters
The flagship empirical lesson from Spain's *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]) is that statutory benefit generosity fails in practice when administrative delivery relies on ex-ante means testing, onerous household cohabitation verification, and prior-year tax returns: according to official AIReF evaluations [@airef-opinion-imv-2023; @airef-opinion-imv-2024], 56% of eligible households in severe poverty never receive IMV (70% non-take-up for CAPI), while thousands of impoverished families suffer devastating retrospective debt recovery notices (*cobros indebidos*). UBR's paramount operational advantage is near-universal (>98%) automatic delivery executed through coordinated AEAT, Social Security, and municipal infrastructure.

## 2. Research questions
- **RQ-M12-01**: How can Spain's *Agencia Estatal de Administración Tributaria* (AEAT), *Instituto Nacional de la Seguridad Social* (INSS), and INE *Padrón Continuo* execute monthly individual UBR disbursement and real-time IRPF withholding clearing with >98% take-up and zero retrospective debt traps?
  - *Hypothesis:* Operating a **Unified Monthly Tax-Transfer Clearing Account** (*Cuenta Única Tributaria-Social*) linked to DNI/NIE—where every adult resident receives the baseline UBR cash transfer via automated SEPA credit on the 1st of each month (or credits it against monthly IRPF payroll withholdings *retenciones a cuenta*) without application forms—raises take-up above 98% and reduces operational overhead per recipient by >70% relative to IMV.
- **RQ-M12-02**: How can monthly payroll clearing protect employee privacy against employer snooping into household composition, disability, or vulnerability status under GDPR Art. 9 and *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018])?
  - *Hypothesis:* Restricting employer payroll clearing exclusively to the uniform individual adult UBR credit via an algorithmic, privacy-preserving **Numerical Tax Code** (*Código de Retención Sintético*)—while routing all child supplements (`M02`) and disability top-ups (`M07`) directly through AEAT/INSS bank disbursements—completely shields sensitive personal and family data from employer human resources departments.
- **RQ-M12-03**: What statutory shields against debt attachment (*inembargabilidad*) and last-mile payment rails (bypassing municipal *Padrón* barriers and commercial bank AML account freezes) guarantee continuous access to the *mínimo existencial*?
  - *Hypothesis:* Classifying UBR as strictly *inembargable* under Art. 607 of *Ley 1/2000* (LEC [@ley-1-2000-lec]) and Art. 44 TRLGSS [@boe-trlgss-2015]—with an explicit statutory carve-out for court-ordered child support and alimony (*pensiones alimenticias*) under Art. 608 LEC [@ley-1-2000-lec]—coupled with absolute immunity from commercial bank overdraft set-offs and internal public debt compensation (Art. 53.2 TRLGSS [@boe-trlgss-2015]; Arts. 71–73 LGT [@boe-lgt-2003]) for retroactive IMV debts, guarantees continuous basic subsistence.

## 3. State of knowledge
Empirical public administration literature shows that bureaucratic application hurdles, stigma, frequent recertification audits, and fear of sudden retrospective debt clawbacks are the primary drivers of welfare non-take-up [@hoynes-rothstein-2019; @airef-opinion-imv-2023]. Conversely, universal child benefits and automated refundable tax credits routinely achieve 96–99% coverage [@van-parijs-vanderborght-2017]. Evidence from Barcelona's B-MINCOME [@todeschini-bmincome-2020] and Finland's trial [@kangas-2021-finland] proves that unconditional, predictable monthly payment schedules on a fixed calendar day drastically reduce cognitive load, liquidity distress, and recourse to predatory consumer loans.

## 4. Spain context & data sources
- **Existing Digital Spine:** AEAT digital clearing (*Renta Web*, real-time VAT reporting *SII*, and monthly Form 111/190 payroll withholdings), TGSS/INSS (*Tarjeta Social Digital* integrated registry of all public cash transfers), and INE *Padrón Municipal Continuo*.
- **Administrative Law & Data Protection Statutes:**
  - *Ley 58/2003 General Tributaria* (LGT [@boe-lgt-2003] Arts. 71–73 on tax compensation/set-off; Art. 95 on tax confidential data sharing exceptions).
  - *Ley 1/2000 de Enjuiciamiento Civil* (LEC [@ley-1-2000-lec] Art. 607 on general non-seizability scales; Art. 608 on the special exception for court-ordered maintenance and child support).
  - *Real Decreto Legislativo 8/2015* (TRLGSS [@boe-trlgss-2015] Art. 44 on non-seizability of basic social security benefits; Art. 53.2 on recovery of undue benefits).
  - *Ley 40/2015 de Régimen Jurídico del Sector Público* (LRJSP [@ley-40-2015-lrjsp] Art. 41 on automated administrative action *actuación administrativa automatizada*).
  - *Ley 39/2015 del Procedimiento Administrativo Común* (LPAC [@boe-lpac-2015] Art. 82 on the mandatory prior hearing guarantee *trámite de audiencia*).
  - *Reglamento (UE) 2016/679* (GDPR Art. 9 on special category data; Art. 22 on automated individual decision-making) and Spanish *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018]).
  - *Resolución de 17 de febrero de 2020* (BOE 2 de mayo de 2020) on municipal padrón registration for unhoused residents (*padrón social*).

## 5. Methods & identification
1. **Gross vs. Net Operational Architecture:**
   - *Option A (Universal Gross SEPA Disbursement):* INSS/AEAT executes a direct €900 SEPA bank transfer to every resident adult on the 1st of every month; employers compute standard IRPF withholding rates on gross salaries without adjusting for UBR. This option maximizes intra-household transparency and individual financial autonomy (`M14`).
   - *Option B (Hybrid Payroll Clearing via Numerical Tax Code):* For formal salaried employees, employers apply a single standard withholding adjustment reflecting the adult UBR tax credit, while transferring the remaining balance. Child, disability, and zero-earner benefits are credited directly by AEAT/INSS.
2. **Algorithmic Due Process & Anti-Offset Shield Protocol:**
   - Formalize statutory language forbidding commercial banks from executing automated overdraft offsets (*compensación bancaria*) and barring AEAT and TGSS from executing automatic administrative set-offs (under Art. 53.2 TRLGSS [@boe-trlgss-2015] and Arts. 71–73 LGT [@boe-lgt-2003]) against the UBR account balance for non-fraudulent past IMV overpayments (*cobros indebidos*).
   - Codify the explicit carve-out for judicial child support orders under Art. 608 LEC [@ley-1-2000-lec].
   - Mandate that all automated administrative determinations comply with Art. 41 LRJSP [@ley-40-2015-lrjsp], establishing mandatory human-in-the-loop review and a 30-day prior hearing window under Art. 82 LPAC [@boe-lpac-2015] before any benefit suspension or revision.
3. **Last-Mile Social Inclusion & Public Rail Protocol:**
   - Codify *Empadronamiento Social de Oficio* to bypass municipal Padrón gatekeeping for unhoused and precariously housed residents under the Technical Instructions of 17 February 2020 (BOE 2 May 2020).
   - Establish a public payment delivery rail via *Sociedad Estatal Correos y Telégrafos* (*Correos*) and Banco de España providing basic accounts (*cuentas de pago básicas* under *Real Decreto-ley 19/2018*) with statutory immunity from commercial AML/KYC account freezes (*Ley 10/2010*).

## 6. Pilot implications
- **Municipal:** Pilots at the municipal level (e.g. Barcelona *B-MINCOME* [@todeschini-bmincome-2020]) cannot alter AEAT payroll tax withholding codes (Form 111) or TGSS social security databases; municipal pilots are confined to gross municipal SEPA transfers, useful for testing prepaid debit cards and municipal social work interface, but unable to evaluate automated tax clearing.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional pilots require coordinated data exchange protocols with the central Ministry of Inclusion and AEAT, facing jurisdictional barriers to altering national payroll withholding formulas.
  - In *Régimen Foral* (Basque Country / Navarre), direct-tax data sharing, Form 110/111 payroll withholdings, and regional personal tax registries are administered directly by the *Diputaciones Forales* (Álava, Bizkaia, Gipuzkoa) and the *Hacienda Foral de Navarra* under *Ley 12/2002* and *Ley 28/1990*, not the State AEAT. This provides an ideal real-world laboratory to pilot the Numerical Tax Code and automated monthly tax-benefit clearing under foral tax sovereignty.
- **National:** Full deployment across the whole territory enables real-time synchronization between the AEAT national database, TGSS daily affiliation registers, and the *Padrón Continuo*, eliminating inter-administrative fragmentation and achieving seamless automated clearing.

## 7. Risks, counterarguments & open issues
- **Counterargument (Registration Fraud & Ghost Residents):** Tying automatic disbursements to the municipal *Padrón* could incentivize fictitious registrations. *Mitigation:* Cross-validate *Padrón* active status continuously against the National Health System card registry (*Tarjeta Sanitaria Individual*), school enrollments, and Social Security activity, flagging anomalies for localized in-person verification (`M13`).
- **Counterargument (Digital Divide Exclusion):** Low-income or elderly individuals without digital certificates (*Cl@ve*, *DNI electrónico*) could be marginalized. *Mitigation:* Mandate proactive *de oficio* enrollment by public agencies; no citizen is required to log into an online portal to receive baseline UBR.

## 8. Deliverables & effort
- AEAT–INSS–Padrón Digital Interoperability Blueprint and Numerical Tax Code Specification.
- Statutory Draft for *Inembargabilidad* Shield (with Art. 608 LEC child support carveout) and LRJSP Art. 41 / LPAC Art. 82 Algorithmic Due-Process Protections for Chapter 6. (Effort: 4 person-weeks).
