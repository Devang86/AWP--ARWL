# workprogram_data.py  –  KKC Audit Work Program Data  (Version 2.0)
# Statutory Audit | Mapped to ICAI Standards on Auditing & KKC Audit Manual 2026
# Significantly expanded: detailed actionable procedures, new areas, NFRA focus

AUDIT_AREAS = [
    "Revenue from Operations",
    "Other Income",
    "Employee Benefits Expenses",
    "Other Expenses",
    "Borrowings",
    "Finance Costs",
    "Investments",
    "Significant Judgements & Estimates",
    "Related Party Transactions",
    "Fraud Risk Assessment",
    "Risk Assessment – FSLI",
    "Going Concern",
    "Leases (Ind AS 116)",
    "Fixed Assets & Intangibles",
    "Trade Receivables & Accrued Income",
    "Cash & Bank Balances",
    "Share Capital, Reserves & Equity",
    "Provisions & Other Liabilities",
    "Taxation – Current & Deferred",
    "Contingent Liabilities & Commitments",
    "IT Application & ITGC Testing",
    "SEBI LODR & Statutory Compliance",
    "Audit Completion & Reporting",
    "NFRA Inspection Focus Areas",
]

ASSERTION_MAP = {
    "OCC": "Occurrence",
    "COM": "Completeness",
    "ACC": "Accuracy",
    "COF": "Cut-off",
    "CLA": "Classification",
    "EXI": "Existence",
    "R&O": "Rights & Obligations",
    "VAL": "Valuation & Allocation",
    "P&D": "Presentation & Disclosure",
    "UNB": "Understandability",
}

# ═══════════════════════════════════════════════════════════════════════════════
WORKPROGRAMS = {

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Revenue from Operations": {
    "objective": (
        "To obtain sufficient appropriate audit evidence that Revenue from Operations comprising "
        "(A) Mutual Fund Distribution Income – trail commissions, upfront commissions, transaction "
        "fees and advisory fees earned as an AMFI-registered MF distributor, and (B) Gains from "
        "Sale of Structured Products – realised gains on disposal of Market-Linked Debentures (MLDs), "
        "Non-Convertible Debentures (NCDs), bonds and other structured debt instruments classified as "
        "FVTPL under Ind AS 109 – is recognised in accordance with Ind AS 115 (Revenue from Contracts "
        "with Customers) for distribution income and Ind AS 109 (Financial Instruments) for instrument "
        "gains, is complete, accurately computed, corroborated by independent RTA data reconciliation, "
        "correctly allocated to the audit period, and presented and disclosed appropriately. Revenue is "
        "a presumed fraud risk under SA 240 Para 26 requiring highest professional scepticism."
    ),
    "risk_overview": (
        "IND AS FRAMEWORK: Trail commission is variable consideration under Ind AS 115 Para 50-53 "
        "(AUM-linked). Constraint per Ind AS 115 Para 56-58 applies – recognise only to extent highly "
        "probable no reversal. Upfront commission satisfies PO at point in time (Para 38). "
        "Structured product gains governed by Ind AS 109 Para 5.7.1 – FVTPL gains to P&L; SPPI test "
        "(Para 4.1.3) determines classification. Derecognition per Ind AS 109 Para 3.2.3 requires "
        "contractual rights to expire or transfer qualifying for derecognition.\n\n"
        "STREAM A – MF DISTRIBUTION INCOME (approx 90% of revenue): ARWL AUM grew Rs.59,351 Cr "
        "to Rs.77,103 Cr (30%). Two RTAs: CAMS (services SBI MF, HDFC MF, ICICI Pru, DSP, Mirae, "
        "ABSL, Franklin, PGIM, WhiteOak, Canara Robeco, Tata, Edelweiss) and KFintech (services "
        "Nippon, Axis, Kotak, UTI, Bandhan/IDFC, HSBC, LIC). Key risks: AUM in back-office differs "
        "from RTA; commission rate exceeds AMFI cap; trail on redeemed folios; premature upfront "
        "recognition; AMFI ban on regular plan upfront violated; SIP upfront recognised in full; "
        "management JE manipulation of revenue accounts.\n\n"
        "STREAM B – STRUCTURED PRODUCT GAINS (material; revenue for dealer): MLDs typically FVTPL "
        "(fail SPPI per Ind AS 109 Para 4.1.3 – market-linked return not solely P&I). NCDs may be "
        "FVTPL if trading model. Key risks: gain computed on wrong cost basis; accrued interest "
        "(dirty price component) not separated from capital gain – Ind AS 109 Para B5.4.2 requires "
        "separation; prior period FVTPL MTM gains double-counted at realisation; MLD redemption "
        "value not agreed to issuer term sheet; group entity transactions not at market price."
    ),
    "steps": [
        {
            "no": 1,
            "category": "A1 | Ind AS 115 Revenue Policy Assessment",
            "risk": "Incorrect application of Ind AS 115 five-step model may result in revenue recognised in wrong period or at wrong amount. Variable consideration (AUM-linked trail) must be constrained per Para 56-58.",
            "procedure": (
                "Step 1A – Obtain ARWL Revenue Recognition Policy and apply Ind AS 115 five-step model:\n"
                "  (i) Contract (Para 9): Distribution agreement with AMC – verify written, AMC committed, "
                "payment terms defined, commercial substance exists.\n"
                "  (ii) Performance Obligations (Para 22-30): Trail = continuous service (over time, "
                "Para 35(a) – customer simultaneously receives and consumes benefit). Upfront = investment "
                "execution (point in time, Para 38). Verify no bundling issue.\n"
                "  (iii) Transaction Price (Para 47-72): Trail = variable consideration linked to AUM. "
                "Apply constraint test (Para 56-58): is it highly probable that reversal will NOT occur? "
                "Document basis for constraint conclusion.\n"
                "  (iv) Allocation (Para 73-86): If AMC pays combined trail + upfront, verify ARWL allocates "
                "on relative standalone selling price basis.\n"
                "  (v) Recognition (Para 31-38): Trail recognised proportionate to service rendered (monthly/ "
                "quarterly). Upfront only on investment execution date.\n\n"
                "Step 1B – Obtain AMFI registration certificate and verify ARN is active and in good standing.\n\n"
                "Step 1C – Obtain AMFI website commission disclosure for ARWL ARN. Compare total disclosed "
                "commission with total commission income per books. Material discrepancy = red flag.\n\n"
                "Step 1D – Verify SEBI/AMFI upfront ban compliance: since October 2018, upfront commissions "
                "on regular plan MF schemes are prohibited. Only trail permissible on regular plans. "
                "Upfront only on direct plans, NPS, or other SEBI-permitted products. Document compliance."
            ),
            "assertions": ["OCC", "ACC", "CLA"],
            "sa_ref": "SA 315 Para 11, 12 | SA 240 Para 26 | Ind AS 115 Para 9, 22, 35, 38, 47, 56-58",
            "kkc_ref": "KKC Manual S.8, S.17",
        },
        {
            "no": 2,
            "category": "A2 | RTA Universe Mapping & AMC Empanelment Completeness",
            "risk": "Incomplete AMC empanelment list means certain commission streams are excluded from RTA reconciliation, leading to undetected revenue overstatement or understatement.",
            "procedure": (
                "Step 2A – Obtain ARWL complete AMC empanelment list. Verify against AMFI website distributor "
                "database for ARWL ARN. Each empanelled AMC must have a corresponding revenue ledger sub-account.\n\n"
                "Step 2B – Map ALL AMCs to their RTA:\n"
                "  CAMS-serviced: SBI MF, HDFC MF, ICICI Prudential, DSP, Mirae, ABSL, Franklin, PGIM, "
                "WhiteOak, Canara Robeco, Invesco, Tata, Edelweiss, Navi, ITI.\n"
                "  KFintech-serviced: Nippon India, Axis, Kotak, UTI, Bandhan (ex-IDFC), HSBC, LIC, "
                "Mahindra Manulife, Quantum.\n"
                "  Other registrars (Sundaram, Motilal Oswal): identify separately.\n\n"
                "Step 2C – For each RTA (CAMS and KFintech), obtain the official Distributor Commission "
                "Statement for full FY 2025-26 showing: ARN, AMC, scheme, plan, AUM, bps rate, computed "
                "commission, TDS deducted, net payment, credit note reference, payment UTR.\n\n"
                "Step 2D – Verify ARWL back-office covers ALL empanelled AMCs – not just material ones. "
                "Missing AMCs = completeness risk. Document the full AMC-RTA mapping in workpaper."
            ),
            "assertions": ["COM", "OCC", "R&O"],
            "sa_ref": "SA 315 Para 11 | SA 500 Para 7, 8 | SA 505 Para 7",
            "kkc_ref": "KKC Manual S.8, S.27",
        },
        {
            "no": 3,
            "category": "A3 | CAMS RTA Statement vs Books – Three-Level Reconciliation",
            "risk": "Trail commission in books may differ from CAMS-computed amounts. This is the single most critical test for completeness and accuracy of the majority of ARWL revenue.",
            "procedure": (
                "Step 3A – Obtain CAMS Distributor Commission Statement for FY 2025-26 (Excel/CSV format) "
                "directly from CAMS portal or authenticated ARWL download. Statement must show:\n"
                "  AMC | Scheme | Plan | Month | Average AUM | Trail bps | Commission = AUM × bps/10000 × days/365 "
                "| TDS @ 10% u/s 194H | Net amount | Credit note no. | Payment date | RTGS UTR.\n\n"
                "Step 3B – AMC-level reconciliation:\n"
                "  (i) Aggregate CAMS-computed commission by AMC for April 2025 – March 2026.\n"
                "  (ii) Agree to ARWL revenue ledger for same AMCs.\n"
                "  (iii) Document differences > Rs.1 lakh per AMC per quarter.\n\n"
                "Step 3C – Scheme-level recomputation (top 10 schemes by trail income):\n"
                "  From CAMS: extract Scheme, Month, AUM, Rate (bps), CAMS commission.\n"
                "  Auditor recompute: Commission = AUM × (bps ÷ 10,000) × (Days in month ÷ 365).\n"
                "  Three-column check: Auditor compute vs CAMS statement vs ARWL books.\n"
                "  Document variance at each comparison stage separately.\n\n"
                "Step 3D – Bank credit trace for selected AMCs:\n"
                "  Agree CAMS net commission to ARWL bank credit advice (RTGS receipt).\n"
                "  Verify TDS per CAMS = TDS in Form 26AS for that AMC deductor.\n\n"
                "Step 3E – Commission rate verification (top 5 schemes):\n"
                "  Agree bps rate in CAMS to AMC distribution agreement.\n"
                "  Verify rate does not exceed AMFI maximum (equity: up to 100 bps; debt: up to 50 bps; "
                "liquid: lower as per AMFI circular). Document AMFI cap compliance."
            ),
            "assertions": ["OCC", "ACC", "COM", "R&O"],
            "sa_ref": "SA 500 Para 7, 8 | SA 505 Para 7, 8, 9 | SA 330 Para 18, 20",
            "kkc_ref": "KKC Manual S.22, S.27, S.44",
        },
        {
            "no": 4,
            "category": "A4 | KFintech RTA Statement vs Books – Parallel Reconciliation",
            "risk": "KFintech services a separate set of AMCs. Independent reconciliation of KFintech data is mandatory – not optional despite CAMS being the larger RTA.",
            "procedure": (
                "Step 4A – Obtain KFintech Distributor Commission Statement for FY 2025-26 with same fields as "
                "CAMS statement. Verify document authenticity.\n\n"
                "Step 4B – AMC-level reconciliation for all KFintech-serviced AMCs:\n"
                "  Aggregate by AMC | Compare to ARWL books | Document differences.\n\n"
                "Step 4C – Scheme-level recomputation for top 8 KFintech-serviced schemes:\n"
                "  Same recomputation as Step 3C. Document three-column comparison.\n\n"
                "Step 4D – Bank credit trace for Nippon MF, Axis MF, Kotak MF, UTI MF.\n\n"
                "Step 4E – MASTER THREE-WAY RECONCILIATION (primary audit evidence):\n"
                "  CAMS total trail + KFintech total trail + Other RTAs = Total per RTA statements\n"
                "  vs. Total trail per ARWL books (revenue ledger)\n"
                "  vs. Total trail per ARWL P&L Note on Revenue from Operations.\n"
                "  All three must agree. Unexplained residual = material risk. "
                "This three-way document is the most important revenue working paper and must be filed."
            ),
            "assertions": ["OCC", "ACC", "COM"],
            "sa_ref": "SA 500 Para 7, 8 | SA 505 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.22, S.27",
        },
        {
            "no": 5,
            "category": "A5 | AUM Data Integrity – RTA vs Back-Office vs AMFI Published Data",
            "risk": "Trail commission is computed on AUM per Ind AS 115 Para 50 (variable consideration). If ARWL back-office AUM differs from the authoritative RTA data, the commission computation base is incorrect.",
            "procedure": (
                "Step 5A – Obtain ARWL monthly AUM register from back-office for all 12 months.\n\n"
                "Step 5B – AUM cross-verification at AMC level for 3 selected months (April 2025, "
                "October 2025, March 2026):\n"
                "  (i) Extract AMC-wise AUM from RTA commission statement for those months.\n"
                "  (ii) Compare with ARWL back-office AUM for same months.\n"
                "  (iii) Differences indicate data feed errors or manual overrides.\n\n"
                "Step 5C – AMFI published data cross-check:\n"
                "  AMFI publishes monthly distributor-wise AUM at amfiindia.com.\n"
                "  Obtain AMFI published AUM for ARWL ARN for April 2025, September 2025, March 2026.\n"
                "  ARWL states AUM of Rs.77,103 Cr at FY25 end – agree to AMFI published figure.\n"
                "  Discrepancy between ARWL-stated AUM and AMFI published = significant red flag.\n\n"
                "Step 5D – Folio-level verification (15 largest folios by AUM):\n"
                "  From ARWL back-office: AUM per folio at 31 March 2026.\n"
                "  From CAMS/KFintech CAS (Consolidated Account Statement): Units × NAV = AUM.\n"
                "  Agree both. Any folio in ARWL books not in CAS = fictitious folio risk.\n\n"
                "Step 5E – Redemption exit test:\n"
                "  Identify folios that fully redeemed in FY 2025-26 (from RTA redemption data).\n"
                "  Verify trail stops in ARWL books from redemption month.\n"
                "  Trail on redeemed folios = misstatement under Ind AS 115 Para 56 (constraint violated)."
            ),
            "assertions": ["OCC", "ACC", "VAL"],
            "sa_ref": "SA 500 Para 7 | SA 520 Para 5, 6 | SA 315 Para 21 | Ind AS 115 Para 50, 56",
            "kkc_ref": "KKC Manual S.12, S.22, S.27",
        },
        {
            "no": 6,
            "category": "A6 | Upfront Commission – Transaction-Level Testing & Regulatory Compliance",
            "risk": "Upfront commissions may violate AMFI ban on regular plan upfronts (since October 2018), be recognised before investment execution (PO not yet satisfied per Ind AS 115 Para 38), or be subject to unrecorded clawback obligations.",
            "procedure": (
                "Step 6A – Obtain upfront commission register for FY 2025-26: client folio, AMC, scheme, "
                "plan type (regular/direct), investment date, amount, commission rate, commission amount, "
                "AMC credit note no., receipt date.\n\n"
                "Step 6B – MUS sample covering 60% of upfront commission value. Mandatory inclusion of:\n"
                "  (i) All transactions in last 15 days of each quarter (cut-off risk).\n"
                "  (ii) Top 20 transactions by value.\n"
                "  (iii) All transactions where rate exceeds AMFI maximum.\n"
                "  (iv) Transactions with related-party AMCs.\n\n"
                "Step 6C – For each selected transaction:\n"
                "  (i) AMC credit note confirming investment executed and commission payable.\n"
                "  (ii) Investment date from CAMS/KFintech = revenue recognition date (Ind AS 115 Para 38).\n"
                "  (iii) Plan type: If regular plan – upfront PROHIBITED per AMFI circular (Oct 2018). "
                "Document and report any regular plan upfront as non-compliance.\n"
                "  (iv) Direct plan upfront: agree rate to AMC agreement; verify within permissible cap.\n\n"
                "Step 6D – SIP commission per Ind AS 115:\n"
                "  If SIP PO satisfied per instalment (continuous service model), recognise trail per "
                "instalment. Verify no full SIP commitment upfront recognised on registration date.\n\n"
                "Step 6E – Clawback verification:\n"
                "  Obtain list of investments redeemed within 12 months of purchase from CAMS/KFintech.\n"
                "  For applicable AMC clawback provisions: verify ARWL reversed commission proportionately.\n"
                "  Cross-check reversals against AMC debit notes (clawback documentation)."
            ),
            "assertions": ["OCC", "ACC", "COF", "R&O"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18, 20 | SA 240 Para 32 | Ind AS 115 Para 35, 38, 56",
            "kkc_ref": "KKC Manual S.22, S.27",
        },
        {
            "no": 7,
            "category": "A7 | Cut-Off Testing – Trail and Upfront Commission",
            "risk": "Trail commission for April 2026 may be pulled into March 2026 (premature recognition violating Ind AS 115 Para 31 – over time recognition principle), or genuine March 2026 accruals omitted.",
            "procedure": (
                "Step 7A – Trail cut-off:\n"
                "  Obtain CAMS and KFintech statements for March 2026 AND April 2026 separately.\n"
                "  Verify March trail computed on March AUM (not April AUM) per Ind AS 115 Para 47.\n"
                "  Verify April AUM not used for March computation.\n"
                "  If AMC pays in arrears (April credit for March trail): verify accrual in March books "
                "= April receipt per bank. Accrued income reconciliation per Ind AS 115 Para 116.\n\n"
                "Step 7B – Year-end accrual verification (Ind AS 115 contract asset):\n"
                "  Accrued trail at 31 March 2026 (contract asset) = Expected March commission per RTA.\n"
                "  Trace: AMC-wise accrual in books → Actual receipt in April/May 2026 bank statement.\n"
                "  Document reconciliation for each material AMC.\n\n"
                "Step 7C – Upfront cut-off:\n"
                "  All upfront entries in period 20 March 2026 to 10 April 2026: verify investment date.\n"
                "  April 2026 investment date in books as March 2026 revenue = overstatement.\n"
                "  March 2026 investment + April AMC credit note: verify investment was actually executed "
                "in March (check CAMS/KFintech transaction record).\n\n"
                "Step 7D – Post-closure entries: obtain all JEs to revenue after trial balance date. "
                "Investigate all – high risk for period manipulation."
            ),
            "assertions": ["COF", "OCC", "ACC"],
            "sa_ref": "SA 330 Para 20 | SA 500 Para 7 | SA 560 Para 6 | Ind AS 115 Para 31, 47, 116",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 8,
            "category": "A8 | Form 26AS / AIS – TDS Cross-Check on Commission Income",
            "risk": "TDS deducted by AMCs on commission (Sec 194H, 10%) is an independent government-verified cross-check. Discrepancy between TDS per 26AS and TDS implied by booked income indicates unrecorded or fictitious revenue.",
            "procedure": (
                "Step 8A – Obtain Form 26AS and Annual Information Statement (AIS) from Income Tax portal for "
                "ARWL for FY 2025-26. AIS shows TDS deducted by all AMCs on commission under Sec 194H.\n\n"
                "Step 8B – TDS cross-check reconciliation:\n"
                "  Total TDS per Form 26AS (all AMC deductors) × 10 = Implied gross commission.\n"
                "  vs. Gross commission per ARWL books (revenue ledger, before TDS netting).\n"
                "  These should broadly agree (within last-quarter TDS timing difference).\n\n"
                "Step 8C – Investigate material differences:\n"
                "  TDS credit in 26AS without corresponding revenue in books = UNRECORDED INCOME.\n"
                "  Revenue in books without 26AS TDS credit = POTENTIALLY FICTITIOUS revenue.\n"
                "  Document each difference with management explanation and corroborating evidence.\n\n"
                "Step 8D – TDS receivable balance:\n"
                "  TDS receivable in balance sheet = TDS per 26AS minus advance tax offset.\n"
                "  Reconcile computed TDS receivable to balance sheet figure."
            ),
            "assertions": ["COM", "ACC", "OCC"],
            "sa_ref": "SA 500 Para 7 | SA 520 Para 5 | SA 505 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 9,
            "category": "A9 | Journal Entry Testing on Revenue Accounts (SA 240 Para 32 – Mandatory)",
            "risk": "SA 240 Para 32(a) requires mandatory JE testing on revenue accounts for ALL audits. This is a NFRA critical requirement. Absence of this test or inadequate documentation of results is a reportable deficiency.",
            "procedure": (
                "Step 9A – Extract complete JE population for all revenue accounts for FY 2025-26 "
                "DIRECTLY from accounting system (Tally/ERP/SAP). Do NOT use management summaries. "
                "Verify completeness: total credits per JE = revenue per trial balance.\n\n"
                "Step 9B – Apply CAATs filters:\n"
                "  Filter 1: Posted by CFO, CEO, MD user IDs (above normal posting level).\n"
                "  Filter 2: Posted before 8 AM, after 8 PM, on weekends, on public holidays.\n"
                "  Filter 3: Round-number amounts (Rs.1 Cr, Rs.50 L, Rs.10 L exact).\n"
                "  Filter 4: Blank narration or vague text (misc / adjustment / to be verified).\n"
                "  Filter 5: Revenue credit with debit to intercompany / suspense / capital accounts.\n"
                "  Filter 6: Entries posted after trial balance date but before financial statements signed.\n"
                "  Filter 7: Revenue credits with debit to receivables but no RTA/AMC credit note.\n\n"
                "Step 9C – Investigate ALL flagged items: obtain source document (AMC credit note, RTA "
                "statement, bank advice), authorisation, and business rationale. JEs not supported by "
                "third-party document = misstatement risk. Escalate to EP.\n\n"
                "Step 9D – Reversal test: query revenue credits in FY 2025-26 reversed (debited) in "
                "April/May 2026. Reversals = premature recognition in March 2026."
            ),
            "assertions": ["OCC", "ACC", "COM"],
            "sa_ref": "SA 240 Para 32(a) | SA 315 Para 22 | SA 330 Para 16",
            "kkc_ref": "KKC Manual S.14, S.25",
        },
        {
            "no": 10,
            "category": "B1 | Structured Products – Ind AS 109 Classification & SPPI Assessment",
            "risk": "Incorrect Ind AS 109 classification of structured products drives wrong measurement basis and P&L/OCI treatment. MLDs typically fail SPPI test (Para 4.1.3) as market-linked returns are NOT solely payments of P&I.",
            "procedure": (
                "Step 10A – Obtain Structured Products Investment Register for FY 2025-26: Instrument type "
                "(MLD/NCD/Bond/Structured Note), Issuer, ISIN, Face value, Acquisition cost, Acquisition date, "
                "Ind AS 109 classification, Opening balance 01 Apr 2025, Additions, Disposals, Closing balance "
                "31 Mar 2026, Gain/loss on disposal.\n\n"
                "Step 10B – SPPI Test per Ind AS 109 Para 4.1.3 for each instrument:\n"
                "  MLDs: Payoff linked to Nifty 50/Gold/other index = NOT solely P&I = FAILS SPPI = FVTPL mandatory.\n"
                "  NCDs with fixed coupon and no features: passes SPPI. Check business model (HTC = amortised cost; "
                "trading = FVTPL). Verify management's SPPI documentation exists for each instrument.\n"
                "  Structured notes with derivative features: fails SPPI = FVTPL per Para 4.1.4.\n"
                "  Obtain SPPI assessment documentation for top 10 instruments by value.\n\n"
                "Step 10C – Revenue vs Other Income classification per Ind AS 1 Para 7:\n"
                "  If ARWL's ordinary business includes structured product distribution/dealing, gains = Revenue.\n"
                "  If incidental: Other Income. Verify consistent classification. Document basis.\n"
                "  Prior year: what was the classification? Any change = Ind AS 8 disclosure required.\n\n"
                "Step 10D – Verify opening FVTPL portfolio values agreed to prior year closing balances."
            ),
            "assertions": ["COM", "CLA", "EXI", "VAL"],
            "sa_ref": "SA 315 Para 11 | SA 500 Para 7 | Ind AS 109 Para 4.1.1-4.1.4, 4.1.3 | Ind AS 1 Para 7",
            "kkc_ref": "KKC Manual S.8, S.27",
        },
        {
            "no": 11,
            "category": "B2 | Structured Products – Existence via Demat & Issuer Confirmation",
            "risk": "Structured products recorded in books may not physically exist, or may have been disposed of without recording, leading to fictitious disposal gains.",
            "procedure": (
                "Step 11A – Demat verification (NSDL/CDSL):\n"
                "  Obtain NSDL/CDSL DP statement for ALL ARWL demat accounts as at 01 April 2025 AND "
                "31 March 2026 (not just one date).\n"
                "  Opening register → Opening demat (01 Apr 2025): every instrument must match.\n"
                "  Purchases in year → Demat credits: agree ISIN, quantity, date.\n"
                "  Disposals in year → Demat debits: agree ISIN, quantity, settlement date.\n"
                "  Closing demat (31 Mar 2026) = Closing per investment register. Any gap = unexplained.\n\n"
                "Step 11B – Unlisted/privately-placed MLDs:\n"
                "  If demat-held: per DP statement above.\n"
                "  If physical: obtain original debenture certificate; verify ARWL's name as holder.\n"
                "  Obtain issuer/arranger confirmation of ARWL's registered holding at relevant dates.\n\n"
                "Step 11C – Exchange-traded bonds:\n"
                "  Obtain broker contract notes for all purchases and sales.\n"
                "  Verify settlement via CCIL (Clearing Corporation of India) for G-Sec or exchange "
                "settlement for other listed bonds.\n\n"
                "Step 11D – FVTPL fair value at 31 March 2026:\n"
                "  Listed: NSE/BSE/Bloomberg closing price on 31 March 2026 per ISIN.\n"
                "  Unlisted: independent valuation report. Assess valuer per SA 620."
            ),
            "assertions": ["EXI", "R&O", "COM", "VAL"],
            "sa_ref": "SA 505 Para 7 | SA 500 Para 7 | SA 501 Para 4 | SA 620 Para 8",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 12,
            "category": "B3 | Gain Computation – Arithmetic Accuracy & Accrued Interest Separation",
            "risk": "Gains may be overstated if accrued interest (included in dirty price settlement) is not separated from capital gain. Per Ind AS 109 Para B5.4.2 and the EIR method, interest accrual and capital gain are distinct. Double-counting prior FVTPL MTM gains at realisation is a specific risk.",
            "procedure": (
                "Step 12A – For EACH disposal during FY 2025-26, obtain trade confirmation/contract note:\n"
                "  Sale proceeds = Settlement amount per trade confirmation (verify from broker).\n"
                "  Carrying value at disposal = FVTPL book value at that date per amortisation schedule.\n"
                "  Gain/(Loss) = Sale proceeds – Carrying value. Agree to P&L amount.\n\n"
                "Step 12B – CRITICAL: Dirty Price vs Clean Price separation (Ind AS 109 B5.4.2):\n"
                "  For ALL NCDs and bonds (interest-bearing instruments):\n"
                "  Settlement price (dirty price) = Clean price + Accrued interest.\n"
                "  Accrued interest = Face Value × Coupon Rate × (Days since last coupon ÷ 365).\n"
                "  Clean price proceeds = Dirty price – Accrued interest.\n"
                "  Capital gain = Clean price proceeds – Carrying value (FVTPL book value).\n"
                "  Accrued interest must be recognised separately as INTEREST INCOME (Other Income) "
                "– NOT as part of gain on sale. Failure = overstatement of gain, understatement of interest.\n"
                "  Verify ARWL correctly bifurcates for each bond/NCD disposal.\n\n"
                "Step 12C – MLD-specific gain computation:\n"
                "  Obtain issuer redemption computation statement and final term sheet.\n"
                "  Redemption value = Face value × Participation rate × Index performance.\n"
                "  Gain = Redemption value – CARRYING VALUE (not original cost if previously MTM'd).\n"
                "  ANTI-DOUBLE COUNT CHECK: If MLD was FVTPL during holding, prior MTM gains already in P&L. "
                "At disposal: Gain = Proceeds – Closing carrying value (already MTM'd). "
                "Verify ARWL does not re-recognise already-booked MTM gains as new realised gains.\n\n"
                "Step 12D – CAAT recomputation: import all disposal records into Excel. "
                "Recompute Gain = Proceeds – Carrying value for 100% of transactions. "
                "Flag differences > Rs.1 lakh. No sampling – full population test."
            ),
            "assertions": ["ACC", "OCC", "VAL", "CLA"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18 | Ind AS 109 Para 3.2.3, 3.2.12, 5.7.1, B5.4.2",
            "kkc_ref": "KKC Manual S.27, S.35",
        },
        {
            "no": 13,
            "category": "B4 | Structured Products – Cut-Off & Settlement Verification",
            "risk": "Per Ind AS 109 Para 3.2.3, derecognition occurs when contractual rights expire or qualifying transfer occurs. Gain recognised before settlement = revenue recognised before derecognition criteria met.",
            "procedure": (
                "Step 13A – Obtain accounting policy: does ARWL recognise on trade date or settlement date?\n"
                "  For exchange-traded: T+1 (G-Sec via RBI SGL), T+2 (exchange-listed bonds).\n"
                "  For OTC: per trade confirmation settlement date.\n"
                "  Verify policy consistent throughout year.\n\n"
                "Step 13B – Year-end cut-off (25 March 2026 to 07 April 2026):\n"
                "  Trades executed on or before 31 March 2026 with settlement in April 2026:\n"
                "  Verify recognition date = trade date or settlement date per stated policy.\n"
                "  Trades settled March 2026 not recognised = understatement.\n"
                "  Trades settled April 2026 recognised March 2026 = overstatement.\n\n"
                "Step 13C – Settlement confirmation for selected transactions:\n"
                "  (i) NSDL/CDSL demat debit confirms security transferred out of ARWL account.\n"
                "  (ii) Bank credit confirms sale proceeds received in ARWL bank.\n"
                "  BOTH required for derecognition under Ind AS 109 Para 3.2.6 (transfer of risks and rewards).\n"
                "  Transaction where security transferred but cash not received = incomplete = do not recognise gain."
            ),
            "assertions": ["COF", "OCC", "R&O"],
            "sa_ref": "SA 330 Para 20 | SA 500 Para 7 | SA 560 Para 6 | Ind AS 109 Para 3.2.3, 3.2.6",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 14,
            "category": "B5 | Structured Products – Related Party & Arm's Length (Ind AS 24 & SA 550)",
            "risk": "Structured product transactions with Anand Rathi group entities (AR Securities, AR Share Brokers) may not be at market price, enabling artificial gain or loss manipulation, violating Ind AS 24 and SA 550.",
            "procedure": (
                "Step 14A – Identify all structured product transactions where counterparty is:\n"
                "  (i) Anand Rathi group entity (AR Securities Ltd, AR Share & Stock Brokers, AR Capital Markets).\n"
                "  (ii) Fund/scheme managed by group entity.\n"
                "  (iii) Company where ARWL promoters/KMPs have directorship.\n\n"
                "Step 14B – For each identified RPT structured product trade:\n"
                "  Listed instruments: compare transaction price to NSE/BSE Bloomberg mid-price on trade date.\n"
                "  Unlisted/OTC: obtain independent broker quote or Bloomberg/Reuters indicative price.\n"
                "  Discount on sale to related party = possible benefit transfer = Ind AS 24 disclosure.\n"
                "  Premium on purchase from related party = overpayment benefiting related party.\n\n"
                "Step 14C – SEBI LODR Regulation 23 audit committee approval:\n"
                "  Verify AC approved material RPT structured product trades. Attach AC minutes.\n"
                "  Check ARWL RPT note includes these transactions.\n"
                "  Per SA 550 Para 16: test for arm's length and document conclusion."
            ),
            "assertions": ["OCC", "VAL", "R&O", "P&D"],
            "sa_ref": "SA 550 Para 16, 17 | SA 500 Para 7 | Ind AS 24 Para 18, 19 | SEBI LODR Reg. 23",
            "kkc_ref": "KKC Manual S.15, S.35",
        },
        {
            "no": 15,
            "category": "B6 & Final | Revenue Disclosure & Master Reconciliation Conclusion",
            "risk": "Revenue disclosures may not meet Ind AS 115 Para 110-129 (disaggregation, contract balances, significant judgements) and Ind AS 107 Para 40 (sensitivity analysis on FVTPL instruments).",
            "procedure": (
                "Step 15A – Ind AS 115 disclosures review:\n"
                "  (i) Disaggregation (Para 114-115): trail by category (equity/debt/hybrid/liquid), upfront, "
                "transaction fees disclosed separately.\n"
                "  (ii) Contract balances (Para 116): accrued income (contract asset) and advance received "
                "(contract liability) with opening/closing movement.\n"
                "  (iii) Significant judgements (Para 122-126): basis for over-time recognition, variable "
                "consideration constraint methodology, clawback provisions, SIP commission basis.\n\n"
                "Step 15B – Ind AS 107 and 109 disclosures for structured products:\n"
                "  Realised gains vs unrealised FVTPL gains (MTM): disclosed separately.\n"
                "  Interest rate sensitivity per Ind AS 107 Para 40: impact of 100bps on FVTPL portfolio.\n"
                "  Maturity profile of structured product holdings.\n\n"
                "Step 15C – Quarterly consistency (SEBI LODR Reg 33):\n"
                "  Q1 + Q2 + Q3 + Q4 revenue per BSE/NSE quarterly filings = Annual audited revenue.\n"
                "  Differences require investigation.\n\n"
                "Step 15D – MASTER REVENUE RECONCILIATION (Final Audit Conclusion Document):\n"
                "  Trail Commission per CAMS (Step 3)\n"
                "+ Trail Commission per KFintech (Step 4)\n"
                "+ Upfront Commission per AMC credit notes (Step 6)\n"
                "+ Structured Product Gains per trade confirmations + demat (Steps 11-13)\n"
                "+ Advisory/Other fees (separately tested)\n"
                "= Total Revenue per independently corroborated sources\n"
                "vs. Revenue per Audited P&L\n"
                "DIFFERENCE = Must be zero or documented with explanation.\n"
                "This document is the primary audit conclusion for revenue and must be partner-reviewed."
            ),
            "assertions": ["P&D", "ACC", "COM", "OCC"],
            "sa_ref": "SA 520 Para 5, 7 | SA 700 Para 13 | Ind AS 115 Para 110-129 | Ind AS 107 Para 40",
            "kkc_ref": "KKC Manual S.12, S.46, S.48",
        },
    ],
},


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Other Income": {
    "objective": (
        "To verify that all Other Income is completely and accurately recorded, relates to the entity, "
        "is in the correct period, is appropriately classified between revenue from operations and other income, "
        "and is disclosed per Ind AS 1 and applicable accounting standards."
    ),
    "risk_overview": (
        "ARWL's other income includes: interest on FDs and liquid funds (treasury operations), dividend income, "
        "profit/loss on sale of investments, gain on FVTPL investments, exchange gain/loss, and miscellaneous receipts. "
        "ARWL contributed ₹234 Cr in direct taxes (FY25) – indicating significant taxable income; other income components "
        "must be correctly characterised for tax purposes too. Risks: incorrect classification between revenue and other income, "
        "income not accrued on time, incorrect Ind AS 109 treatment of investment income."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Completeness & Classification Assessment",
            "risk": "Other income items may be incompletely captured or incorrectly classified as revenue from operations, distorting operating performance metrics.",
            "procedure": (
                "Step 1A – Obtain a detailed schedule of all items included in 'Other Income' for FY 2025-26 with month-wise breakup.\n\n"
                "Step 1B – For each line item, assess whether it constitutes 'other income' or should be reclassified as 'revenue from operations'. "
                "The principle: if the income is incidental to the principal business activity it is 'other income'; if integral, it is 'revenue'.\n\n"
                "Step 1C – Verify consistency of classification with prior year. Any reclassification between other income and revenue "
                "must be assessed for compliance with Ind AS 8 (change in accounting policy or estimate) and adequately disclosed.\n\n"
                "Step 1D – Check whether any material income items have been omitted from 'other income' – review debit/credit notes, "
                "bank credit entries, and correspondence for any receipts not routed through P&L."
            ),
            "assertions": ["COM", "CLA", "OCC"],
            "sa_ref": "SA 315 Para 11 | SA 520 Para 5",
            "kkc_ref": "KKC Manual S.8, S.12",
        },
        {
            "no": 2,
            "category": "Interest Income – FDs & Liquid Funds",
            "risk": "Interest income on treasury investments may be understated (not fully accrued) or computed on incorrect principal / rate, particularly where FDs were renewed or prematurely withdrawn during the year.",
            "procedure": (
                "Step 2A – Obtain the complete fixed deposit register showing: Bank, FD number, principal, interest rate (%), "
                "deposit date, maturity date, interest amount, and TDS deducted.\n\n"
                "Step 2B – For all FDs outstanding during FY 2025-26, recompute interest income independently: "
                "Interest = Principal × Rate% × (Days/365). Compare with management's figure. Document differences.\n\n"
                "Step 2C – For FDs matured during the year: verify maturity proceeds received match principal + interest less TDS. "
                "Trace to bank statement. Verify interest correctly accounted even if FD was renewed (gross up renewal).\n\n"
                "Step 2D – For liquid fund investments: obtain NAV statements from CAMS/KFintech for beginning and end of year. "
                "Verify unrealised gain/(loss) = (Closing NAV × Units) – (Opening NAV × Units + Purchases – Redemptions). "
                "Ensure income is classified as FVTPL gain in P&L under Ind AS 109.\n\n"
                "Step 2E – Verify accrued interest receivable in balance sheet as at 31 March 2026 is complete – sum of interest "
                "earned on FDs from last interest credit date to 31 March 2026."
            ),
            "assertions": ["OCC", "ACC", "COF", "COM"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 3,
            "category": "Dividend Income",
            "risk": "Dividend income may be recorded without ownership verification, or in the wrong period.",
            "procedure": (
                "Step 3A – Obtain list of all dividend receipts during FY 2025-26. Trace each to bank statement or broker confirmation.\n\n"
                "Step 3B – For each dividend: verify the company held the underlying investment on the record date "
                "(cross-reference with NSDL/CDSL demat statement or investment register).\n\n"
                "Step 3C – Verify accounting: For FVTPL equity investments – dividend recognised in P&L when right to receive is established "
                "(Ind AS 109 Para 5.7.1A). For FVOCI equity instruments – dividend recognised in P&L unless it clearly represents "
                "a recovery of part of cost.\n\n"
                "Step 3D – Verify TDS / withholding tax on dividends has been correctly accounted. "
                "For domestic dividends: TDS @ 10% u/s 194 if dividend > ₹5,000 – verify Form 26AS reconciliation."
            ),
            "assertions": ["OCC", "R&O", "COF", "ACC"],
            "sa_ref": "SA 500 Para 7 | Ind AS 109 Para 5.7.1A",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 4,
            "category": "Profit / Loss on Sale of Investments",
            "risk": "Gains or losses may be incorrectly computed, or disposals may not represent arm's length transactions.",
            "procedure": (
                "Step 4A – Obtain investment disposal schedule showing: investment type, cost of acquisition, proceeds, "
                "gain/loss, and date of disposal.\n\n"
                "Step 4B – Recompute gain/loss for each material disposal = Sale proceeds – Carrying value (cost or fair value per Ind AS 109).\n\n"
                "Step 4C – For listed securities: verify sale price against NSE/BSE market price on date of sale. "
                "Flag any sale significantly below market price (possible related-party benefit or fictitious sale).\n\n"
                "Step 4D – Verify derecognition accounting: asset removed from books, proceeds received, gain/loss recognised in P&L. "
                "Ensure no asset is still on books after disposal.\n\n"
                "Step 4E – Verify compliance with Ind AS 109 derecognition criteria (transfer of risks and rewards or control)."
            ),
            "assertions": ["OCC", "ACC", "VAL"],
            "sa_ref": "SA 500 Para 7 | Ind AS 109 Para 3.2",
            "kkc_ref": "KKC Manual S.27",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Employee Benefits Expenses": {
    "objective": (
        "To verify that all employee benefit expenses are completely and accurately recorded, are properly authorised, "
        "relate to the period, and comply with Ind AS 19 (Employee Benefits) and applicable statutory requirements "
        "including PF, ESI, Gratuity Act, and tax withholding provisions."
    ),
    "risk_overview": (
        "ARWL's RM count grew to 380 in FY25 with stated regret attrition below 1%. "
        "The company operates a performance-linked pay structure. Key risks: "
        "(a) Ghost employees on payroll, (b) Incorrect accrual of variable/performance-linked pay for RMs, "
        "(c) Actuarial assumptions in defined benefit obligations (gratuity, leave encashment) may be biased, "
        "(d) ESOP expense incorrectly computed, (e) Statutory compliance – PF/ESI/TDS gaps, "
        "(f) Incorrect treatment of termination benefits."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Planning Analytics – Payroll Benchmarking",
            "risk": "Without trend analysis, fictitious employees, unauthorised pay increases, or incorrect expense accruals may remain undetected.",
            "procedure": (
                "Step 1A – Prepare a payroll analytics dashboard: "
                "(i) Total employee cost per month – plot trend for 12 months; identify months with unusual spikes. "
                "(ii) Average cost per employee = Total payroll cost ÷ Average headcount; compare with prior year. "
                "(iii) Fixed payroll (base salary, PF, ESI) vs variable pay (bonus, commissions, ESOP) – compute ratio. "
                "(iv) RM commission per RM = Total RM commissions ÷ Average RM count; compare with prior year.\n\n"
                "Step 1B – Headcount movement analysis: "
                "(i) Opening headcount + Joiners – Leavers = Closing headcount. Agree closing headcount with HR records. "
                "(ii) Verify headcount in each grade/department with HR HRMS system. "
                "(iii) For ARWL: RM headcount of 380 is a stated metric – verify against payroll master.\n\n"
                "Step 1C – Cross-validate: Employee cost / Net inflows (₹12,617 Cr) as a ratio – compare with prior year. "
                "If headcount grew 10% but employee cost grew 25%, investigate the additional cost drivers."
            ),
            "assertions": ["COM", "ACC", "OCC"],
            "sa_ref": "SA 520 Para 5 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.12",
        },
        {
            "no": 2,
            "category": "Payroll Master File Testing & Ghost Employee",
            "risk": "Fictitious employees or employees not entitled to salary may be included in the payroll, leading to misappropriation of company funds.",
            "procedure": (
                "Step 2A – Obtain the payroll master file as at 31 March 2026 from the HRMS system (not from management-prepared spreadsheets). "
                "The master file should include: employee ID, name, PAN, Aadhaar, bank account number, designation, department, "
                "date of joining, base salary, and allowances.\n\n"
                "Step 2B – Apply CAATs / data analytics on the master file: "
                "(i) Duplicate PAN: Flag any two employees sharing the same PAN. "
                "(ii) Duplicate bank account: Flag any two employees with identical bank account numbers. "
                "(iii) Employees without PAN: Flag records with blank/invalid PAN (non-compliance with income tax requirements). "
                "(iv) Employees with zero or negative salary: Investigate anomalies. "
                "(v) Salary amounts ending in rounded figures for large number of employees: unusual pattern.\n\n"
                "Step 2C – Select a stratified sample of minimum 30 employees (or 5% of headcount): "
                "(i) Agree name and employee number to offer letter / appointment letter. "
                "(ii) Agree salary to most recent salary revision letter / increment letter. "
                "(iii) Verify PAN matches Form 16 / 26AS. "
                "(iv) Agree bank account to cancelled cheque / bank mandate in employee file. "
                "(v) Physically verify (or verify via video/ID) existence of 5 employees selected randomly.\n\n"
                "Step 2D – Joiner testing: Select 10 employees who joined during FY 2025-26. "
                "Verify salary only from date of joining; confirm offer letter date matches joining date in HRMS.\n\n"
                "Step 2E – Leaver testing: Select 10 employees who left during FY 2025-26. "
                "Verify salary stopped on leaving date; full and final settlement computed correctly; "
                "no salary paid after leaving date; any notice-period recovery correctly applied."
            ),
            "assertions": ["OCC", "ACC", "COM"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18 | SA 240 Para 32",
            "kkc_ref": "KKC Manual S.22, S.27",
        },
        {
            "no": 3,
            "category": "RM Variable Pay & Performance Commission",
            "risk": "RM commission may be accrued based on incorrect performance data or not linked to the actual commission policy, leading to over/understatement of employee costs.",
            "procedure": (
                "Step 3A – Obtain the RM Commission / Incentive Policy document approved by the Board/HR Committee. "
                "Understand the commission formula: is it based on net inflows? AUM? Client retention? A combination?\n\n"
                "Step 3B – Obtain the net inflows data per RM from the back-office system for FY 2025-26. "
                "This data should be extracted directly from the back-office – not from management-prepared summaries.\n\n"
                "Step 3C – Select top 15 RMs by commission payout: "
                "(i) Independently recompute commission based on policy formula and net inflow data. "
                "(ii) Compare with actual commission paid/accrued in payroll. "
                "(iii) For differences exceeding 5% or ₹1 lakh, obtain documentary explanation.\n\n"
                "Step 3D – Verify the year-end commission accrual: obtain the accrual workings as at 31 March 2026. "
                "Verify that commissions are accrued for the period January to March 2026 based on Q4 performance data. "
                "Agree accrual to subsequent payment in April/May 2026.\n\n"
                "Step 3E – Check for any discretionary bonuses above the policy framework: "
                "verify Board/MD approval for out-of-policy payments."
            ),
            "assertions": ["OCC", "ACC", "COF", "COM"],
            "sa_ref": "SA 500 Para 7 | SA 540 Para 8",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 4,
            "category": "Defined Benefit Obligations – Gratuity & Leave Encashment",
            "risk": "Actuarial assumptions may be biased or inconsistent with market conditions, leading to understatement of defined benefit obligations and employee costs.",
            "procedure": (
                "Step 4A – Obtain the actuarial valuation report as at 31 March 2026. Verify it covers: "
                "(i) Projected Benefit Obligation (PBO) – opening and closing. "
                "(ii) Current service cost, interest cost, actuarial gains/losses, benefits paid. "
                "(iii) Assumptions: discount rate, salary escalation rate, attrition rate, mortality rate, retirement age.\n\n"
                "Step 4B – Assess the appropriateness of key assumptions: "
                "(i) Discount rate: Should be based on yield of Government Securities at the balance sheet date with maturity matching liability duration. "
                "For 31 March 2026, obtain 10-year G-Sec yield (expected ~7.0-7.5%). Compare with actuarial assumption. "
                "(ii) Salary escalation: Verify consistency with actual salary increases in the current year and management's guidance on future increases. "
                "(iii) Attrition rate: ARWL has stated RM attrition below 1% – verify this is reflected in the actuarial model, as very low attrition increases the obligation (employees stay longer and earn higher gratuity). "
                "(iv) Mortality: Verify use of Indian Assured Lives Mortality (IALM) 2006-08 or latest published tables.\n\n"
                "Step 4C – Assess independence and competence of the actuary per SA 620. "
                "Verify the actuary's professional qualifications (Fellow of Institute of Actuaries of India) and independence from the client.\n\n"
                "Step 4D – Recompute and verify: Current Service Cost + Opening PBO + Interest Cost (PBO × discount rate) "
                "– Benefits Paid ± Actuarial Gain/Loss = Closing PBO.\n\n"
                "Step 4E – Verify Ind AS 19 presentation: "
                "(i) Current service cost and interest cost in P&L under employee benefits expense. "
                "(ii) Actuarial gains/losses in Other Comprehensive Income (OCI). "
                "(iii) Past service cost recognised immediately in P&L. "
                "(iv) Verify note disclosure: movement in PBO, plan assets, amount recognised in P&L, OCI, and balance sheet."
            ),
            "assertions": ["VAL", "COM", "P&D", "ACC"],
            "sa_ref": "SA 540 Para 8, 13, 15 | SA 620 Para 8, 9, 12",
            "kkc_ref": "KKC Manual S.35, S.37",
        },
        {
            "no": 5,
            "category": "ESOP Expense (Ind AS 102)",
            "risk": "ESOP expense may be incorrectly computed due to wrong fair value at grant date, incorrect vesting schedule, or improper treatment of forfeitures and modifications.",
            "procedure": (
                "Step 5A – Obtain the ESOP Scheme document(s) and the Board resolution approving the scheme. "
                "Verify scheme is compliant with SEBI (Share Based Employee Benefits and Sweat Equity) Regulations, 2021.\n\n"
                "Step 5B – Obtain the fair value computation at grant date from the management's independent valuer. "
                "Assess the valuation model used (Black-Scholes or binomial lattice). Evaluate reasonableness of inputs: "
                "(i) Spot price on grant date (agree to NSE/BSE), (ii) Exercise price (agree to scheme), "
                "(iii) Risk-free rate (agree to G-Sec rate at grant date), (iv) Expected volatility (verify historical calculation), "
                "(v) Expected dividends (verify with actual dividend history), (vi) Expected option life.\n\n"
                "Step 5C – ESOP expense computation: "
                "(i) For each tranche, compute expense = Fair value at grant × Number of options expected to vest ÷ Vesting period × Proportion of current period. "
                "(ii) Adjust for forfeitures: If options forfeited during year, reverse the expense for those options. "
                "(iii) Cumulative expense = Cumulative FV charge – Expense recognised in prior years = Current year expense.\n\n"
                "Step 5D – Verify the ESOP Reserve movement in Statement of Changes in Equity: "
                "Opening ESOP Reserve + Current year ESOP expense – Options exercised (transferred to Share Capital + Securities Premium) – Forfeitures = Closing ESOP Reserve.\n\n"
                "Step 5E – Verify disclosures per Ind AS 102: "
                "Weighted average fair value, exercise prices, option movements (granted, exercised, forfeited, outstanding), "
                "weighted average remaining contractual life, and valuation model inputs."
            ),
            "assertions": ["ACC", "VAL", "P&D"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 6,
            "category": "Statutory Compliance – PF, ESI, TDS on Salaries",
            "risk": "Non-compliance with statutory obligations may indicate under-accrual or misappropriation, and may expose the company to penalties and interest.",
            "procedure": (
                "Step 6A – PF Compliance: "
                "(i) Obtain ECR (Electronic Challan cum Return) for all 12 months. "
                "(ii) Verify PF wages base is correct per EPF Act – includes basic salary, DA, and certain allowances. "
                "(iii) Recompute employer and employee PF contribution: Employee 12% + Employer 12% (of which 8.33% to EPS, 3.67% to EPF). "
                "(iv) Verify monthly PF challan payment is by 15th of following month. "
                "(v) Agree total annual PF contributions per ECR to PF expense in P&L.\n\n"
                "Step 6B – TDS on Salaries (Section 192): "
                "(i) Obtain Form 24Q filings for all 4 quarters. "
                "(ii) Agree total salary declared in 24Q with total payroll per books. "
                "(iii) Verify TDS computed correctly per Income Tax slabs for each employee. "
                "(iv) Verify TDS remitted on time (7th of following month). "
                "(v) Verify Form 16 issued to all employees by 15 June 2026.\n\n"
                "Step 6C – Professional Tax (PT): Verify monthly PT deduction and payment per applicable state laws. "
                "ARWL operates in multiple states (Maharashtra, Karnataka, Gujarat) – verify state-wise compliance.\n\n"
                "Step 6D – Gratuity Fund: Verify if ARWL maintains a gratuity fund with LIC/approved insurer. "
                "If yes, verify annual contribution and fund balance. If unfunded, verify provision adequacy."
            ),
            "assertions": ["COM", "ACC", "P&D"],
            "sa_ref": "SA 501 Para 9 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Other Expenses": {
    "objective": (
        "To verify that all other operating expenses are properly authorised, accurately recorded, "
        "relate to the business, are in the correct period, and are appropriately classified between "
        "revenue/capital and between expense categories."
    ),
    "risk_overview": (
        "ARWL's other expenses include: technology and platform maintenance costs, marketing and business development, "
        "professional fees, office expenses, travel, communication, bank charges, insurance, and other administration. "
        "Wealth management companies have high professional fee and technology costs. Risks include: "
        "personal expenses of promoters/directors charged to company, fictitious vendor payments, "
        "incorrect capitalisation vs expensing of tech costs, and non-deduction of TDS on vendor payments."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Analytical Review of Expense Ledgers",
            "risk": "Without detailed analytical procedures, fictitious, personal, or unusually large expenses may pass undetected.",
            "procedure": (
                "Step 1A – Obtain a complete schedule of other expenses for FY 2025-26 broken down by ledger account head, "
                "with comparative figures for FY 2024-25. Compute year-on-year % change for each head.\n\n"
                "Step 1B – For each expense head varying by more than 15% or ₹25 lakhs (whichever is lower), "
                "obtain management explanation and corroborate with independent evidence (contracts, invoices, market rates).\n\n"
                "Step 1C – Compute each expense as a percentage of total revenue and compare with prior year. "
                "Rising expense ratios without business justification are a risk indicator.\n\n"
                "Step 1D – Identify any new expense accounts that appear in FY 2025-26 that were not present in prior year. "
                "Investigate the nature and business purpose of such new categories.\n\n"
                "Step 1E – Specifically analyse: professional fees (for any undisclosed related-party payments), "
                "marketing expenses (for promotional expenses without adequate supporting), "
                "and 'miscellaneous expenses' (often used to hide fictitious charges)."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 520 Para 5, 6 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.12",
        },
        {
            "no": 2,
            "category": "Vouching – Large & Unusual Expenses",
            "risk": "Large or unusual expense items may lack business substance or may involve undisclosed related-party transactions.",
            "procedure": (
                "Step 2A – Using risk-based and value-based selection, select vouchers covering at least 65% of total other expenses by value. "
                "Ensure selection includes all items above ₹10 lakhs individually, plus a random sample of smaller items.\n\n"
                "Step 2B – For each selected expense voucher: "
                "(i) Verify original tax invoice (not photocopy) with GST number, GSTIN of vendor, HSN/SAC code. "
                "(ii) Verify vendor is registered and GST return filed (check GST portal for GSTR-1). "
                "(iii) Verify purchase order / contract / work order authorised per Delegation of Authority. "
                "(iv) Verify goods/services received note or completion certificate for services. "
                "(v) Verify invoice approved for payment by authorised signatory. "
                "(vi) Trace to bank payment statement – confirm payment to vendor account.\n\n"
                "Step 2C – TDS compliance verification: "
                "(i) Professional fees (advocates, CAs, consultants) above ₹30,000: TDS @ 10% u/s 194J. "
                "(ii) Contract/outsourced services above ₹30,000: TDS @ 2% u/s 194C. "
                "(iii) Rent above ₹2,40,000/year: TDS @ 10% u/s 194I. "
                "(iv) Verify TDS remitted and Form 26Q filed.\n\n"
                "Step 2D – Vendor master review: Check for vendors with residential addresses, no GST registration, "
                "or vendor names similar to employee names or directors – red flags for fictitious payments."
            ),
            "assertions": ["OCC", "ACC", "CLA"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.22, S.27",
        },
        {
            "no": 3,
            "category": "Technology & Platform Costs – Capitalisation Assessment",
            "risk": "Technology expenditure may be incorrectly expensed when it meets criteria for capitalisation as an intangible asset under Ind AS 38, or vice versa.",
            "procedure": (
                "Step 3A – Obtain a schedule of all technology-related expenses for FY 2025-26: "
                "software licenses, platform maintenance, SaaS subscriptions, IT infrastructure, development costs, app development.\n\n"
                "Step 3B – For each technology expense, apply the capitalisation test under Ind AS 38: "
                "(i) Technical feasibility to complete the intangible. "
                "(ii) Intention to complete and use/sell. "
                "(iii) Ability to generate probable future economic benefits. "
                "(iv) Adequate resources to complete. "
                "(v) Ability to reliably measure expenditure.\n\n"
                "Step 3C – SaaS Subscriptions: Per IFRIC Agenda Decision (March 2019) and Ind AS treatment, "
                "SaaS/cloud service costs where customer does not control the underlying asset should be expensed as incurred. "
                "Verify no SaaS costs have been capitalised.\n\n"
                "Step 3D – For multi-year technology contracts: verify period allocation – prepaid portion carried forward, "
                "current period portion expensed.\n\n"
                "Step 3E – If ARWL is building a proprietary digital wealth platform (as mentioned in the Annual Report), "
                "verify whether development phase costs have been appropriately capitalised per Ind AS 38 Para 57 "
                "(research phase expensed, development phase capitalised if criteria met)."
            ),
            "assertions": ["OCC", "CLA", "ACC", "VAL"],
            "sa_ref": "SA 500 Para 7 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 4,
            "category": "Cut-off & Accruals Testing",
            "risk": "Expenses may be recorded in wrong period – affecting both current year and prior year P&L.",
            "procedure": (
                "Step 4A – Test expense entries in the period 15 March 2026 to 15 April 2026 for correct period allocation. "
                "Select all items above ₹5 lakhs in this period for review.\n\n"
                "Step 4B – Verify that year-end accruals are complete and accurate: "
                "(i) Audit fee accrual – agree to engagement letter. "
                "(ii) Insurance premium accrual – verify unexpired premium carried forward. "
                "(iii) Maintenance contract accruals – verify period covered by contract. "
                "(iv) Electricity and utility accruals – verify based on January/February usage.\n\n"
                "Step 4C – Review prepaid expenses schedule: verify all items are genuinely prepaid (not expenses in the current year), "
                "and the amortisation is on a straight-line basis over the service period.\n\n"
                "Step 4D – Search for any large invoices dated in March 2026 but paid only in May/June 2026 – "
                "assess whether these have been accrued correctly."
            ),
            "assertions": ["COF", "ACC", "COM"],
            "sa_ref": "SA 330 Para 20",
            "kkc_ref": "KKC Manual S.27",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Borrowings": {
    "objective": (
        "To verify that all borrowings are completely and accurately recorded, exist as at the balance sheet date, "
        "are obligations of the entity, are correctly measured at amortised cost using the effective interest rate (EIR) "
        "method, covenant compliance is maintained, and all required disclosures per Ind AS 107 and Ind AS 32 are made."
    ),
    "risk_overview": (
        "ARWL is primarily a fee-based wealth management company; borrowings are expected to be limited to working capital lines. "
        "However, lease liabilities (Ind AS 116) form a significant part of financial liabilities. "
        "Risks include: off-balance-sheet arrangements not recognised, incorrect EIR computation, "
        "covenant breaches requiring reclassification, undisclosed pledges, and borrowings from related parties."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Completeness – External Confirmation",
            "risk": "Borrowings may be omitted from the balance sheet, particularly credit facilities not fully drawn or guarantee arrangements.",
            "procedure": (
                "Step 1A – Obtain a schedule of all borrowings as at 31 March 2026 from management: "
                "lender name, type of facility, sanctioned amount, outstanding balance, interest rate, repayment terms, security, and covenants.\n\n"
                "Step 1B – Send direct external confirmation requests (per SA 505) to all banks and financial institutions "
                "with whom ARWL has facilities, regardless of whether the facility is drawn down. "
                "Confirmation must cover: outstanding principal, interest accrued, security/collateral given, overdue amounts, and contingent liabilities.\n\n"
                "Step 1C – Agree confirmed balances to books. For any differences: obtain reconciliation, "
                "investigate timing differences, and ensure no unrecorded borrowings.\n\n"
                "Step 1D – Review board minutes for all 12 months for authorisations of new borrowings or security creation. "
                "Verify all such authorisations are reflected in the borrowings schedule.\n\n"
                "Step 1E – Review ROC filings – Form CHG-1/CHG-4 (charge creation/modification/satisfaction). "
                "Any charge registered with ROC must correspond to a borrowing in the books.\n\n"
                "Step 1F – Review bank statements for all accounts for any repayment/receipt patterns suggesting undisclosed borrowings."
            ),
            "assertions": ["COM", "EXI", "R&O"],
            "sa_ref": "SA 505 Para 7, 8, 9 | SA 500 Para 7 | SA 501 Para 9",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Measurement – EIR & Amortised Cost",
            "risk": "Borrowings may be recorded at nominal value rather than amortised cost using EIR, understating interest expense and overstating borrowings.",
            "procedure": (
                "Step 2A – For each material borrowing carried at amortised cost (as required by Ind AS 109): "
                "verify management has computed EIR correctly including upfront fees, processing charges, and other transaction costs.\n\n"
                "Step 2B – Obtain loan agreement for each borrowing. Identify: principal disbursed, transaction costs incurred, "
                "coupon rate, repayment schedule (equated installments or bullet), and any prepayment penalties.\n\n"
                "Step 2C – Independently recompute the EIR using Excel IRR function or financial calculator: "
                "EIR = IRR of cash flows (initial disbursement received, all principal and interest outflows). "
                "Compare with management's EIR.\n\n"
                "Step 2D – Verify amortised cost schedule: "
                "Opening balance + EIR interest – Actual cash interest paid – Principal repayment = Closing amortised cost balance. "
                "Agree to balance sheet figure.\n\n"
                "Step 2E – Verify interest expense in P&L = EIR × Opening amortised cost (or weighted average balance). "
                "Cross-check with Finance Costs workpaper."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "Covenant Compliance & Classification",
            "risk": "Breach of financial covenants may require reclassification of borrowings from non-current to current, affecting liquidity ratios and going concern assessment.",
            "procedure": (
                "Step 3A – List all financial and non-financial covenants from loan agreements.\n\n"
                "Step 3B – Compute each covenant ratio as at 31 March 2026 using audited figures. Verify compliance.\n\n"
                "Step 3C – If any covenant is breached: "
                "(i) Verify the borrowing is reclassified to current liabilities per Ind AS 1 Para 74. "
                "(ii) Check if lender has provided a waiver letter – if waiver received before balance sheet date and terms met, may remain non-current. "
                "(iii) Assess impact on going concern assessment.\n\n"
                "Step 3D – Verify correct presentation: current vs non-current portion of term loans. "
                "Current = amount repayable within 12 months of balance sheet date. Recompute from repayment schedule."
            ),
            "assertions": ["CLA", "P&D", "COM"],
            "sa_ref": "SA 560 Para 6 | SA 570 Para 10 | Ind AS 1 Para 74",
            "kkc_ref": "KKC Manual S.24, S.43",
        },
        {
            "no": 4,
            "category": "Security & Disclosures",
            "risk": "Security/collateral provided on borrowings may not be disclosed, or may cover assets not reflected in the balance sheet.",
            "procedure": (
                "Step 4A – For each borrowing: identify the security (hypothecation, pledge, mortgage) provided.\n\n"
                "Step 4B – Verify the secured asset is in the balance sheet and its carrying value is reasonable relative to the outstanding loan.\n\n"
                "Step 4C – Verify CARO 2020 Clause 3(iv) compliance: report on default in repayment. "
                "Confirm no repayment default during the year by checking lender statements.\n\n"
                "Step 4D – Verify Ind AS 107 disclosures: maturity analysis of borrowings (< 1 year, 1-3 years, 3-5 years, > 5 years), "
                "interest rate sensitivity, fair value disclosure, and nature of security.\n\n"
                "Step 4E – Verify CARO 2020 Clause 3(v): Report on default in repayment to banks/FIs/debenture holders."
            ),
            "assertions": ["P&D", "COM"],
            "sa_ref": "SA 700 Para 13 | SA 330 Para 20",
            "kkc_ref": "KKC Manual S.46, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Finance Costs": {
    "objective": (
        "To verify that all finance costs (interest on borrowings, lease interest, bank charges, "
        "processing fees, and other finance charges) are completely and accurately recorded, "
        "relate to the current period, and are appropriately disclosed."
    ),
    "risk_overview": (
        "Finance costs must reconcile with borrowings – any disconnect indicates either misstatement of borrowings "
        "or incorrect interest computation. Additionally, interest on lease liability (Ind AS 116 unwinding) "
        "must be separately tracked. Risk: understatement of finance costs to inflate operating margins."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Analytical Verification",
            "risk": "Finance costs may be understated to improve reported profitability or EBITDA metrics.",
            "procedure": (
                "Step 1A – Compute the implied average interest rate: Finance Costs ÷ Average Borrowings balance (opening + closing ÷ 2). "
                "Compare with contractual interest rates on each facility. Significant unexplained difference requires investigation.\n\n"
                "Step 1B – Reconcile finance costs to components: "
                "(i) Interest on borrowings per EIR schedule (from Borrowings workpaper). "
                "(ii) Interest on lease liabilities per Ind AS 116 unwinding schedule. "
                "(iii) Bank charges and commission. "
                "(iv) Other finance charges. "
                "Total must agree with P&L finance costs figure.\n\n"
                "Step 1C – Compare finance costs year-on-year: if borrowings increased, finance costs should broadly increase and vice versa. "
                "Unexplained reduction in finance costs with stable/rising borrowings is a red flag."
            ),
            "assertions": ["COM", "ACC"],
            "sa_ref": "SA 520 Para 5 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.12",
        },
        {
            "no": 2,
            "category": "Vouching & Recomputation",
            "risk": "Individual interest charges may be incorrectly computed or misclassified.",
            "procedure": (
                "Step 2A – Verify interest on each borrowing against lender statement: agree amount and period.\n\n"
                "Step 2B – Verify EIR-based interest = Carrying amount of borrowing × EIR rate. "
                "This must match finance costs charged in P&L (from EIR amortisation table in Borrowings workpaper).\n\n"
                "Step 2C – Verify lease interest (Ind AS 116): For each lease, compute interest for the period = "
                "Opening Lease Liability × IBR. Verify total lease interest in P&L matches sum of all lease computations.\n\n"
                "Step 2D – Verify processing fees / origination fees: these should be part of EIR and amortised, "
                "not expensed immediately (unless immaterial).\n\n"
                "Step 2E – Verify that borrowing costs qualifying for capitalisation (if any capital work-in-progress exists) "
                "are not charged to P&L but capitalised per Ind AS 23."
            ),
            "assertions": ["OCC", "ACC", "COF"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.27",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Investments": {
    "objective": (
        "To obtain sufficient appropriate audit evidence that investments are complete, exist, are owned by the entity, "
        "are correctly classified and measured under Ind AS 109 or Ind AS 28 as applicable, "
        "income from investments is correctly recognised, and impairment is appropriately assessed."
    ),
    "risk_overview": (
        "ARWL may hold: (a) Mutual fund units – treasury management (FVTPL), (b) Equity shares in subsidiaries/associates "
        "at cost less impairment in standalone, (c) Structured product investments (FVTPL), (d) Bonds/NCDs (amortised cost). "
        "Key risks: incorrect Ind AS 109 classification driving wrong P&L/OCI treatment, overvalued subsidiaries without impairment, "
        "ECL not computed for debt instruments, fair value manipulation for unlisted investments."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Investment Schedule & Third-Party Confirmation",
            "risk": "Investments may be fictitiously recorded or investments actually held may differ from what is recorded.",
            "procedure": (
                "Step 1A – Obtain the investment schedule as at 31 March 2026 classified by: type (equity/debt/MF units), "
                "Ind AS 109 category (FVTPL/FVOCI/Amortised Cost), and investee name.\n\n"
                "Step 1B – Mutual fund units: Obtain CAMS and KFintech consolidated account statements as at 31 March 2026. "
                "Verify folio-wise, scheme-wise unit balances. Agree to investment schedule. "
                "Verify NAV used for valuation = NAV published by AMFI on 31 March 2026.\n\n"
                "Step 1C – Listed equity investments: Obtain NSDL/CDSL demat statement for all demat accounts as at 31 March 2026. "
                "Verify ISIN-wise and quantity-wise to investment schedule. Agree closing market price to NSE/BSE data.\n\n"
                "Step 1D – Unlisted equity investments (subsidiaries/associates): Obtain share certificate copies. "
                "Send confirmation to investee company management confirming ARWL's shareholding.\n\n"
                "Step 1E – Bonds/NCDs: Obtain demat statement for bonds. Verify ISIN, face value, and carrying amount per amortised cost schedule.\n\n"
                "Step 1F – Agree total per investment schedule to balance sheet. "
                "Verify current vs non-current classification (investments realisable within 12 months = current)."
            ),
            "assertions": ["EXI", "COM", "R&O", "VAL"],
            "sa_ref": "SA 505 Para 7 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Classification & Measurement – Ind AS 109",
            "risk": "Incorrect classification of investments leads to wrong measurement basis and incorrect P&L or OCI impact.",
            "procedure": (
                "Step 2A – For each investment category, verify classification documentation: "
                "(i) FVTPL: Equity instruments held for trading, or designated at FVTPL, or residual category. "
                "(ii) FVOCI: Equity instruments designated at FVOCI (irrevocable election at initial recognition). "
                "(iii) Amortised Cost: Debt instruments that pass the SPPI test and held in HTC business model. "
                "(iv) FVTPL: Debt instruments not meeting AC or FVOCI criteria.\n\n"
                "Step 2B – For all debt instruments at amortised cost: verify SPPI (Solely Payments of Principal and Interest) test documentation. "
                "If the instrument has features like conversion rights, equity-linked returns, or non-standard interest, it fails SPPI.\n\n"
                "Step 2C – FVTPL valuation: "
                "(i) MF units: Closing NAV per AMFI × units. Recompute and agree. "
                "(ii) Listed equity: NSE/BSE closing price × shares. Recompute and agree. "
                "(iii) Unlisted equity at FVTPL: Obtain independent valuation report. Assess valuer's qualifications and assumptions.\n\n"
                "Step 2D – Verify that classification is consistent with prior year, or if changed, Ind AS 109 Para 4.4 permits reclassification "
                "only on change in business model – verify management's documentation of business model assessment."
            ),
            "assertions": ["VAL", "CLA", "ACC"],
            "sa_ref": "SA 540 Para 8, 13 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "Impairment – Subsidiaries & Associates",
            "risk": "Investments in subsidiaries or associates may be carried at cost significantly above recoverable amount without impairment recognition.",
            "procedure": (
                "Step 3A – For each investment in subsidiary/associate at cost: "
                "Compare carrying value with net assets of investee (from latest audited financial statements).\n\n"
                "Step 3B – Assess impairment indicators per Ind AS 36: "
                "(i) Carrying value > net assets of subsidiary. "
                "(ii) Subsidiary reporting persistent losses. "
                "(iii) Significant adverse changes in technological, market, economic, or regulatory environment. "
                "(iv) Evidence of obsolescence or physical damage of subsidiary's assets.\n\n"
                "Step 3C – If indicators exist: obtain management's impairment test. "
                "Evaluate the DCF model: are the projected cash flows reasonable? "
                "Is the discount rate (WACC) appropriate? Is the terminal growth rate sustainable?\n\n"
                "Step 3D – For listed subsidiaries/associates: compare market capitalisation with net assets – "
                "sustained market cap below book value is an impairment indicator.\n\n"
                "Step 3E – Verify ECL (Expected Credit Loss) computation for debt instruments carried at amortised cost or FVOCI. "
                "Determine stage (Stage 1 – 12 month ECL, Stage 2 – lifetime ECL on credit-deteriorated, Stage 3 – credit-impaired). "
                "Verify computation methodology, probability of default, loss given default, and exposure at default."
            ),
            "assertions": ["VAL", "COM"],
            "sa_ref": "SA 540 Para 8 | SA 620 Para 8",
            "kkc_ref": "KKC Manual S.35, S.37",
        },
        {
            "no": 4,
            "category": "Investment Income & P&L Reconciliation",
            "risk": "Income from investments may be incorrectly classified or omitted from P&L.",
            "procedure": (
                "Step 4A – Prepare a reconciliation of investment income: "
                "(i) FVTPL gains/(losses) = Closing fair value – Opening fair value + Redemptions proceeds – Cost of redemptions. "
                "Agree to P&L figure.\n\n"
                "(ii) Interest income on bonds: Opening amortised cost × EIR × time. Agree to Other Income.\n\n"
                "(iii) Dividend income – from schedule in Other Income workpaper.\n\n"
                "Step 4B – Verify FVOCI movements: Gains/losses on FVOCI investments should be in OCI "
                "(not recycled to P&L for equity instruments; recycled for debt instruments on disposal/derecognition).\n\n"
                "Step 4C – Verify that investment income from related-party investees is at arm's length "
                "(dividends at same rate as other investors, interest at market rate)."
            ),
            "assertions": ["OCC", "ACC", "CLA"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.27",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Trade Receivables & Accrued Income": {
    "objective": (
        "To verify that trade receivables and accrued income are complete, exist, are owned by the entity, "
        "correctly valued (net of ECL provisions), and appropriately disclosed as at 31 March 2026."
    ),
    "risk_overview": (
        "ARWL's receivables primarily comprise: accrued trail commissions not yet received from AMCs, "
        "accrued advisory fees, and other fee receivables. These are financial assets under Ind AS 109 subject to ECL. "
        "Risks: overstatement of accrued income, insufficient ECL provisioning, and concentration risk in receivables."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Existence & Completeness",
            "risk": "Accrued income may be fictitiously included in receivables, or genuine receivables may be omitted.",
            "procedure": (
                "Step 1A – Obtain ageing analysis of trade receivables / accrued income as at 31 March 2026: "
                "categorised by counterparty (AMC-wise, client-wise), amount outstanding, and age bucket (< 30 days, 30-90 days, > 90 days).\n\n"
                "Step 1B – For the top 10 outstanding balances by value: "
                "(i) Verify the underlying transaction – commission calculation or invoice. "
                "(ii) Send external confirmation to AMC or client to confirm the receivable amount. "
                "(iii) Verify subsequent receipt in April/May 2026 as corroboration.\n\n"
                "Step 1C – Cross-link receivables to revenue: Verify that accrued trail income in receivables = "
                "Trail income accrued in P&L but not yet received in cash. Prepare reconciliation.\n\n"
                "Step 1D – Verify there are no credit balances in debtors (which would indicate advance received but not netted)."
            ),
            "assertions": ["EXI", "COM", "R&O"],
            "sa_ref": "SA 505 Para 7 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Valuation – ECL Assessment",
            "risk": "Trade receivables may be overvalued if Expected Credit Loss provision is inadequate.",
            "procedure": (
                "Step 2A – Determine the ECL provisioning approach: "
                "(i) Simplified approach (Ind AS 109 Para 5.5.15) – lifetime ECL for trade receivables without significant financing component. "
                "(ii) General approach – 12-month ECL for Stage 1; lifetime ECL for Stages 2 and 3.\n\n"
                "Step 2B – Review management's provision matrix: "
                "(i) Assess historical loss rates by ageing bucket. "
                "(ii) Verify forward-looking adjustments (macroeconomic factors affecting AMC ability to pay). "
                "(iii) For AMC receivables: AMCs are large, regulated entities – default risk is low but should be documented.\n\n"
                "Step 2C – For any specific receivables identified as doubtful (outstanding > 6 months, disputed): "
                "verify specific provision computation and reasonableness.\n\n"
                "Step 2D – Verify write-offs: any receivables written off during the year – verify proper approval and that the amount was genuinely uncollectible."
            ),
            "assertions": ["VAL", "COM"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "Presentation & Disclosure",
            "risk": "Receivables may not be properly disclosed per Ind AS 107 financial instrument requirements.",
            "procedure": (
                "Step 3A – Verify presentation: current vs non-current classification (receivable within 12 months = current).\n\n"
                "Step 3B – Verify Ind AS 107 disclosures: credit risk concentration, maximum credit exposure, "
                "ageing analysis, ECL movement, and information about any collateral held.\n\n"
                "Step 3C – Verify CARO 2020 Clause 3(ix): report on default in repayment of dues."
            ),
            "assertions": ["P&D", "COM"],
            "sa_ref": "SA 700 Para 13",
            "kkc_ref": "KKC Manual S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Cash & Bank Balances": {
    "objective": (
        "To verify that all cash and bank balances are complete, exist, are owned by the entity, "
        "accurately recorded, and appropriately disclosed as at 31 March 2026."
    ),
    "risk_overview": (
        "For ARWL, cash and bank balances include: current accounts, savings accounts, FD accounts (covered under investments), "
        "and potentially escrow accounts. The risk of misappropriation of cash is higher for entities with high cash operations, "
        "but for ARWL (fee-based digital company), risks are primarily around completeness of account disclosure and "
        "accuracy of bank reconciliations."
    ),
    "steps": [
        {
            "no": 1,
            "category": "External Confirmation & Reconciliation",
            "risk": "Bank balances may be misstated – either overstated through kiting or understated by omitting accounts.",
            "procedure": (
                "Step 1A – Obtain a list of ALL bank accounts maintained by ARWL as at 31 March 2026 "
                "(including accounts opened and closed during the year).\n\n"
                "Step 1B – Send bank confirmation requests directly to all banks for all accounts: "
                "Confirmation should cover: bank balance, overdraft/credit facilities, borrowings outstanding, "
                "guarantees issued, and any assets pledged.\n\n"
                "Step 1C – Obtain bank reconciliation statements for all significant accounts as at 31 March 2026. "
                "Verify: (i) Balance per books = Balance per bank statement ± reconciling items. "
                "(ii) Outstanding cheques are genuine – not older than 90 days (stale cheques). "
                "(iii) Deposits in transit are credited in April 2026 bank statement. "
                "(iv) No unexplained reconciling items.\n\n"
                "Step 1D – Scan April 2026 bank statements (first 15 days) for large unusual transactions "
                "that may represent window-dressing of March 2026 balances (kiting)."
            ),
            "assertions": ["EXI", "COM", "ACC"],
            "sa_ref": "SA 505 Para 7, 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Completeness of Accounts Disclosure",
            "risk": "Undisclosed bank accounts may be used to siphon funds or hide transactions.",
            "procedure": (
                "Step 2A – Cross-check bank account list with: (i) Board resolutions for opening/closing of accounts, "
                "(ii) IT return filings – bank accounts must be declared in income tax return, "
                "(iii) GST registration – bank accounts linked to GSTIN.\n\n"
                "Step 2B – Verify that all accounts are in the name of ARWL (not personal accounts of directors or employees).\n\n"
                "Step 2C – For any accounts with minimal or zero balances: verify these are not used to route transactions outside normal operations."
            ),
            "assertions": ["COM", "R&O"],
            "sa_ref": "SA 500 Para 7 | SA 240 Para 32",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 3,
            "category": "Presentation & Disclosures",
            "risk": "Cash and cash equivalents may not be correctly defined or short-term FDs included incorrectly.",
            "procedure": (
                "Step 3A – Verify the definition of 'cash equivalents' per Ind AS 7: "
                "short-term, highly liquid investments with original maturity of 3 months or less. "
                "Ensure only qualifying items are included.\n\n"
                "Step 3B – Verify cash flow statement preparation: "
                "opening + closing cash and cash equivalents per cash flow statement = balance sheet balances. "
                "Verify no other items (long-term FDs) are included.\n\n"
                "Step 3C – Verify if any cash is restricted (e.g. margin money with exchanges, security deposits with regulators). "
                "Restricted cash should not be classified as 'cash and cash equivalents'."
            ),
            "assertions": ["P&D", "CLA"],
            "sa_ref": "SA 700 Para 13 | Ind AS 7",
            "kkc_ref": "KKC Manual S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Share Capital, Reserves & Equity": {
    "objective": (
        "To verify that share capital is correctly recorded, all movements in reserves are properly authorised "
        "and accurately reflected, equity transactions are compliant with Companies Act 2013 and SEBI regulations, "
        "and EPS is correctly computed and disclosed per Ind AS 33."
    ),
    "risk_overview": (
        "ARWL declared a 1:1 bonus issue in March 2025 and declared total dividend of ₹14/share (pre-bonus equivalent). "
        "Key risks: incorrect recording of bonus issue, EPS not restated for bonus issue, "
        "ESOP exercise incorrectly recorded, unauthorised share issuances, and incorrect dividend accounting."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Share Capital Verification",
            "risk": "Share capital balances may be incorrect if bonus issue or ESOP exercise is incorrectly recorded.",
            "procedure": (
                "Step 1A – Obtain the share capital reconciliation: "
                "Opening number of shares × face value = Opening share capital. "
                "Add: Bonus shares issued (1:1 ratio) × face value = Bonus share capital. "
                "Add: ESOP shares exercised × face value = ESOP share capital addition. "
                "Closing share capital per books must agree with balance sheet.\n\n"
                "Step 1B – Bonus Issue verification: "
                "(i) Verify Board resolution and shareholder approval for 1:1 bonus issue. "
                "(ii) Verify source of bonus: capitalisation from free reserves (Securities Premium or General Reserve). "
                "(iii) Verify that the reserve capitalised was available (not restricted). "
                "(iv) Verify new shares registered with ROC – Form SH-7 / Form SH-8. "
                "(v) Agree increased share capital to BSE/NSE listing confirmation.\n\n"
                "Step 1C – ESOP exercise: Verify shares allotted on ESOP exercise = exercise price collected in cash "
                "(agree to bank) + ESOP reserve transferred to share capital and securities premium.\n\n"
                "Step 1D – Confirm total shares outstanding with registrar (KFintech/Link Intime) as at 31 March 2026."
            ),
            "assertions": ["EXI", "COM", "ACC", "R&O"],
            "sa_ref": "SA 500 Para 7 | SA 505 Para 7",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Reserves & Surplus Movement",
            "risk": "Reserves may be incorrectly adjusted or movements unauthorised.",
            "procedure": (
                "Step 2A – Obtain movement schedule for each reserve: "
                "Retained Earnings, Securities Premium, General Reserve, Capital Redemption Reserve, ESOP Reserve, "
                "FVOCI Reserve, and OCI – Actuarial Gains/Losses.\n\n"
                "Step 2B – Verify Retained Earnings: Opening + PAT ± OCI items – Dividends declared = Closing. "
                "Agree PAT to P&L. Agree dividends to Board resolutions.\n\n"
                "Step 2C – Dividend verification: "
                "(i) Verify Board resolution for interim dividend (₹7/share). "
                "(ii) Verify AGM approval for final dividend recommendation (₹7/share on post-bonus capital). "
                "(iii) Verify dividend is only on paid-up equity capital. "
                "(iv) Verify TDS on dividend @ 10% u/s 194 deducted and remitted.\n\n"
                "Step 2D – Verify OCI items: Actuarial gains/(losses) on DBO and FVOCI investment movements "
                "are correctly transferred to OCI Reserve, net of deferred tax.\n\n"
                "Step 2E – Verify that no reserve is restricted from distribution without proper compliance with Companies Act."
            ),
            "assertions": ["OCC", "ACC", "COM"],
            "sa_ref": "SA 500 Para 7 | SA 330 Para 18",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 3,
            "category": "Earnings Per Share – Ind AS 33",
            "risk": "EPS may be incorrectly computed – particularly if bonus issue adjustment not applied retrospectively.",
            "procedure": (
                "Step 3A – Basic EPS = Net profit attributable to ordinary shareholders ÷ Weighted average number of ordinary shares outstanding.\n\n"
                "Step 3B – Critical adjustment: Bonus issue treated as if it occurred at the beginning of the earliest period presented. "
                "Verify that EPS for the current year AND prior year comparative is computed on post-bonus share count.\n\n"
                "Step 3C – Diluted EPS: Identify all potential dilutive instruments (ESOP options outstanding, convertible instruments). "
                "Compute diluted EPS using treasury stock method for options.\n\n"
                "Step 3D – Verify disclosures per Ind AS 33: numerator and denominator reconciliation, "
                "instruments that may dilute basic EPS in future, and reason for adjustment to weighted average shares."
            ),
            "assertions": ["ACC", "P&D"],
            "sa_ref": "SA 700 Para 13 | Ind AS 33",
            "kkc_ref": "KKC Manual S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Provisions & Other Liabilities": {
    "objective": (
        "To verify that all provisions and other liabilities are completely and accurately recorded, "
        "are obligations of the entity, correctly measured, and appropriately disclosed per Ind AS 37 "
        "(Provisions, Contingent Liabilities and Contingent Assets)."
    ),
    "risk_overview": (
        "Provisions include: bonus payable, leave encashment (short-term), statutory dues payable, "
        "audit fees payable, and other accruals. Ind AS 37 requires provisions to meet three criteria: "
        "present obligation, probable outflow, and reliable estimate. Risk: provisions may be under-accrued "
        "to inflate profits, or over-accrued to create cookie-jar reserves."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Completeness of Provisions",
            "risk": "Obligations may not be provisioned leading to understatement of liabilities and overstatement of profits.",
            "procedure": (
                "Step 1A – Obtain a schedule of all provisions as at 31 March 2026.\n\n"
                "Step 1B – Assess completeness: Review contracts, agreements, and correspondence for any obligations "
                "not yet provisioned. Specifically look for: pending litigation settlements, regulatory penalty obligations, "
                "vendor warranty claims, and service guarantees.\n\n"
                "Step 1C – For each provision, apply the Ind AS 37 recognition test: "
                "(i) Present obligation (legal or constructive) from past event? "
                "(ii) Probable outflow of economic resources? "
                "(iii) Reliable estimate possible? "
                "If all three criteria are met, provision must be recognised.\n\n"
                "Step 1D – Inquire of management and legal counsel about any pending matters where obligation exists but no provision made."
            ),
            "assertions": ["COM", "OCC"],
            "sa_ref": "SA 315 Para 11 | SA 501 Para 9",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Measurement & Movement",
            "risk": "Provisions may be incorrectly measured or manipulated for earnings management purposes.",
            "procedure": (
                "Step 2A – For each provision, verify measurement: Ind AS 37 requires best estimate of expenditure required to settle. "
                "For significant provisions, assess: (i) Was the estimate based on reasonable assumptions? (ii) Has the provision been consistently computed?\n\n"
                "Step 2B – Verify provision movement: Opening + Additions + Unwinding of discount – Utilisations – Reversals = Closing. "
                "Investigate any large reversals – reversals may indicate original provision was excessive (earnings management).\n\n"
                "Step 2C – For short-term employee benefit provisions (earned leave, sick leave): "
                "verify computation based on leave days outstanding per HR system × daily salary rate.\n\n"
                "Step 2D – For accrued expenses: verify each significant accrual has underlying contractual or statutory basis "
                "(not arbitrary round-sum accruals)."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Taxation – Current & Deferred": {
    "objective": (
        "To verify that current tax expense (income tax payable) is correctly computed, "
        "deferred tax assets/liabilities are completely and accurately recorded and measured, "
        "and all tax-related disclosures per Ind AS 12 are made."
    ),
    "risk_overview": (
        "ARWL paid ₹234 Crores in direct taxes in FY 2024-25 – a significant increase from ₹110 Crores. "
        "This sharp increase (113%) requires verification of underlying taxable income computation. "
        "Deferred tax arises from timing differences (ESOP, defined benefit obligations, depreciation differences, ECL). "
        "Risk: current tax understatement, DTA not recoverable, and inadequate MAT credit disclosure."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Current Tax Computation",
            "risk": "Current tax may be incorrectly computed due to wrong tax rate, incorrect allowances/disallowances, or incorrect taxable income base.",
            "procedure": (
                "Step 1A – Obtain the income tax computation for AY 2026-27 (FY 2025-26). "
                "Verify starting point = accounting profit per P&L.\n\n"
                "Step 1B – Verify standard deductions and allowances under Income Tax Act: "
                "(i) Depreciation per Income Tax Act (block-wise per Schedule II rates). "
                "(ii) Deduction u/s 80IC, 80JJA, or other applicable sections. "
                "(iii) Disallowances: TDS late payment interest, CSR expenditure (u/s 80G vs disallowable), "
                "penalties, personal expenses.\n\n"
                "Step 1C – Verify tax rate applied: For FY 2025-26, if ARWL is under new tax regime, rate = 22% + surcharge + cess. "
                "If under old regime with exemptions, 30% + surcharge + cess. Verify which regime and confirm consistency.\n\n"
                "Step 1D – Verify advance tax payments: Compare advance tax paid (June, September, December, March instalments) "
                "with computed tax liability. Verify interest u/s 234B and 234C is not materially understated.\n\n"
                "Step 1E – Agree total current tax expense to Form ITR-6 / tax computation and ensure consistency between "
                "books and tax return."
            ),
            "assertions": ["ACC", "VAL", "COM"],
            "sa_ref": "SA 500 Para 7 | SA 540 Para 8",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 2,
            "category": "Deferred Tax Assets & Liabilities",
            "risk": "Deferred tax may be incorrectly computed due to wrong temporary differences, incorrect tax rate, or DTA not meeting recognition criteria.",
            "procedure": (
                "Step 2A – Obtain deferred tax working paper. Verify it includes all significant temporary differences:\n"
                "(i) Depreciation: Accounting depreciation vs tax depreciation – timing difference. "
                "(ii) ESOP expense: Deductible only on exercise for tax – creates DTA. "
                "(iii) Defined benefit obligations: Provision recognised in books, deductible when paid – creates DTA. "
                "(iv) ECL provisions: Deductible when actually written off – creates DTA. "
                "(v) FVTPL unrealised gains/losses: Taxable when realised – creates DTL/DTA.\n\n"
                "Step 2B – Verify tax rate applied to temporary differences: For deferred tax, use the enacted/substantively enacted rate "
                "applicable when the temporary difference is expected to reverse.\n\n"
                "Step 2C – DTA Recoverability assessment: DTA should only be recognised if it is probable that future taxable profit "
                "will be available against which the DTA can be utilised (Ind AS 12 Para 24-31). "
                "Given ARWL's track record of profitability (PAT ₹301 Cr), recoverability appears likely – but document the assessment.\n\n"
                "Step 2D – Verify deferred tax on OCI items (actuarial gains/losses, FVOCI investments) is presented in OCI, not P&L.\n\n"
                "Step 2E – Verify Ind AS 12 disclosures: Movement in DTA/DTL, major components of tax expense, reconciliation of "
                "effective tax rate to statutory rate."
            ),
            "assertions": ["VAL", "COM", "P&D"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35, S.46",
        },
        {
            "no": 3,
            "category": "GST Compliance Review",
            "risk": "Incorrect GST treatment may indicate revenue misclassification or expose the company to demands.",
            "procedure": (
                "Step 3A – Verify GST applicability on each revenue stream: "
                "(i) Distribution commissions from AMCs – GST applicable @ 18% (reverse charge if applicable). "
                "(ii) Advisory fees – GST @ 18%. "
                "(iii) Verify GSTR-3B reconciles with GSTR-1 and books.\n\n"
                "Step 3B – Verify Input Tax Credit (ITC) claimed: Only business expenses with proper tax invoice and GSTR-2B credit qualify. "
                "ITC claimed to be reconciled with GSTR-2B monthly.\n\n"
                "Step 3C – Verify compliance with CARO 2020 Clause 3(viii): "
                "Whether company has submitted all mandatory GST returns and paid taxes."
            ),
            "assertions": ["COM", "ACC", "P&D"],
            "sa_ref": "SA 500 Para 7 | CARO 2020 Cl.3(viii)",
            "kkc_ref": "KKC Manual S.44",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Contingent Liabilities & Commitments": {
    "objective": (
        "To identify and assess all contingent liabilities, capital commitments, and other commitments, "
        "verify that recognition criteria under Ind AS 37 are correctly applied, and ensure adequate "
        "disclosure in financial statements per Ind AS 37 and SA 501."
    ),
    "risk_overview": (
        "ARWL faces potential contingent liabilities from: SEBI orders/penalties (prior forensic audit history), "
        "income tax demands and appeals, client complaints/arbitration proceedings, AMFI regulatory actions, "
        "and potential employee litigation. Capital commitments relate to technology investments and office expansion. "
        "Risk: significant contingent liabilities may not be disclosed, or provisions may be made for items that should be contingent liabilities."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Identification – Legal Proceedings & Regulatory Actions",
            "risk": "Significant legal obligations may be unrecorded or disclosed only when they crystallise into actual payments.",
            "procedure": (
                "Step 1A – Obtain a comprehensive list of all legal proceedings, regulatory actions, and claims involving ARWL from:\n"
                "(i) Legal team – list of all litigation (civil, criminal, regulatory). "
                "(ii) Company Secretary – notices from SEBI, AMFI, MCA, Income Tax Department, GST authorities. "
                "(iii) Board minutes – any legal matters discussed. "
                "(iv) Internal audit reports – compliance issues raised.\n\n"
                "Step 1B – SEBI-specific: Given prior SEBI penalty and EY forensic audit, obtain: "
                "(i) Copy of all SEBI orders/show cause notices received. "
                "(ii) Status of compliance with remediation requirements. "
                "(iii) Any ongoing investigations by SEBI.\n\n"
                "Step 1C – Income Tax matters: Obtain Form 26AS, AIS, and list of tax demands / appeals pending. "
                "For each demand: assess likelihood of success (probable/possible/remote).\n\n"
                "Step 1D – Obtain legal representation letter (SA 501 Para 9): "
                "Send a letter to ARWL's external legal advisors requesting their assessment of all pending legal matters. "
                "Request: nature of matter, current status, management's assessment, and lawyer's view on likely outcome."
            ),
            "assertions": ["COM", "OCC", "P&D"],
            "sa_ref": "SA 501 Para 9, 10, 11, 12 | SA 580 Para 11",
            "kkc_ref": "KKC Manual S.44",
        },
        {
            "no": 2,
            "category": "Classification – Provision vs Contingent Liability vs Note Disclosure",
            "risk": "Items may be incorrectly classified, leading to either overstatement of liabilities (provision for items that should be contingent) or non-disclosure (items that should be disclosed as contingent).",
            "procedure": (
                "Step 2A – Apply Ind AS 37 decision framework to each identified item:\n"
                "(i) Present obligation + Probable outflow + Reliable estimate → Provision required. "
                "(ii) Present obligation + Possible outflow OR no reliable estimate → Contingent Liability (disclose). "
                "(iii) Remote possibility of outflow → No provision, no disclosure required.\n\n"
                "Step 2B – For each provision in the financial statements: verify it meets all three Ind AS 37 criteria. "
                "If any criterion is not met, provision may need to be reversed and reclassified to contingent liability.\n\n"
                "Step 2C – Tax assessments: Verify that the company has assessed each demand separately. "
                "Do not net demands against refunds. For demands where appeal is filed, assess probability of success "
                "based on merits of the case and legal opinion."
            ),
            "assertions": ["CLA", "VAL"],
            "sa_ref": "SA 501 Para 9 | SA 540 Para 8",
            "kkc_ref": "KKC Manual S.44, S.35",
        },
        {
            "no": 3,
            "category": "Capital & Other Commitments",
            "risk": "Capital commitments may be omitted, leading to inadequate disclosure of future cash outflows.",
            "procedure": (
                "Step 3A – Obtain schedule of capital commitments as at 31 March 2026: "
                "(i) Contracts entered into but not yet executed (technology, office renovation, equipment). "
                "(ii) Net of advances paid against these contracts.\n\n"
                "Step 3B – Obtain contracts for each commitment and verify: amount committed, timeline, and counterparty.\n\n"
                "Step 3C – Verify other commitments: "
                "(i) Lease commitments (Ind AS 116 – disclosed as lease liability). "
                "(ii) Service contracts with AMCs or technology vendors that are non-cancellable. "
                "(iii) Minimum guarantee arrangements.\n\n"
                "Step 3D – Verify CARO 2020 Clause 3(i)(b): Physical verification of assets. "
                "Verify CARO clause 3(ii): disclosure of inventory-related matters if applicable."
            ),
            "assertions": ["COM", "P&D"],
            "sa_ref": "SA 501 Para 9 | SA 700 Para 13",
            "kkc_ref": "KKC Manual S.44, S.46",
        },
        {
            "no": 4,
            "category": "Disclosure Adequacy",
            "risk": "Contingent liability disclosures may be generic and not entity-specific, failing to provide users with meaningful information.",
            "procedure": (
                "Step 4A – Review Note on Contingent Liabilities in financial statements. "
                "Verify: (i) Each material contingent liability is individually disclosed. "
                "(ii) Nature of contingency is explained. "
                "(iii) Financial impact / range of outcomes is provided. "
                "(iv) Uncertainties affecting timing or amount are described. "
                "(v) Possible reimbursement (e.g. insurance cover) is mentioned.\n\n"
                "Step 4B – Verify cross-consistency: Matters provisioned should not appear in contingent liabilities and vice versa.\n\n"
                "Step 4C – Subsequent events check (SA 560): Any legal matters crystallising between 31 March 2026 and "
                "date of auditor's report that are adjusting events should be reflected in the financial statements."
            ),
            "assertions": ["P&D", "COM", "UNB"],
            "sa_ref": "SA 560 Para 6 | SA 700 Para 13",
            "kkc_ref": "KKC Manual S.43, S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Significant Judgements & Estimates": {
    "objective": (
        "To assess whether management's accounting estimates are reasonable, based on appropriate assumptions, "
        "consistently applied, free from management bias, and adequately disclosed per SA 540 and Ind AS 1 Para 125-133."
    ),
    "risk_overview": (
        "SA 540 is a high-risk area attracting significant NFRA scrutiny. NFRA inspection reports consistently find "
        "that auditors fail to develop their own independent estimate, accept management assumptions without challenge, "
        "and do not document professional judgement exercised. Key estimates for ARWL: actuarial valuations (gratuity/leave), "
        "ESOP fair value, ECL on receivables, deferred tax recoverability, fair value of unlisted investments, "
        "impairment of investments, and income tax provisions."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Complete Inventory of Estimates",
            "risk": "Material estimates may be excluded from the scope of SA 540 procedures if not properly identified.",
            "procedure": (
                "Step 1A – Prepare a complete inventory of all accounting estimates in the financial statements. "
                "Review each note to accounts, accounting policy, and significant judgement disclosure.\n\n"
                "Step 1B – For each estimate, document: "
                "(i) Nature of estimate and the financial statement amount. "
                "(ii) Method used (actuarial, DCF, market observable, formula-based). "
                "(iii) Key assumptions driving the estimate. "
                "(iv) Degree of estimation uncertainty (low/medium/high). "
                "(v) Whether the estimate gives rise to a Significant Risk (SA 315 Para 28).\n\n"
                "Step 1C – Confirm with management: Were any new estimation techniques introduced in FY 2025-26? "
                "Were any changes in accounting estimates made per Ind AS 8? "
                "If yes, verify the change is appropriately disclosed and justified.\n\n"
                "Step 1D – Assess potential for management bias: "
                "Are estimates consistently conservative or aggressive? Is there evidence of anchoring to prior year estimates "
                "without updating for changed circumstances?"
            ),
            "assertions": ["VAL", "P&D"],
            "sa_ref": "SA 540 Para 8, 14 | SA 315 Para 28",
            "kkc_ref": "KKC Manual S.11, S.35",
        },
        {
            "no": 2,
            "category": "Deep Assessment of High-Risk Estimates",
            "risk": "Management estimates in high-judgement areas may be biased or based on unsupported assumptions.",
            "procedure": (
                "Step 2A – For each estimate classified as high uncertainty: "
                "(i) Evaluate the process used by management: Is there a documented model? Who reviews it? What governance applies?\n\n"
                "(ii) Test controls over the estimation process: "
                "Is the estimate reviewed by the CFO? Is the actuary's report reviewed by an independent party? "
                "Are assumptions challenged by the Board?\n\n"
                "(iii) For actuarial estimates (gratuity): Cross-check discount rate assumption against current market rates. "
                "An outdated or conservatively low discount rate would overstate the DBO.\n\n"
                "(iv) For ECL: Verify the historical loss experience used as the basis. "
                "Assess whether forward-looking macro adjustments are reasonable and not biased.\n\n"
                "(v) For impairment DCF: Assess revenue growth rates against actual performance and analyst consensus. "
                "Terminal growth rate should not exceed long-term GDP growth rate. "
                "WACC should be benchmarked against CAPM (using ARWL's beta, market risk premium, risk-free rate)."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 9, 10, 13 | SA 330 Para 14",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "Auditor's Independent Estimate Development",
            "risk": "Without developing an independent estimate, the auditor cannot objectively evaluate whether management's estimate is reasonable. NFRA has flagged this as a recurring deficiency.",
            "procedure": (
                "Step 3A – For each significant estimate (as required by SA 540 Para 13): "
                "Develop the auditor's own point estimate or a range of acceptable estimates.\n\n"
                "Step 3B – For actuarial valuations: "
                "Using actuarial software or working with a KKC-appointed actuary (SA 620), "
                "independently compute DBO using auditor's own assumptions for discount rate and attrition. "
                "Compare with management's actuary result.\n\n"
                "Step 3C – For impairment testing (DCF): "
                "Input management's cash flow projections but apply auditor's own discount rate. "
                "Test sensitivity: what is the value in use if growth rate is reduced by 1%? If WACC increases by 1%?\n\n"
                "Step 3D – Document the comparison: "
                "(i) If management's estimate is within the auditor's range: conclude estimate is reasonable. "
                "(ii) If outside range: obtain additional evidence, challenge management, and consider misstatement.\n\n"
                "Step 3E – Document professional judgement exercised at each step – per NFRA requirements, "
                "the working paper must clearly show the auditor's independent thought process."
            ),
            "assertions": ["VAL"],
            "sa_ref": "SA 540 Para 13, 15, 16 | SA 620 Para 8",
            "kkc_ref": "KKC Manual S.35, S.37",
        },
        {
            "no": 4,
            "category": "Retrospective Review of Prior Year Estimates",
            "risk": "Consistent over/under estimation in prior years suggests systematic bias.",
            "procedure": (
                "Step 4A – Compare prior year estimates (as at 31 March 2025) with actual outcomes in FY 2025-26. "
                "Example: Compare actuarial provision at 31 March 2025 with actual gratuity payments in FY 2025-26. "
                "Large consistent differences indicate management bias.\n\n"
                "Step 4B – For ECL: Compare prior year ECL provision with actual credit losses in current year. "
                "If ECL consistently overstated, it may indicate cookie-jar provisioning.\n\n"
                "Step 4C – Document findings of retrospective review and assess impact on current year estimate evaluation."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 9, 12",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 5,
            "category": "Disclosure Assessment",
            "risk": "Ind AS 1 Para 125-133 disclosures may be boilerplate and not entity-specific.",
            "procedure": (
                "Step 5A – Review critical accounting estimates and judgements disclosure in notes to accounts. "
                "Verify: (i) Each significant estimate is individually disclosed. "
                "(ii) Key assumptions and sources of estimation uncertainty are described. "
                "(iii) Sensitivity analysis provided (what is the impact if assumption changes by X%).\n\n"
                "Step 5B – Verify that disclosures are entity-specific – not standard boilerplate. "
                "NFRA has specifically called out generic disclosures as a deficiency.\n\n"
                "Step 5C – Verify that amounts at risk of material adjustment within next financial year are identified per Ind AS 1 Para 129."
            ),
            "assertions": ["P&D", "COM", "UNB"],
            "sa_ref": "SA 700 Para 13 | SA 540 Para 20",
            "kkc_ref": "KKC Manual S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Related Party Transactions": {
    "objective": (
        "To identify all related parties and transactions, assess arm's length nature, verify proper "
        "authorisation including audit committee and shareholder approvals, and ensure complete and accurate "
        "disclosure per SA 550, Ind AS 24, Companies Act Section 188, and SEBI LODR Regulation 23."
    ),
    "risk_overview": (
        "ARWL is a listed entity within the Anand Rathi Group. Group entities may include investment banking, "
        "stock broking, commodity broking, and other financial services entities. "
        "Prior SEBI forensic audit heightens RPT scrutiny. Risks: undisclosed RPTs, revenue sharing not at arm's length, "
        "investments in or loans to group entities without proper approval, expense allocation between group companies."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Complete Identification of Related Parties",
            "risk": "Related parties may not be completely identified, leading to undisclosed transactions and regulatory non-compliance.",
            "procedure": (
                "Step 1A – Obtain management's related party list and independently verify completeness by:\n"
                "(i) Shareholding pattern from BSE/NSE/MCA – identify entities holding > 2% of ARWL's equity. "
                "(ii) MCA company master data – search for entities with common directors. "
                "(iii) Form DIR-8 / MBP-1 disclosures filed by directors with ARWL. "
                "(iv) Notes to consolidated financial statements – identify all subsidiaries and associates. "
                "(v) Company's group structure chart.\n\n"
                "Step 1B – Verify that the following categories are included per Ind AS 24 Para 9: "
                "(i) Key Management Personnel (KMP) and their relatives. "
                "(ii) Entities in which KMP have significant influence or control. "
                "(iii) Subsidiaries, associates, joint ventures. "
                "(iv) Holding company and fellow subsidiaries.\n\n"
                "Step 1C – Compare with prior year related party list. "
                "Any deletions must be verified (relationship actually ceased) and any additions investigated."
            ),
            "assertions": ["COM", "OCC"],
            "sa_ref": "SA 550 Para 11, 12, 13 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.15",
        },
        {
            "no": 2,
            "category": "Detection of Undisclosed RPTs",
            "risk": "Transactions with related parties may be structured to appear as third-party transactions to avoid disclosure requirements.",
            "procedure": (
                "Step 2A – Apply CAATs to the general ledger: "
                "Screen all transactions to identify counterparties whose names match or are similar to known related parties. "
                "Use fuzzy matching algorithms if available.\n\n"
                "Step 2B – Review bank payments > ₹10 lakhs for any payments to individuals or entities not on the approved vendor list. "
                "Cross-reference with related party list.\n\n"
                "Step 2C – Review contracts signed during the year – verify counterparty identity for all contracts above ₹50 lakhs.\n\n"
                "Step 2D – Examine expense accounts particularly: professional fees, outsourcing fees, marketing expenses, "
                "rent – these are common vehicles for related-party transactions.\n\n"
                "Step 2E – For revenue: Verify that none of the commission/fee income is routed from or through related parties "
                "in a manner that distorts the true nature of the transaction."
            ),
            "assertions": ["OCC", "COM"],
            "sa_ref": "SA 550 Para 14, 15 | SA 240 Para 32",
            "kkc_ref": "KKC Manual S.15, S.25",
        },
        {
            "no": 3,
            "category": "Authorisation – Companies Act & SEBI LODR",
            "risk": "Material RPTs may not have received requisite regulatory approvals, exposing ARWL to penalties and the auditor to qualification obligations.",
            "procedure": (
                "Step 3A – Verify Audit Committee approval: Per SEBI LODR Regulation 23(2), all material RPTs require "
                "prior approval of the Audit Committee. Obtain AC minutes and verify each material RPT was approved.\n\n"
                "Step 3B – Verify shareholder approval: SEBI LODR Regulation 23(4) requires shareholder approval for material RPTs "
                "(threshold: > 10% of annual consolidated turnover). Verify for applicable transactions.\n\n"
                "Step 3C – Companies Act Section 188: For RPTs involving sale/purchase of goods/services above prescribed thresholds, "
                "verify Board approval and ordinary resolution if required.\n\n"
                "Step 3D – Obtain and review the Register of Contracts maintained by Company Secretary per Section 189 of Companies Act. "
                "Verify all Section 188 contracts are entered in this register.\n\n"
                "Step 3E – Verify SEBI LODR Regulation 23(9): Half-yearly disclosure of RPTs to stock exchanges. "
                "Cross-check disclosures filed with NSE/BSE against books."
            ),
            "assertions": ["OCC", "R&O"],
            "sa_ref": "SA 550 Para 16, 17 | SEBI LODR Reg. 23",
            "kkc_ref": "KKC Manual S.15",
        },
        {
            "no": 4,
            "category": "Arm's Length Assessment",
            "risk": "RPTs may not be at arm's length, resulting in wealth transfer from ARWL to related parties and consequent loss to minority shareholders.",
            "procedure": (
                "Step 4A – For each material RPT, obtain the pricing policy / arm's length justification from management.\n\n"
                "Step 4B – Revenue transactions with group companies: "
                "Compare revenue rates/fees with rates charged to unrelated third parties for similar services. "
                "If no comparable unrelated party transactions exist, assess reasonableness of the pricing.\n\n"
                "Step 4C – Expense transactions with group companies (shared services, IT, HR): "
                "Verify allocation methodology is reasonable and consistently applied. "
                "Obtain third-party quotes for similar services to benchmark.\n\n"
                "Step 4D – Lending/borrowing between group companies: "
                "Verify interest rate is at arm's length (comparable to bank lending rates for similar risk profile). "
                "Verify no interest-free or below-market loans exist without proper approval.\n\n"
                "Step 4E – Property/lease transactions with promoter-related entities: "
                "Obtain independent valuation of rent to verify arm's length."
            ),
            "assertions": ["VAL", "OCC", "R&O"],
            "sa_ref": "SA 550 Para 16, 17 | SA 540 Para 8",
            "kkc_ref": "KKC Manual S.15, S.35",
        },
        {
            "no": 5,
            "category": "Completeness of Disclosure",
            "risk": "Ind AS 24 and SEBI LODR disclosure requirements are extensive and omissions can lead to financial statements not giving a true and fair view.",
            "procedure": (
                "Step 5A – Review Note on Related Party Disclosures. "
                "Verify ALL identified RPTs appear in the note with: counterparty name, nature of relationship, "
                "transaction description, amount during year, and outstanding balance.\n\n"
                "Step 5B – Agree RPT note amounts to underlying ledgers. "
                "Verify the figures are complete (not just selected transactions).\n\n"
                "Step 5C – Verify outstanding balances with related parties are shown separately in the balance sheet.\n\n"
                "Step 5D – Verify SEBI LODR Regulation 34(3) & Schedule V – Annual Report RPT disclosure "
                "is consistent with the financial statement disclosures.\n\n"
                "Step 5E – Verify disclosure of KMP compensation: "
                "Short-term benefits (salary, bonus), post-employment benefits (PF, gratuity), "
                "other long-term benefits, termination benefits, and share-based payments – all per Ind AS 24 Para 17."
            ),
            "assertions": ["COM", "P&D"],
            "sa_ref": "SA 550 Para 25, 26 | SA 700 Para 13",
            "kkc_ref": "KKC Manual S.46, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Fraud Risk Assessment": {
    "objective": (
        "To identify and assess all risks of material misstatement due to fraud at both the financial statement "
        "and assertion levels, design and implement appropriate responses to those risks, and respond appropriately "
        "to identified or suspected fraud in accordance with SA 240."
    ),
    "risk_overview": (
        "ARWL-specific fraud context: Prior depository fraud event, SEBI penalty, and EY forensic audit on record. "
        "This prior history is a significant risk factor requiring heightened professional scepticism. "
        "SA 240 Para 26 treats revenue recognition as a presumed fraud risk for all audits. "
        "Additional fraud risks for wealth management: client fund misappropriation, fictitious commission claims, "
        "mis-selling leading to regulatory penalties, and management override of revenue recognition controls."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Engagement Team Brainstorming – RAPD",
            "risk": "Without a formal, structured discussion, fraud risks may be individually identified but not collectively assessed, leading to gaps in audit response.",
            "procedure": (
                "Step 1A – Conduct a formal Risk Assessment and Planning Discussion (RAPD) with ALL members of the engagement team, "
                "including the Engagement Partner. This must be a genuine discussion, not a tick-box exercise.\n\n"
                "Step 1B – The discussion must specifically address: "
                "(i) How could management commit financial statement fraud? "
                "(ii) Where could employee fraud or asset misappropriation occur? "
                "(iii) Are there revenue targets, analyst expectations, or bonus schemes that create incentive to manipulate? "
                "(iv) Given ARWL's prior SEBI forensic audit, what systemic weaknesses might remain? "
                "(v) Are there complex transactions near year-end that could be used to manipulate results?\n\n"
                "Step 1C – Review prior year audit file for fraud indicators noted. "
                "Review SEBI/EY forensic findings (if available) for systemic issues.\n\n"
                "Step 1D – Document the discussion outcomes in a RAPD memorandum signed by all attendees. "
                "The document must show a genuine exchange of ideas, not standard paragraphs. "
                "Per NFRA requirements: documentation must demonstrate actual discussion, not a standard template."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 240 Para 15, 16 | SA 315 Para 10 | SA 230 Para 8",
            "kkc_ref": "KKC Manual S.14",
        },
        {
            "no": 2,
            "category": "Management & TCWG Fraud Inquiries",
            "risk": "Known or suspected fraud may not be identified unless specific, direct inquiries are made of multiple persons at different levels.",
            "procedure": (
                "Step 2A – Inquire of Senior Management (CEO, CFO, COO): "
                "(i) Is management aware of any fraud or suspected fraud involving the company? "
                "(ii) What anti-fraud controls does the company have? "
                "(iii) Are there any areas where internal controls are overridden?\n\n"
                "Step 2B – Inquire of Internal Audit: "
                "(i) What fraud investigations were conducted in FY 2025-26? "
                "(ii) Were any control deficiencies found that could facilitate fraud? "
                "(iii) Were all findings reported to the Audit Committee?\n\n"
                "Step 2C – Inquire of Audit Committee (those charged with governance): "
                "(i) Whistleblower complaints received? "
                "(ii) Any allegations against management? "
                "(iii) Regulatory actions that may indicate fraud?\n\n"
                "Step 2D – Inquire of employees in accounts payable, payroll, and revenue teams "
                "(those not in senior management positions) about any pressures to record unusual entries.\n\n"
                "Step 2E – Document all inquiries and responses. "
                "Assess consistency – any inconsistency in responses must be investigated."
            ),
            "assertions": ["OCC", "COM"],
            "sa_ref": "SA 240 Para 17, 18, 19, 20 | SA 260 Para 4",
            "kkc_ref": "KKC Manual S.14",
        },
        {
            "no": 3,
            "category": "Presumed Fraud Risk – Revenue Recognition",
            "risk": "SA 240 Para 26 requires the auditor to presume fraud risk in revenue recognition for all audits. This cannot be rebutted without strong documented evidence.",
            "procedure": (
                "Step 3A – Document the presumed fraud risk in revenue recognition and the basis for any rebuttal "
                "(if the engagement team believes revenue manipulation risk is low based on entity's business model – e.g. commission income from AMCs which is third-party verifiable).\n\n"
                "Step 3B – Design specific procedures responsive to this presumed fraud risk:\n"
                "(i) Journal entry testing on revenue accounts (covered in Revenue workpaper). "
                "(ii) Cut-off testing with heightened focus near year-end. "
                "(iii) Confirming significant revenue amounts directly with AMCs. "
                "(iv) Testing for side agreements that modify revenue terms. "
                "(v) Checking for revenue reversals in April/May 2026.\n\n"
                "Step 3C – NFRA specifically requires: "
                "If revenue fraud risk is rebutted, the documentation must clearly show why the specific characteristics of the entity's revenue make fraud highly unlikely. A generic rebuttal is insufficient."
            ),
            "assertions": ["OCC", "ACC", "COF"],
            "sa_ref": "SA 240 Para 26, 27, 32(a)",
            "kkc_ref": "KKC Manual S.14, S.25",
        },
        {
            "no": 4,
            "category": "Management Override of Controls",
            "risk": "SA 240 Para 31 identifies management override as always a significant risk. Specific mandatory procedures must be performed regardless of assessed control environment.",
            "procedure": (
                "Step 4A – Journal Entry Testing (MANDATORY per SA 240 Para 32(a)):\n"
                "(i) Obtain entire JE population for FY 2025-26 directly from the accounting system. "
                "(ii) Screen for: entries by senior management, entries made after period-end, "
                "entries with non-standard descriptions, round-number entries, entries to unusual account combinations, "
                "entries reversing in the following period.\n"
                "(iii) Select items for investigation based on risk characteristics. "
                "(iv) Obtain documentation for all selected entries and assess propriety.\n\n"
                "Step 4B – Review of accounting estimates for bias (MANDATORY per SA 240 Para 32(b)):\n"
                "(i) Review the direction of management's estimates (consistently aggressive = always at upper end of range). "
                "(ii) Assess whether estimates have changed in a manner that produces a particular financial result. "
                "(iii) Compare estimates with outcomes of prior year estimates.\n\n"
                "Step 4C – Evaluation of significant unusual transactions (MANDATORY per SA 240 Para 32(c)):\n"
                "(i) Obtain a list of all significant, unusual, or complex transactions in the year. "
                "(ii) For each: understand the business rationale, verify the transaction was properly authorised, "
                "confirm it was recorded in accordance with applicable accounting standards. "
                "(iii) Be specifically alert to transactions that lack economic substance (e.g. circular transactions with group companies)."
            ),
            "assertions": ["OCC", "ACC", "VAL"],
            "sa_ref": "SA 240 Para 31, 32, 33 | SA 580 Para 16",
            "kkc_ref": "KKC Manual S.14, S.25, S.47",
        },
        {
            "no": 5,
            "category": "Specific Fraud Risks – Wealth Management Sector",
            "risk": "Sector-specific fraud risks in wealth management may not be covered by standard audit procedures.",
            "procedure": (
                "Step 5A – Client funds segregation: Verify that client monies are not commingled with company funds. "
                "Check for any client money violations – SEBI Regulations require strict segregation.\n\n"
                "Step 5B – Mis-selling risk: Review any complaints filed by clients alleging mis-selling of products. "
                "Assess whether provisions are adequate for potential refunds or penalties.\n\n"
                "Step 5C – Ghost clients / fictitious AUM: "
                "Cross-verify AUM data with AMFI published data for ARWL as distributor. "
                "AMFI publishes distributor-wise AUM data – reconcile with internal AUM records.\n\n"
                "Step 5D – Fictitious commission: "
                "Verify that commission income is supported by actual AMC-issued credit notes. "
                "Check that commission for the same period is not claimed from multiple sources.\n\n"
                "Step 5E – Response if fraud detected or suspected: "
                "(i) Immediately escalate to Engagement Partner. "
                "(ii) Assess impact on audit risk assessment and sufficiency of evidence. "
                "(iii) Communicate to Audit Committee per SA 260 Para 10. "
                "(iv) Consider obligation under Companies Act Section 143(12): If fraud involving ₹1 crore or more by officers/employees, report to Central Government via MCA portal."
            ),
            "assertions": ["OCC", "COM"],
            "sa_ref": "SA 240 Para 35, 36, 40 | Companies Act S.143(12)",
            "kkc_ref": "KKC Manual S.14, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Risk Assessment – FSLI": {
    "objective": (
        "To perform risk assessment procedures to obtain a thorough understanding of the entity, its environment, "
        "and its internal controls, identify and assess risks of material misstatement at both the financial statement "
        "level and assertion level for each significant FSLI, and document planned audit responses."
    ),
    "risk_overview": (
        "SA 315 is the foundation of the entire audit. NFRA inspections consistently identify deficiencies in: "
        "inadequate walkthroughs, IT environment understanding gaps, failure to assess significant risks properly, "
        "and assertion-level risk assessments not linked to planned procedures. "
        "For ARWL, significant risks at FSLI level include: revenue recognition, actuarial estimates, RPTs, and IT-driven automated processes."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Understanding Entity – Business Model & Industry",
            "risk": "Inadequate business understanding leads to incorrect risk identification and planning.",
            "procedure": (
                "Step 1A – Document ARWL's business model: AMFI-registered mutual fund distributor and wealth management company. "
                "Revenue = commissions from AMCs (trail and upfront) + advisory fees. "
                "Operating model: RM-driven client acquisition and retention. "
                "Target segment: HNI clients with investible wealth of ₹50 Lakhs to ₹500 Crores.\n\n"
                "Step 1B – Industry dynamics: Review AMFI AUM data, SEBI annual report, and competitor disclosures. "
                "Understand industry commission structures and regulatory changes (SEBI circulars on expense ratios).\n\n"
                "Step 1C – Regulatory environment: Document all applicable regulations – SEBI (LODR, IOSCO), AMFI, "
                "Companies Act, Income Tax Act, GST, and Exchange Control (for Dubai operations).\n\n"
                "Step 1D – Financial performance review: Compute key ratios – Revenue growth (30%), PAT margin, "
                "AUM/Revenue ratio, Employee cost/Revenue ratio. Identify trends and anomalies.\n\n"
                "Step 1E – Understand incentives and pressures: Listed entity with analyst coverage, "
                "management has stated 20-25% PAT growth target. High public scrutiny = pressure to maintain trajectory."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 315 Para 11, 12, A51 | SA 520 Para 5",
            "kkc_ref": "KKC Manual S.8",
        },
        {
            "no": 2,
            "category": "Understanding Internal Controls",
            "risk": "Control deficiencies may lead to undetected misstatements; overreliance on controls without testing reduces audit effectiveness.",
            "procedure": (
                "Step 2A – Control Environment: Assess tone at top, organisational structure, authority and responsibility, "
                "HR policies, code of ethics, and commitment to competence.\n\n"
                "Step 2B – Entity Risk Assessment Process: Understand how ARWL identifies and manages business and financial reporting risks. "
                "Does the entity have a formal ERM framework? How are financial reporting risks addressed?\n\n"
                "Step 2C – Information System: Understand how transactions are initiated, authorised, processed, recorded, and reported. "
                "Identify key IT applications and manual controls at each stage.\n\n"
                "Step 2D – Control Activities: Identify specific controls relevant to each significant FSLI: "
                "authorisation controls, reconciliation procedures, segregation of duties, physical safeguards.\n\n"
                "Step 2E – Monitoring: Internal audit function, management reviews, KPI dashboards, "
                "audit committee oversight, SEBI compliance monitoring.\n\n"
                "Step 2F – Perform walkthroughs for at least 3 significant processes (revenue, payroll, treasury). "
                "Document walkthrough using a flowchart or process description. Identify one transaction from origination to recording. "
                "NFRA requirement: walkthrough documentation must be sufficiently detailed to demonstrate understanding."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 315 Para 14-24 | SA 330 Para 8",
            "kkc_ref": "KKC Manual S.10, S.9",
        },
        {
            "no": 3,
            "category": "FSLI Risk Assessment Matrix",
            "risk": "Without a structured risk assessment matrix, procedures may not be tailored to specific risks at the assertion level.",
            "procedure": (
                "Step 3A – Prepare the FSLI Risk Assessment Matrix for all significant balance sheet and P&L line items. "
                "For each FSLI, assess:\n"
                "(i) Inherent risk factors: volume of transactions, complexity, degree of judgement, susceptibility to fraud. "
                "(ii) Control risk: strength of internal controls over this FSLI (reliance vs pure substantive). "
                "(iii) Combined RoMM per assertion.\n\n"
                "Step 3B – Identify which FSLIs give rise to 'significant risks' per SA 315 Para 27: "
                "Significant risks require: (i) Special audit consideration, (ii) Substantive procedures mandatory (cannot rely solely on controls), "
                "(iii) Must include specific test of details.\n\n"
                "Step 3C – For ARWL, likely significant risks: "
                "(i) Revenue recognition – commission income accuracy. "
                "(ii) Actuarial valuations – complexity and management judgement. "
                "(iii) IT-driven automated calculations – risk if ITGC deficient. "
                "(iv) RPTs – given group structure and prior SEBI scrutiny.\n\n"
                "Step 3D – Link each assessed risk to specific planned audit procedures. "
                "The linkage must be explicit: 'This risk is addressed by procedure X in workpaper Y.'"
            ),
            "assertions": ["OCC", "COM", "ACC", "VAL", "EXI", "P&D"],
            "sa_ref": "SA 315 Para 25, 26, 27, 28 | SA 330 Para 6",
            "kkc_ref": "KKC Manual S.17",
        },
        {
            "no": 4,
            "category": "Overall Financial Statement Level Risk Response",
            "risk": "FS-level risks pervade the entire audit and require an overall response design.",
            "procedure": (
                "Step 4A – Assess overall FS-level risks: "
                "(i) Management integrity and tone at top. "
                "(ii) Complexity of the entity's business model and transactions. "
                "(iii) Pressure to meet external benchmarks (analyst expectations, bonus targets). "
                "(iv) Control environment deficiencies.\n\n"
                "Step 4B – Design overall responses (SA 330 Para 5-6): "
                "(i) Assign most senior and experienced team members to highest-risk areas. "
                "(ii) Incorporate elements of unpredictability – change sample selection methodology, "
                "visit branch offices, perform surprise cash counts. "
                "(iii) Modify timing – perform more work at period end rather than interim. "
                "(iv) Increase reliance on substantive procedures rather than controls where control environment is weak.\n\n"
                "Step 4C – For listed entity: Engagement Quality Control Review (EQCR) to be completed before report issuance. "
                "Assign EQCR reviewer (partner not involved in engagement) at planning stage."
            ),
            "assertions": ["OCC", "COM", "ACC", "VAL"],
            "sa_ref": "SA 315 Para 26 | SA 330 Para 5, 6 | SA 240 Para 22",
            "kkc_ref": "KKC Manual S.17, S.19",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Going Concern": {
    "objective": (
        "To assess whether the going concern assumption used in preparing the financial statements is appropriate, "
        "obtain sufficient appropriate audit evidence to support management's assessment, and determine whether "
        "any material uncertainty about the entity's ability to continue as a going concern exists, "
        "in accordance with SA 570 (Revised) and Ind AS 1."
    ),
    "risk_overview": (
        "ARWL's financial profile appears robust: PAT ₹301 Crores, strong AUM growth, net inflows ₹12,617 Crores, "
        "and management guidance of 20-25% PAT growth. However, going concern must still be formally assessed. "
        "Potential stress factors: AUM is equity market-linked (30% market decline = ~30% AUM decline = significant trail income impact), "
        "SEBI regulatory actions, concentration in equity MF distribution, and interest rate risk on debt products."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Formal Going Concern Evaluation",
            "risk": "Even if financial performance appears strong, going concern assessment cannot be bypassed. Regulatory sanctions or business model disruption could rapidly change the picture.",
            "procedure": (
                "Step 1A – Assess going concern indicators (Ind AS 1 Para 25-26 and SA 570 Para 10):\n"
                "Financial indicators: Net liability position? Loan defaults? Negative operating cash flows? "
                "Inability to pay dividends? Large operating losses?\n"
                "Operating indicators: Loss of key licenses (AMFI registration, SEBI certificate)? Key management departure? "
                "Loss of significant AMC relationships? Regulatory sanctions affecting business?\n"
                "Other indicators: Changes in regulations eliminating revenue model? Pending major litigation?\n\n"
                "Step 1B – For ARWL-specific risk: Perform a stress-test analysis: "
                "(i) If Nifty 50 falls 30% from current level → AUM falls proportionately → Trail income falls proportionately. "
                "(ii) Compute break-even AUM level = fixed costs / trail commission rate. "
                "(iii) Assess adequacy of capital buffer to sustain operations if revenue contracts significantly.\n\n"
                "Step 1C – Review SEBI regulatory posture: Any pending show cause notices or investigations could materially "
                "affect ARWL's license to operate."
            ),
            "assertions": ["P&D", "VAL"],
            "sa_ref": "SA 570 Para 10, 11, 12 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.13, S.24",
        },
        {
            "no": 2,
            "category": "Management Assessment Review",
            "risk": "Management's going concern assessment may be overly optimistic and not adequately challenged.",
            "procedure": (
                "Step 2A – Obtain management's formal going concern assessment covering at least 12 months from 31 March 2026 "
                "(i.e., assessment must cover period to at least 31 March 2027).\n\n"
                "Step 2B – Review the cash flow projections supporting management's assessment: "
                "(i) Test the mathematical accuracy of the projections. "
                "(ii) Assess the reasonableness of revenue growth assumptions (is 20-25% PAT growth realistic given market conditions?). "
                "(iii) Assess the sensitivity of the projections to adverse scenarios. "
                "(iv) Verify that all significant outflows (dividends, tax, capital expenditure, loan repayments) are included.\n\n"
                "Step 2C – Assess whether management has considered all available information up to the date of auditor's report. "
                "Ask management: Are there any post-balance-sheet events that could affect going concern?\n\n"
                "Step 2D – Inquire of legal counsel and SEBI compliance team on any regulatory matters that could threaten operations."
            ),
            "assertions": ["P&D", "VAL"],
            "sa_ref": "SA 570 Para 13, 14, 16 | SA 560 Para 6",
            "kkc_ref": "KKC Manual S.24, S.43",
        },
        {
            "no": 3,
            "category": "Conclusion & Reporting Implications",
            "risk": "Incorrect conclusion on going concern may result in an inappropriate audit opinion.",
            "procedure": (
                "Step 3A – Based on all evidence, conclude: "
                "(i) Going concern assumption is appropriate – no material uncertainty → Verify Ind AS 1 disclosure note is present. "
                "(ii) Material uncertainty exists but adequately disclosed → Include Emphasis of Matter paragraph (SA 706 Para 6(a)). "
                "(iii) Material uncertainty exists but not adequately disclosed → Qualified or Adverse opinion (SA 705).\n\n"
                "Step 3B – Obtain written representation from management confirming their assessment of going concern "
                "and that they are not aware of any matters that would affect the ability to continue (SA 580).\n\n"
                "Step 3C – Document reasoning in Conclusion Memorandum. "
                "NFRA requires specific evidence supporting the going concern conclusion, not a standard paragraph."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SA 570 Para 18, 19, 20, 21, 22, 23 | SA 706 Para 6 | SA 705 Para 7",
            "kkc_ref": "KKC Manual S.24, S.47, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Leases (Ind AS 116)": {
    "objective": (
        "To verify that all lease arrangements are identified and correctly classified, Right-of-Use (ROU) Assets "
        "and Lease Liabilities are completely and accurately measured and recognised, modifications are properly accounted, "
        "and all required disclosures per Ind AS 116 are made."
    ),
    "risk_overview": (
        "ARWL has significant office space in Mumbai (Lower Parel, Goregaon), other cities, and Dubai. "
        "All these are likely operating leases now on-balance sheet under Ind AS 116. "
        "Key risks: incomplete lease identification, incorrect Incremental Borrowing Rate (IBR), "
        "lease term estimation (renewal options), and incorrect treatment of lease incentives."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Completeness – Lease Register",
            "risk": "Leases may be incompletely identified, particularly embedded leases in service contracts.",
            "procedure": (
                "Step 1A – Obtain the Lease Register maintained by management listing all leases with: "
                "asset description, lessor, commencement date, lease term, monthly rental, "
                "renewal options, IBR used, ROU Asset, and Lease Liability.\n\n"
                "Step 1B – Cross-verify with: (i) Fixed asset register (all office premises should have ROU entries). "
                "(ii) Rental expense account – any remaining rent expenses should be only for short-term/low-value leases. "
                "(iii) Board-approved office locations list.\n\n"
                "Step 1C – Review all service and outsourcing contracts for embedded lease components "
                "(e.g. dedicated server space, dedicated vehicle, dedicated equipment). "
                "Per Ind AS 116 Para 9: if a contract contains a lease component and non-lease component, account for separately.\n\n"
                "Step 1D – Identify leases that qualify for recognition exemptions: "
                "(i) Short-term (lease term ≤ 12 months, including renewal option) – expense on straight-line. "
                "(ii) Low-value assets (underlying asset value < USD 5,000 when new) – expense on straight-line. "
                "Verify that management's classification is correct."
            ),
            "assertions": ["COM", "EXI"],
            "sa_ref": "SA 315 Para 11 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.8, S.27",
        },
        {
            "no": 2,
            "category": "Measurement of ROU Asset & Lease Liability",
            "risk": "Incorrect IBR or lease term assumption leads to material misstatement of both ROU Asset and Lease Liability.",
            "procedure": (
                "Step 2A – Lease term determination: "
                "(i) Verify lease term = non-cancellable period + optional renewal periods if 'reasonably certain' to exercise. "
                "(ii) For ARWL's primary offices – given business continuity requirements, renewal is likely 'reasonably certain'. "
                "(iii) Document the basis for including or excluding renewal periods.\n\n"
                "Step 2B – IBR assessment: "
                "(i) IBR is the rate ARWL would pay to borrow funds for a similar term with similar security. "
                "(ii) Obtain management's IBR assessment for each lease. "
                "(iii) Benchmark: Compare with ARWL's actual borrowing rates or prevailing secured loan rates for similar tenure. "
                "(iv) IBR should be updated only on lease modification or reassessment – not annually. "
                "Verify management is not updating IBR when not required.\n\n"
                "Step 2C – For a sample of 5 leases (covering top 80% of ROU Asset): "
                "Independently build the lease liability amortisation table in Excel: "
                "Opening balance + Interest (IBR × opening balance) – Lease payment = Closing balance. "
                "Agree closing lease liability to balance sheet.\n\n"
                "Step 2D – Verify ROU Asset = Initial Lease Liability + Initial Direct Costs + Prepaid Lease Payments "
                "– Lease Incentives Received (e.g. rent-free periods, fit-out contributions from lessor).\n\n"
                "Step 2E – Verify depreciation: ROU Asset depreciated on straight-line over shorter of lease term or useful life of underlying asset."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 8 | SA 500 Para 7",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "Lease Modifications & Reassessments",
            "risk": "Lease modifications or reassessment events may not be correctly accounted, leading to incorrect Lease Liability and ROU Asset.",
            "procedure": (
                "Step 3A – Identify any lease modifications in FY 2025-26: rent renegotiations, extensions, early terminations, expansions.\n\n"
                "Step 3B – For each modification: "
                "(i) If modification increases scope at separate price: treat as new lease (derecognise modified portion). "
                "(ii) Other modifications: remeasure Lease Liability at revised IBR; adjust ROU Asset.\n\n"
                "Step 3C – Identify reassessment events: "
                "(i) Change in lease term (exercising or not exercising renewal/termination option). "
                "(ii) Change in variable lease payments based on market review. "
                "Verify remeasurement at date of reassessment.\n\n"
                "Step 3D – Lease terminations: "
                "Verify gain/loss on termination = Carrying amount of Lease Liability – Carrying amount of ROU Asset at termination date. "
                "Agree to P&L."
            ),
            "assertions": ["VAL", "COF"],
            "sa_ref": "SA 540 Para 8 | SA 560 Para 6",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 4,
            "category": "Disclosures – Ind AS 116",
            "risk": "Ind AS 116 requires extensive quantitative and qualitative disclosures which are frequently incomplete.",
            "procedure": (
                "Step 4A – Verify ROU Asset rollforward: opening + additions – depreciation – disposals – impairment = closing. By class of asset.\n\n"
                "Step 4B – Verify Lease Liability maturity analysis: undiscounted cash flows < 1 year, 1-5 years, > 5 years.\n\n"
                "Step 4C – Verify P&L amounts: depreciation of ROU, interest on lease liability, short-term lease expense, "
                "variable lease payments not included in lease liability, income from sub-leasing.\n\n"
                "Step 4D – Verify cash flow statement: principal repayment of lease liability (financing activity), "
                "interest on lease liability (financing or operating activity per accounting policy).\n\n"
                "Step 4E – Verify qualitative disclosures: nature of leasing activities, "
                "significant assumptions and judgements (lease term, IBR), extension and termination options."
            ),
            "assertions": ["P&D", "COM"],
            "sa_ref": "SA 700 Para 13 | SA 330 Para 20",
            "kkc_ref": "KKC Manual S.46",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Fixed Assets & Intangibles": {
    "objective": (
        "To obtain sufficient appropriate audit evidence that tangible fixed assets (PPE) and intangible assets "
        "are completely recorded, exist, are owned by the entity, correctly valued and depreciated/amortised, "
        "no impairment is unrecognised, and disclosures comply with Ind AS 16, Ind AS 38, and CARO 2020."
    ),
    "risk_overview": (
        "ARWL's tangible assets include office furniture, IT equipment, servers, and leasehold improvements. "
        "Intangibles may include software, proprietary technology platform, and customer-related intangibles. "
        "Risks: overstatement through incorrect capitalisation of revenue expenditure, "
        "insufficient depreciation/amortisation, unrecognised impairment on proprietary technology, "
        "and non-compliance with CARO physical verification requirements."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Fixed Asset Register & Opening Balance",
            "risk": "Opening balances may not correctly roll forward from prior year audited figures.",
            "procedure": (
                "Step 1A – Agree opening gross block and accumulated depreciation per FAR to prior year closing balances (audited).\n\n"
                "Step 1B – Agree total closing gross block and NBV to balance sheet PPE and intangible asset note.\n\n"
                "Step 1C – Verify the FAR is maintained with adequate details: "
                "asset description, location, purchase date, cost, useful life, depreciation method, cumulative depreciation, NBV, "
                "and disposal date (if applicable).\n\n"
                "Step 1D – For additions: Select items > ₹5 lakhs individually and verify: "
                "(i) Purchase order / sanction. "
                "(ii) Invoice from supplier. "
                "(iii) Goods received note / installation certificate. "
                "(iv) Asset put-to-use date (depreciation commences). "
                "(v) Confirm asset meets capitalisation criteria under Ind AS 16."
            ),
            "assertions": ["EXI", "COM", "R&O"],
            "sa_ref": "SA 500 Para 7 | SA 501 Para 4",
            "kkc_ref": "KKC Manual S.27, S.44",
        },
        {
            "no": 2,
            "category": "Physical Verification",
            "risk": "Assets may be recorded but not physically exist, or may be damaged/obsolete without adequate impairment.",
            "procedure": (
                "Step 2A – Obtain management's physical verification report for the year. "
                "CARO 2020 Clause 3(i)(b) requires physical verification to be carried out at reasonable intervals.\n\n"
                "Step 2B – Assess adequacy of management's physical verification: Was it conducted by a responsible person? "
                "Were differences identified? Were differences reconciled?\n\n"
                "Step 2C – Perform independent spot verification: Select 10-15 assets from the FAR and physically verify their existence. "
                "Confirm: asset is at the location stated in FAR, is in usable condition, and matches description.\n\n"
                "Step 2D – Identify assets in FAR that cannot be physically located or are damaged/obsolete – "
                "assess whether write-off or impairment is required."
            ),
            "assertions": ["EXI", "VAL"],
            "sa_ref": "SA 501 Para 4 | CARO 2020 Cl.3(i)(b)",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 3,
            "category": "Capitalisation vs Expense Boundary",
            "risk": "Revenue expenses may be incorrectly capitalised (overstatement of assets), or capital expenditure may be expensed (understatement of assets and overstatement of expenses).",
            "procedure": (
                "Step 3A – Review the repairs and maintenance expense account. "
                "Scan for items > ₹2 lakhs that may meet capitalisation criteria (enhancing future economic benefits).\n\n"
                "Step 3B – Review technology expenses: "
                "(i) Software development costs: Apply Ind AS 38 criteria – research phase expensed, development phase capitalised when criteria met. "
                "(ii) Verify management has documented which phase each project is in. "
                "(iii) SaaS / cloud subscriptions: Expense as incurred (per IFRIC interpretation). Do not capitalise.\n\n"
                "Step 3C – Leasehold improvements: "
                "(i) Verify improvements to leased offices are capitalised as PPE (not as lease assets). "
                "(ii) Verify useful life = shorter of improvement life or remaining lease term. "
                "(iii) Verify they are depreciated separately from ROU Asset."
            ),
            "assertions": ["OCC", "CLA", "VAL"],
            "sa_ref": "SA 500 Para 7 | SA 315 Para 11",
            "kkc_ref": "KKC Manual S.27",
        },
        {
            "no": 4,
            "category": "Depreciation & Useful Life Review",
            "risk": "Incorrect depreciation rates or useful life assumptions overstate or understate net book values.",
            "procedure": (
                "Step 4A – Verify depreciation policy is consistent with prior year. If changed, Ind AS 8 requires disclosure.\n\n"
                "Step 4B – Recompute depreciation for a sample of 15 assets: "
                "Depreciation = (Cost – Residual Value) × Rate × Days/365. "
                "Verify rate applied consistent with: (i) Useful life per management's assessment, "
                "(ii) Companies Act Schedule II minimum useful life guidance.\n\n"
                "Step 4C – For intangible assets with indefinite useful life: "
                "Verify annual impairment test performed (Ind AS 38 Para 108). "
                "No indefinite-life intangible should be amortised – verify amortisation is zero.\n\n"
                "Step 4D – For intangibles with finite useful life: "
                "Verify amortisation is on straight-line basis over estimated useful life. "
                "Residual value assumed to be zero unless active market exists."
            ),
            "assertions": ["ACC", "VAL"],
            "sa_ref": "SA 500 Para 7 | SA 540 Para 8",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 5,
            "category": "CARO 2020 Reporting Requirements",
            "risk": "CARO reporting may be incomplete or inaccurate, leading to qualification in CARO report.",
            "procedure": (
                "Step 5A – CARO Clause 3(i)(a): Verify company maintains proper records of fixed assets including location details.\n\n"
                "Step 5B – CARO Clause 3(i)(b): Verify physical verification by management at reasonable intervals – "
                "document conclusion on whether interval is reasonable for entity's size and nature.\n\n"
                "Step 5C – CARO Clause 3(i)(c): For immovable properties (if any): verify title deeds held in company's name. "
                "Verify no properties held in names of directors or promoters (possible related-party asset).\n\n"
                "Step 5D – CARO Clause 3(i)(d): Verify whether any revaluation of PPE/intangibles was performed. "
                "If yes, obtain independent valuation and verify Ind AS 16 revaluation accounting."
            ),
            "assertions": ["P&D", "COM"],
            "sa_ref": "SA 700 Para 13 | CARO 2020 Cl.3(i)",
            "kkc_ref": "KKC Manual S.46, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"IT Application & ITGC Testing": {
    "objective": (
        "To understand ARWL's IT environment, assess IT-related risks arising from the use of IT, "
        "test General IT Controls (GITC) over relevant IT applications, and determine the impact of "
        "IT on the overall audit approach and reliance on automated controls, per SA 315 Para 19-22."
    ),
    "risk_overview": (
        "ARWL relies heavily on technology – a proprietary back-office system for AUM tracking, "
        "an automated commission calculation engine, a CRM, an ERP for accounting (Tally or similar), "
        "and a client-facing digital platform. Integration between these systems is a key risk area. "
        "NFRA has repeatedly flagged IT audit deficiencies: lack of IT environment documentation, "
        "no access control testing, and no automated control reliance testing."
    ),
    "steps": [
        {
            "no": 1,
            "category": "IT Environment Profiling",
            "risk": "Without a comprehensive IT environment profile, IT-related risks cannot be properly identified and audit procedures cannot be appropriately designed.",
            "procedure": (
                "Step 1A – Document the IT environment profile per KKC IT complexity matrix:\n"
                "(i) List all key IT applications: back-office AUM tracking system, commission calculation engine, "
                "ERP/Tally for accounting, HRMS for payroll, CRM, client portal.\n"
                "(ii) For each application: vendor, version, on-premise vs cloud-hosted, interfaces with other systems.\n"
                "(iii) IT infrastructure: server environment, network architecture, database platforms (SQL Server, Oracle).\n\n"
                "Step 1B – Data flows: Map the flow of transactions from initiation to financial statements:\n"
                "Client investment → Back-office system → AMC data feed → Commission calculation → Accounting system (JV) → General Ledger.\n"
                "Identify all automated journal entries, interfaces, and manual intervention points.\n\n"
                "Step 1C – Third-party service providers:\n"
                "(i) CAMS and KFintech – provide AUM data to ARWL. Assess risk of incorrect data input.\n"
                "(ii) If any system is cloud-hosted: obtain SSAE 18 SOC 1 Type II report (or ISAE 3402) from service provider.\n\n"
                "Step 1D – Assess IT complexity (low/medium/high). "
                "ARWL's multi-system environment with automated commission calculation = Medium to High complexity. "
                "Implication: ITGC testing is important for audit reliance on automated controls."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 315 Para 19, 20, 21, A87-A92",
            "kkc_ref": "KKC Manual S.9",
        },
        {
            "no": 2,
            "category": "Logical Access Controls",
            "risk": "Unauthorised access to systems allows unauthorised transactions, data manipulation, or program changes to go undetected.",
            "procedure": (
                "Step 2A – Access provisioning process: "
                "(i) Understand how access is granted: Is there a formal access request and approval process? "
                "(ii) Who approves access to accounting system? To commission calculation engine? To HRMS?\n\n"
                "Step 2B – User access review for each key system:\n"
                "(i) Obtain user access listing as at 31 March 2026.\n"
                "(ii) Verify each user's access level is appropriate for their role (least-privilege principle).\n"
                "(iii) Flag: users with excessive access (e.g. IT person with posting access in ERP).\n"
                "(iv) Flag: terminated employees with active access – run against HR termination list for the year.\n"
                "(v) Flag: users with both initiating and approving access (segregation of duties violation).\n\n"
                "Step 2C – Privileged access: "
                "(i) List all system administrator, database administrator, and super-user accounts.\n"
                "(ii) Verify these are limited to named IT personnel (not generic/shared accounts).\n"
                "(iii) Verify privileged access is subject to enhanced monitoring.\n\n"
                "Step 2D – Password policy: "
                "(i) Minimum length ≥ 8 characters, complexity requirements, expiry ≤ 90 days.\n"
                "(ii) Verify MFA (multi-factor authentication) is enabled for remote access and privileged accounts."
            ),
            "assertions": ["OCC", "R&O"],
            "sa_ref": "SA 315 Para 22 | SA 330 Para 8",
            "kkc_ref": "KKC Manual S.9",
        },
        {
            "no": 3,
            "category": "Change Management Controls",
            "risk": "Unauthorised system changes may introduce errors in financial calculations or create opportunities for fraud.",
            "procedure": (
                "Step 3A – Obtain the change log for all production system changes deployed in FY 2025-26 "
                "for key applications (commission system, ERP, HRMS).\n\n"
                "Step 3B – Verify change management process:\n"
                "(i) Change request documented and approved before development.\n"
                "(ii) Testing in non-production environment (UAT) before go-live.\n"
                "(iii) UAT sign-off by business owner (finance/operations).\n"
                "(iv) Independent deployment to production (developer ≠ deployer).\n"
                "(v) Post-implementation review for critical changes.\n\n"
                "Step 3C – For changes affecting commission calculation logic:\n"
                "(i) Obtain impact assessment document.\n"
                "(ii) Verify commission calculations before and after the change.\n"
                "(iii) Verify no commission calculation errors resulted from the change.\n\n"
                "Step 3D – Emergency/hotfix changes: "
                "Verify that even emergency changes went through expedited but documented approval. "
                "Any undocumented emergency changes = significant IT control deficiency."
            ),
            "assertions": ["ACC", "OCC"],
            "sa_ref": "SA 315 Para 22 | SA 330 Para 8",
            "kkc_ref": "KKC Manual S.9",
        },
        {
            "no": 4,
            "category": "Application Controls – Commission Calculation Engine",
            "risk": "Errors in automated commission calculations directly impact revenue accuracy for the entire year.",
            "procedure": (
                "Step 4A – Understand the commission calculation algorithm: "
                "(i) How does the system receive AUM data (from CAMS/KFintech feed)?\n"
                "(ii) How are commission rates applied (from rate table in the system)?\n"
                "(iii) How is the commission per client / per scheme computed?\n"
                "(iv) How are results transferred to the accounting system (automated JV or manual upload)?\n\n"
                "Step 4B – Test automated calculations:\n"
                "(i) Select a sample of 20 commission calculations from the system.\n"
                "(ii) Independently compute expected commission = AUM × Rate × Days/365.\n"
                "(iii) Compare system output with manual computation.\n"
                "(iv) Investigate differences – system errors, rate table errors, or AUM feed errors.\n\n"
                "Step 4C – Interface testing – AUM data from CAMS/KFintech:\n"
                "(i) Agree sample of AUM figures in commission system with CAMS/KFintech statement.\n"
                "(ii) Verify interface completeness – no AUM data dropped in transmission.\n"
                "(iii) Verify reconciliation is performed between CAMS/KFintech data and system data."
            ),
            "assertions": ["OCC", "ACC", "COM"],
            "sa_ref": "SA 315 Para 21 | SA 330 Para 8, 10",
            "kkc_ref": "KKC Manual S.9",
        },
        {
            "no": 5,
            "category": "IT Operations Controls",
            "risk": "System outages, data loss, or backup failures may result in incomplete or inaccurate financial records.",
            "procedure": (
                "Step 5A – Backup and recovery:\n"
                "(i) Verify backup policy: frequency (daily backup minimum), type (full + incremental), storage location (offsite).\n"
                "(ii) Verify at least one backup restoration test was performed during the year.\n"
                "(iii) Obtain backup logs to verify backups completed without error.\n\n"
                "Step 5B – System availability: "
                "Review incident log for system outages during the year. "
                "Any extended outage during month-end periods is a risk. "
                "Verify manual workarounds used during outages were properly reflected in books.\n\n"
                "Step 5C – Data integrity: "
                "Verify reconciliations performed between source systems and general ledger:\n"
                "(i) Commission system revenue → GL revenue account.\n"
                "(ii) HRMS payroll → GL payroll expense.\n"
                "(iii) FAR depreciation → GL depreciation expense."
            ),
            "assertions": ["COM", "ACC"],
            "sa_ref": "SA 315 Para 22",
            "kkc_ref": "KKC Manual S.9",
        },
        {
            "no": 6,
            "category": "Audit Trail Testing – Rule 11(g) Compliance",
            "risk": "Non-compliance with mandatory audit trail requirements constitutes a reportable matter in CARO 2020 and may indicate control weakness.",
            "procedure": (
                "Step 6A – Per Rule 11(g) of Companies (Audit and Auditors) Rules (effective from April 2023): "
                "The accounting software must have an audit trail feature that:\n"
                "(i) Records changes to books of account (who made, when, what was changed).\n"
                "(ii) Cannot be disabled.\n"
                "(iii) Audit trail is not tampered with.\n\n"
                "Step 6B – Test procedures:\n"
                "(i) Obtain evidence that the audit trail feature is enabled in the accounting software.\n"
                "(ii) Attempt to make a test entry and verify it is captured in the audit trail.\n"
                "(iii) Verify that the audit trail cannot be disabled by any user (including administrators).\n"
                "(iv) Obtain a sample extract of the audit trail and verify it captures user ID, timestamp, and before/after values.\n\n"
                "Step 6C – Verify preservation of audit trail: "
                "Must be preserved for the same period as books of account (8 years for companies).\n\n"
                "Step 6D – Document findings for inclusion in CARO 2020 Clause 3(vi) report. "
                "If audit trail not maintained for any part of the year, CARO must report this fact."
            ),
            "assertions": ["OCC", "COM"],
            "sa_ref": "SA 315 Para 22 | CARO 2020 Cl.3(vi) | Rule 11(g)",
            "kkc_ref": "KKC Manual S.9, S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"SEBI LODR & Statutory Compliance": {
    "objective": (
        "To assess whether ARWL, as a listed entity, complies with key provisions of SEBI LODR "
        "Regulations 2015 relevant to audit reporting, and to verify compliance with other statutory requirements "
        "under Companies Act 2013 that are reportable under SA 250 and CARO 2020."
    ),
    "risk_overview": (
        "ARWL is listed on both NSE and BSE. Non-compliance with SEBI LODR can result in penalties, trading suspension, "
        "and reputational damage. Prior SEBI penalty adds to compliance sensitivity. "
        "Key compliance areas: quarterly financial reporting, RPT disclosures, corporate governance report, "
        "insider trading regulations, and listing agreement covenants."
    ),
    "steps": [
        {
            "no": 1,
            "category": "SEBI LODR – Financial Reporting Compliance",
            "risk": "Quarterly financial results filed with stock exchanges may not reconcile with annual audited figures.",
            "procedure": (
                "Step 1A – Obtain quarterly financial results filed with NSE/BSE under SEBI LODR Regulation 33 for Q1, Q2, Q3, Q4.\n\n"
                "Step 1B – Agree: Sum of Q1+Q2+Q3+Q4 = Annual figures for: Revenue, EBITDA, PAT, EPS.\n\n"
                "Step 1C – Verify limited review for Q1, Q2, Q3 was conducted. Obtain copies of the limited review reports.\n\n"
                "Step 1D – Verify Q4 and annual audit reports were filed within the prescribed timelines: "
                "Annual results within 60 days of end of financial year (by 31 May 2026).\n\n"
                "Step 1E – Verify format of financial results complies with latest SEBI circular on quarterly results format."
            ),
            "assertions": ["ACC", "COM", "P&D"],
            "sa_ref": "SA 250 Para 14 | SEBI LODR Reg. 33",
            "kkc_ref": "KKC Manual S.48",
        },
        {
            "no": 2,
            "category": "Corporate Governance Compliance",
            "risk": "Non-compliance with board composition, audit committee requirements, or mandatory declarations may constitute a LODR violation.",
            "procedure": (
                "Step 2A – Verify board composition per SEBI LODR Regulation 17: "
                "Minimum 6 directors, at least 50% independent directors, at least 1 woman director.\n\n"
                "Step 2B – Verify Audit Committee composition per LODR Reg. 18: "
                "Minimum 3 directors, majority independent, chairperson independent, at least one with financial/accounting expertise.\n\n"
                "Step 2C – Verify Nomination & Remuneration Committee and Stakeholders Relationship Committee composition per LODR Reg. 19, 20.\n\n"
                "Step 2D – Verify Corporate Governance Report (Annexure to Directors' Report) covers all mandatory disclosures per LODR Reg. 34(3) and Schedule V.\n\n"
                "Step 2E – Verify CEO/CFO certification per LODR Reg. 17(8) was submitted to Board."
            ),
            "assertions": ["COM", "P&D"],
            "sa_ref": "SA 250 Para 14 | SEBI LODR",
            "kkc_ref": "KKC Manual S.48",
        },
        {
            "no": 3,
            "category": "Companies Act – Directors' Report & Auditor's Report",
            "risk": "Directors' Report may omit mandatory disclosures, or Auditor's Report may not address all Section 143(3) requirements.",
            "procedure": (
                "Step 3A – Review Directors' Report for completeness of mandatory disclosures under Companies Act 2013:\n"
                "(i) Extract of Annual Return (Sec 92). "
                "(ii) Board meetings held. "
                "(iii) Directors' Responsibility Statement (Sec 134(5)). "
                "(iv) Audit Committee observations. "
                "(v) CSR report (Sec 135). "
                "(vi) Vigil Mechanism / Whistle Blower Policy.\n\n"
                "Step 3B – Verify Auditor's Report covers all Section 143(3) requirements including:\n"
                "(i) Whether books of accounts are maintained. "
                "(ii) Balance sheet / P&L is in agreement with books. "
                "(iii) Auditor's observations / qualifications.\n\n"
                "Step 3C – Verify CARO 2020 report covers all applicable clauses. "
                "Review each CARO clause and ensure the response is accurate and consistent with audit findings."
            ),
            "assertions": ["COM", "P&D"],
            "sa_ref": "SA 700 Para 13 | Companies Act S.143(3)",
            "kkc_ref": "KKC Manual S.48",
        },
        {
            "no": 4,
            "category": "BRSR (Business Responsibility & Sustainability Report)",
            "risk": "BRSR disclosures may be inaccurate or inconsistent with financial data, creating reputational and regulatory risk.",
            "procedure": (
                "Step 4A – ARWL's Annual Report includes BRSR. As auditor, verify accuracy of BRSR data that overlaps with "
                "financial statements: headcount, employee costs, tax paid, energy consumption costs.\n\n"
                "Step 4B – Verify BRSR disclosures are consistent with: financial statements, CARO report, and HR data.\n\n"
                "Step 4C – Verify BRSR is submitted as per SEBI LODR Regulation 34(2)(f) requirements for top 1000 listed entities."
            ),
            "assertions": ["P&D", "ACC"],
            "sa_ref": "SA 700 Para 13 | SEBI LODR Reg. 34",
            "kkc_ref": "KKC Manual S.48",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Audit Completion & Reporting": {
    "objective": (
        "To complete all audit procedures, evaluate misstatements, perform subsequent event procedures, "
        "obtain written representations, communicate with TCWG, and form and express an appropriate audit "
        "opinion on the financial statements per SA 700, SA 701, SA 705, and SA 706."
    ),
    "risk_overview": (
        "Completion procedures ensure no matter remains unaddressed before report issuance. "
        "For a listed entity like ARWL, SA 701 (Key Audit Matters), EQCR, and NFRA documentation requirements "
        "add significant completion requirements. NFRA inspection reports consistently identify completion "
        "deficiencies: EQCR conducted after report, KAMs described generically, and inadequate documentation."
    ),
    "steps": [
        {
            "no": 1,
            "category": "Subsequent Events Review",
            "risk": "Events after 31 March 2026 may require adjustment or disclosure in the financial statements.",
            "procedure": (
                "Step 1A – Obtain and read board minutes for all meetings from 01 April 2026 to the date of auditor's report.\n\n"
                "Step 1B – Inquire of management about subsequent events:\n"
                "(i) New or unusual business developments.\n"
                "(ii) Major changes in AUM or client base.\n"
                "(iii) New significant borrowings or repayments.\n"
                "(iv) Regulatory actions or penalties.\n"
                "(v) Significant litigation judgements.\n"
                "(vi) Major acquisitions, disposals, or restructuring.\n\n"
                "Step 1C – Classify events:\n"
                "(i) Adjusting events (Ind AS 10 Para 9): Confirm/refute conditions existing at balance sheet date → Adjust financial statements.\n"
                "(ii) Non-adjusting events (Ind AS 10 Para 10): Conditions arose after balance sheet date → Disclose if material.\n\n"
                "Step 1D – ARWL-specific: Verify that the recommendation of final dividend (₹7/share on post-bonus capital) "
                "by Board post 31 March 2026 is disclosed as non-adjusting subsequent event (not as a liability in balance sheet).\n\n"
                "Step 1E – Review interim financial information (if available) for any unusual trends."
            ),
            "assertions": ["COM", "P&D"],
            "sa_ref": "SA 560 Para 6, 7, 9, 10 | Ind AS 10",
            "kkc_ref": "KKC Manual S.43",
        },
        {
            "no": 2,
            "category": "Evaluation & Aggregation of Misstatements",
            "risk": "Individually immaterial misstatements may aggregate to a material amount, or management may resist correcting misstatements within performance materiality.",
            "procedure": (
                "Step 2A – Compile the schedule of unadjusted misstatements from all audit areas (both factual and projected).\n\n"
                "Step 2B – Assess aggregate of unadjusted misstatements against performance materiality. "
                "If aggregate exceeds performance materiality, request management to correct all items or perform additional procedures.\n\n"
                "Step 2C – Communicate all misstatements to management and request correction. "
                "Document management's response for each item.\n\n"
                "Step 2D – For misstatements management refuses to correct:\n"
                "(i) Obtain management's reasons in writing.\n"
                "(ii) Evaluate whether the misstatement is material (individually or in aggregate).\n"
                "(iii) If material and uncorrected → modify opinion (SA 705).\n\n"
                "Step 2E – Assess misstatements for indicators of bias: "
                "Do uncorrected misstatements consistently overstate revenue or understate expenses? "
                "Pattern of management bias → reassess risk of material misstatement."
            ),
            "assertions": ["OCC", "COM", "ACC", "VAL"],
            "sa_ref": "SA 450 Para 5, 8, 10, 12 | SA 320 Para 10",
            "kkc_ref": "KKC Manual S.45",
        },
        {
            "no": 3,
            "category": "Written Representations (MRL)",
            "risk": "Without adequate management representations, the auditor lacks written acknowledgement of management's responsibilities.",
            "procedure": (
                "Step 3A – Prepare Management Representation Letter (MRL) to be dated same as auditor's report. "
                "Obtain signatures from CEO and CFO.\n\n"
                "Step 3B – MRL must include representations on:\n"
                "(i) Management's responsibility for preparation of financial statements (SA 580 Para 10).\n"
                "(ii) All relevant information provided to the auditor.\n"
                "(iii) All transactions recorded and reflected in financial statements.\n"
                "(iv) No known fraud or suspected fraud involving management or employees.\n"
                "(v) All related parties and RPTs identified and disclosed.\n"
                "(vi) Compliance with laws and regulations.\n"
                "(vii) Going concern assumption is appropriate.\n"
                "(viii) All actual and contingent liabilities disclosed.\n"
                "(ix) No events between balance sheet date and MRL date that would affect financial statements.\n\n"
                "Step 3C – Per NFRA requirements: If the MRL is not signed by the date of the audit report, "
                "the engagement partner must not sign the audit report. "
                "Obtain MRL before finalising the opinion."
            ),
            "assertions": ["OCC", "COM", "P&D"],
            "sa_ref": "SA 580 Para 10, 11, 14, 16 | SA 240 Para 39",
            "kkc_ref": "KKC Manual S.47",
        },
        {
            "no": 4,
            "category": "Communication with TCWG (Audit Committee)",
            "risk": "Required communications to the Audit Committee may be omitted or provided informally without adequate documentation.",
            "procedure": (
                "Step 4A – Prepare formal written communication to Audit Committee per SA 260 covering:\n"
                "(i) Auditor's responsibilities under SAs.\n"
                "(ii) Planned scope and timing – any changes from initial plan.\n"
                "(iii) Significant risks identified and audit response.\n"
                "(iv) Key Audit Matters proposed for SA 701 report.\n"
                "(v) Significant accounting policies adopted and management judgements.\n"
                "(vi) Significant difficulties encountered during audit (if any).\n"
                "(vii) All significant findings and proposed adjustments.\n"
                "(viii) Internal control deficiencies identified per SA 265.\n\n"
                "Step 4B – Ensure communication is in writing (not just verbal presentation).\n\n"
                "Step 4C – Obtain and document Audit Committee's response, including decisions taken.\n\n"
                "Step 4D – SA 265: If any significant deficiencies in internal controls identified, "
                "communicate in writing to TCWG and management. Verify deficiencies are disclosed in CARO if required."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SA 260 Para 10, 12, 14, 15 | SA 265 Para 9",
            "kkc_ref": "KKC Manual S.46, S.47",
        },
        {
            "no": 5,
            "category": "Key Audit Matters – SA 701",
            "risk": "KAMs may be described generically without entity-specific content, violating SA 701 requirements and attracting NFRA scrutiny.",
            "procedure": (
                "Step 5A – Identify KAMs from: (i) Areas with highest assessed risk of material misstatement, "
                "(ii) Areas requiring significant management judgement, (iii) Effect of significant events or transactions.\n\n"
                "Step 5B – Proposed KAMs for ARWL FY 2025-26:\n"
                "(i) Revenue Recognition – Trail Commission: Given materiality, complexity of AUM-linked calculation, and volume. "
                "Describe: what the matter is, why it was significant, how the audit addressed it (specific procedures, evidence obtained).\n"
                "(ii) Defined Benefit Obligation – Actuarial Valuation: "
                "Sensitivity to discount rate and attrition rate assumptions, use of management's actuary.\n"
                "(iii) IT Systems and Automated Commission Calculation: "
                "Reliance on automated calculations; ITGC weaknesses if any.\n\n"
                "Step 5C – Draft each KAM in the prescribed format:\n"
                "(i) Heading: Name of the KAM.\n"
                "(ii) Why the matter was determined to be a KAM.\n"
                "(iii) How the matter was addressed in the audit (specific procedures, not generic).\n"
                "(iv) Reference to relevant disclosures in financial statements.\n\n"
                "Step 5D – NFRA requirement: KAM descriptions must be entity-specific. "
                "Generic language copied from templates will not meet NFRA standards. "
                "Partner must personally review all KAM drafts."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SA 701 Para 9, 10, 11 | SA 260 Para 10",
            "kkc_ref": "KKC Manual S.48",
        },
        {
            "no": 6,
            "category": "EQCR – Engagement Quality Control Review",
            "risk": "EQCR performed after report issuance is a significant NFRA finding. The review must be completed before the report is signed.",
            "procedure": (
                "Step 6A – Assign EQCR reviewer: Must be a partner not involved in the engagement, "
                "with sufficient seniority and financial services experience. "
                "EQCR cannot be performed by Engagement Partner or team members.\n\n"
                "Step 6B – EQCR scope for listed entity (per SQC 1):\n"
                "(i) Significant judgements made by engagement team.\n"
                "(ii) Conclusions reached on significant risks.\n"
                "(iii) Proposed audit opinion and suitability.\n"
                "(iv) Whether financial statements are free from material misstatement.\n"
                "(v) KAMs – appropriateness of identification and description.\n\n"
                "Step 6C – EQCR documentation: EQCR reviewer must document:\n"
                "(i) Procedures performed during EQCR.\n"
                "(ii) Date EQCR completed (must be before audit report date).\n"
                "(iii) Any significant matters raised and how they were resolved.\n\n"
                "Step 6D – NFRA critical requirement: Report must NOT be dated until EQCR is complete. "
                "Any report dated before EQCR completion = serious quality management violation."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SQC 1 Para 60-66 | SA 220 Para 19, 20",
            "kkc_ref": "KKC Manual S.6",
        },
        {
            "no": 7,
            "category": "Audit Documentation – SA 230",
            "risk": "NFRA inspections frequently identify that audit documentation does not support conclusions reached. Documentation must demonstrate 'experienced auditor' standard.",
            "procedure": (
                "Step 7A – Per SA 230 Para 8: Audit documentation must be sufficient for an experienced auditor "
                "(with no prior connection to the audit) to understand: "
                "(i) Nature, timing, and extent of audit procedures. "
                "(ii) Results of those procedures and evidence obtained. "
                "(iii) Significant matters identified and conclusions reached.\n\n"
                "Step 7B – Engagement partner review of all workpapers before report sign-off:\n"
                "(i) Each workpaper is adequately cross-referenced.\n"
                "(ii) Conclusions are clearly stated and supported by evidence.\n"
                "(iii) Significant matters are documented in conclusion memoranda, not just noted in passing.\n\n"
                "Step 7C – Complete final assembly of audit file within 60 days of report date (SA 230 Para 14). "
                "After final assembly, no deletion of documentation is permitted.\n\n"
                "Step 7D – NFRA requirement: "
                "Working papers must show real auditor thought process – not template-filled documents. "
                "Differences of opinion, resolution of significant issues, and changes in approach must be documented."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SA 230 Para 8, 10, 14 | SA 220 Para 24",
            "kkc_ref": "KKC Manual S.5",
        },
    ],
},

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"NFRA Inspection Focus Areas": {
    "objective": (
        "To specifically address the recurring deficiencies identified by the National Financial Reporting Authority "
        "(NFRA) in its published Audit Quality Inspection Reports on audit firms (2021-2024 cycles), "
        "and build specific procedures to ensure ARWL's statutory audit meets NFRA's quality expectations."
    ),
    "risk_overview": (
        "NFRA has published inspection reports inspecting Big-4 and large domestic audit firms. "
        "Common themes include: SA 315 risk assessment deficiencies, SA 540 estimate testing gaps, "
        "SA 701 generic KAMs, SA 230 documentation failures, independence violations, EQCR timing failures, "
        "revenue fraud risk rebuttals without adequate basis, and IT audit deficiencies. "
        "These are applicable to any statutory audit of a listed company. "
        "KKC must proactively address these areas to ensure audit quality and regulatory compliance."
    ),
    "steps": [
        {
            "no": 1,
            "category": "NFRA Finding: Risk Assessment (SA 315) Deficiencies",
            "risk": "NFRA has found that engagement teams document risk assessment as a compliance exercise rather than as a genuine analytical process, resulting in risks being missed or misassessed.",
            "procedure": (
                "Step 1A – Ensure Risk Assessment and Planning Discussion (RAPD) is a genuine substantive discussion, not a template exercise. "
                "NFRA inspectors specifically look for: evidence of discussion, differing views considered, and conclusion documented with reasoning.\n\n"
                "Step 1B – Risk assessment must be at the assertion level for each FSLI. "
                "It is not sufficient to say 'risk is high for Revenue' – the team must identify which specific assertions "
                "(Occurrence? Completeness? Accuracy? Cut-off?) are at risk and why.\n\n"
                "Step 1C – Walkthroughs must be documented in sufficient detail: "
                "Process description, controls identified, documents sighted, and control effectiveness assessment.\n\n"
                "Step 1D – IT environment must be documented per SA 315 Para 19-22. "
                "NFRA has found that engagement teams treat IT as a black box. "
                "Identify each IT application, its function, interfaces, and risks arising from its use.\n\n"
                "Step 1E – Document that IT risks arising from use of IT have been identified and included in the risk assessment matrix."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 315 Para 5, 10, 11, 13, 19, 21, 22, 25, 26, 27, 28",
            "kkc_ref": "KKC Manual S.9, S.10, S.17",
        },
        {
            "no": 2,
            "category": "NFRA Finding: Accounting Estimates (SA 540) Testing Gaps",
            "risk": "NFRA inspections found that auditors accept management's estimates without independent verification and do not develop an auditor's own estimate.",
            "procedure": (
                "Step 2A – For every significant estimate: "
                "Prepare a documented assessment of: (i) the estimation method, (ii) data sources, "
                "(iii) key assumptions, (iv) sensitivity analysis.\n\n"
                "Step 2B – Develop the auditor's own independent estimate for all high-risk accounting estimates. "
                "NFRA requires this to be documented as an independent exercise, not just a review of management's computation.\n\n"
                "Step 2C – For actuarial valuations: "
                "Do not simply review the actuary's report. "
                "Independently assess: discount rate (compare with market rates), attrition rate (compare with actual employee data), "
                "salary growth (compare with actual increment history).\n\n"
                "Step 2D – Document the comparison between management's estimate and auditor's range. "
                "If management's estimate is within the auditor's range, document why it is acceptable. "
                "If outside, document the additional procedures performed."
            ),
            "assertions": ["VAL", "ACC"],
            "sa_ref": "SA 540 Para 8, 9, 10, 13, 14, 15, 16, 20",
            "kkc_ref": "KKC Manual S.35",
        },
        {
            "no": 3,
            "category": "NFRA Finding: Key Audit Matters – Generic Descriptions",
            "risk": "NFRA has found KAMs that are not entity-specific, do not describe how the auditor specifically addressed the matter, and appear to be copied from prior year or templates.",
            "procedure": (
                "Step 3A – Each KAM must describe: "
                "(i) Why it was the most significant in the audit (entity-specific reason, not generic). "
                "(ii) Exactly how the auditor addressed it – specific procedures, not 'we performed substantive procedures'.\n\n"
                "Step 3B – ARWL-specific KAM language examples:\n"
                "(i) Revenue – trail commission: Reference AUM of ₹77,103 Crores, 30% growth, "
                "specific testing of AMC-wise commission with named AMCs, recomputation methodology, AUM verification from CAMS/KFintech.\n"
                "(ii) Actuarial – gratuity: Reference specific assumptions tested (discount rate at 7.2% vs G-Sec yield), "
                "assessment of RM attrition below 1% and its effect on DBO.\n\n"
                "Step 3C – KAM must NOT use language that is identical to KAMs in prior year without specific reason. "
                "NFRA inspectors compare prior and current year KAMs and flag identical language.\n\n"
                "Step 3D – Engagement Partner must personally draft or review each KAM. "
                "KAMs cannot be entirely delegated to the team."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SA 701 Para 9, 10, 11, A30-A42",
            "kkc_ref": "KKC Manual S.48",
        },
        {
            "no": 4,
            "category": "NFRA Finding: Audit Documentation (SA 230) Deficiencies",
            "risk": "NFRA has found that working papers frequently lack sufficient detail to support the conclusions reached, with many workpapers appearing to be administrative forms rather than evidence of professional judgement.",
            "procedure": (
                "Step 4A – Before signing any workpaper, the team member must verify that it shows:\n"
                "(i) What was done (procedure performed).\n"
                "(ii) What was found (results, including negative findings).\n"
                "(iii) What was concluded (and why).\n"
                "(iv) Where exceptions were found: what were they, were they material, how was the exception resolved?\n\n"
                "Step 4B – Documentation of professional judgement: "
                "Where the team exercised significant professional judgement, document the judgement explicitly. "
                "Example: 'In our assessment, the actuarial discount rate of 7.2% is appropriate because [specific reasons]...'\n\n"
                "Step 4C – Working paper reviews by manager and partner: "
                "Reviews must be documented with dates. NFRA has found undated review notes. "
                "Every review must be signed with the reviewer's name and date.\n\n"
                "Step 4D – Differences of opinion: If team members disagree on a significant matter, "
                "document the disagreement, the alternative views, and how it was resolved. "
                "Suppress no dissenting views."
            ),
            "assertions": ["OCC", "COM", "ACC"],
            "sa_ref": "SA 230 Para 8, 9, 10, 11, 14 | SA 220 Para 24",
            "kkc_ref": "KKC Manual S.5, S.6",
        },
        {
            "no": 5,
            "category": "NFRA Finding: Independence & EQCR Violations",
            "risk": "NFRA has found independence declarations not maintained on file, and EQCR completed after audit report was signed.",
            "procedure": (
                "Step 5A – Independence compliance:\n"
                "(i) Obtain written independence declarations from all engagement team members and the EQCR reviewer.\n"
                "(ii) Verify no team member holds financial interests in ARWL or group entities.\n"
                "(iii) Verify no team member is a director, KMP, or employee of ARWL or any group entity.\n"
                "(iv) Verify firm does not provide prohibited non-audit services to ARWL.\n"
                "(v) Verify long association – has the Engagement Partner served for > 7 consecutive years? Rotation required.\n\n"
                "Step 5B – EQCR timing control:\n"
                "(i) EQCR must be completed before the audit report is signed.\n"
                "(ii) Build a completion timeline: Target date for EQCR completion must be at least 7 working days before planned report date.\n"
                "(iii) EQCR reviewer signs the EQCR completion certificate with date. "
                "This date must be before the Engagement Partner's report date.\n\n"
                "Step 5C – Document EQCR scope and evidence reviewed. "
                "NFRA requires EQCR documentation to show what was reviewed, not just a sign-off."
            ),
            "assertions": ["P&D"],
            "sa_ref": "SQC 1 Para 60-66 | SA 220 Para 14, 19, 20 | ICAI Code of Ethics",
            "kkc_ref": "KKC Manual S.3, S.6",
        },
        {
            "no": 6,
            "category": "NFRA Finding: Fraud Risk – Revenue Presumption Rebuttal",
            "risk": "NFRA has found that auditors rebut the presumed fraud risk in revenue recognition without adequate documented basis.",
            "procedure": (
                "Step 6A – If the engagement team decides to rebut the presumed revenue fraud risk for any revenue stream, "
                "the rebuttal must be based on entity-specific factors, not generic reasoning.\n\n"
                "Step 6B – Acceptable rebuttal basis for ARWL trail commission: "
                "'Trail commission is computed by AMCs and credit notes are issued directly. "
                "The primary risk is accuracy of AMC computation, not manipulation by management. "
                "Revenue is receivable from regulated entities (AMCs). "
                "However, we have not fully rebutted the risk – we still perform commission recomputation and cut-off testing.'\n\n"
                "Step 6C – Even with partial rebuttal, SA 240 mandatory procedures (JE testing, management override testing) "
                "cannot be omitted.\n\n"
                "Step 6D – For advisory fees and related-party revenue: Do NOT rebut fraud risk. "
                "These are directly controlled by management and lack third-party AMC corroboration."
            ),
            "assertions": ["OCC", "ACC"],
            "sa_ref": "SA 240 Para 26, 27 | NFRA Inspection Reports 2021-2024",
            "kkc_ref": "KKC Manual S.14",
        },
        {
            "no": 7,
            "category": "NFRA Finding: Substantive Testing – Sample Sizes & Extrapolation",
            "risk": "NFRA has found that sample sizes are not linked to assessed risk, and errors found in samples are not extrapolated to the population.",
            "procedure": (
                "Step 7A – Sample size determination: "
                "Document the basis for each sample size. Per SA 530, sample size should be based on: "
                "(i) Risk of material misstatement (higher risk → larger sample). "
                "(ii) Tolerable misstatement. "
                "(iii) Expected error rate. "
                "(iv) Population size.\n\n"
                "Step 7B – For MUS (Monetary Unit Sampling): "
                "Document: sampling interval = Tolerable misstatement / Reliability factor. "
                "Population value × Reliability factor / Tolerable misstatement = sample size.\n\n"
                "Step 7C – Error/exception evaluation:\n"
                "(i) For every exception found in a sample, document: nature, amount, cause, and whether it is a misstatement.\n"
                "(ii) For statistical sampling: project errors to population.\n"
                "(iii) Even for non-statistical sampling: consider qualitative impact of errors found.\n\n"
                "Step 7D – NFRA requirement: If errors are found in a sample and no adjustment is proposed, "
                "the workpaper must document why the projected population error is below tolerable misstatement."
            ),
            "assertions": ["OCC", "ACC", "COM", "VAL"],
            "sa_ref": "SA 530 Para 7, 9, 14, 15, 16 | SA 450 Para 5",
            "kkc_ref": "KKC Manual S.22",
        },
        {
            "no": 8,
            "category": "NFRA Finding: Related Party Completeness (SA 550)",
            "risk": "NFRA has found that auditors rely entirely on management's list of related parties without independently verifying completeness.",
            "procedure": (
                "Step 8A – Do not rely solely on management's related party list. "
                "Independently verify completeness using public sources: "
                "BSE/NSE shareholding pattern, MCA company search (common directors), "
                "SEBI insider trading disclosures (promoter group disclosures).\n\n"
                "Step 8B – Use CAATs to scan GL for transactions with related parties: "
                "String matching of counterparty names against related party list. "
                "NFRA has found that auditors did not use data analytics to verify completeness of RPT identification.\n\n"
                "Step 8C – For all identified RPTs: Verify audit committee approval (SEBI LODR Reg. 23). "
                "NFRA has found RPTs proceeding without proper approval.\n\n"
                "Step 8D – Test at least one material RPT for arm's length: obtain third-party evidence of pricing.\n\n"
                "Step 8E – Document the conclusion: all related parties identified, all RPTs approved, "
                "all at arm's length. Evidence basis for each conclusion."
            ),
            "assertions": ["COM", "OCC", "VAL"],
            "sa_ref": "SA 550 Para 11, 12, 13, 14, 15, 16, 25, 26",
            "kkc_ref": "KKC Manual S.15",
        },
    ],
},

}  # END OF WORKPROGRAMS
