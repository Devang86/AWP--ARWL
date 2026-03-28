# app.py  –  KKC Audit Work Program Generator  v4.0
# Streamlit application | No API key | Ind AS Updated | Detailed Revenue | NFRA Focus
# Devang Doshi, Partner – KKC & Associates LLP

import streamlit as st
from datetime import datetime
from workprogram_data_v4 import AUDIT_AREAS, WORKPROGRAMS, ASSERTION_MAP
from excel_generator_v4 import generate_excel

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="KKC Audit Work Program Generator v4.0",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
:root{
  --g:#7CB542;--b:#2C3E6B;--gr:#808285;--dk:#1F2D3D;
  --lg:#EDF7E0;--lb:#EBF0FF;--am:#FFF8E1;--bg:#F4F6FA;
  --red:#C0392B;
}
.stApp{background:var(--bg);}

.kkc-header{
  background:linear-gradient(120deg,#1F2D3D 0%,#2C3E6B 55%,#7CB542 100%);
  color:white;padding:24px 32px;border-radius:10px;margin-bottom:20px;
  box-shadow:0 4px 20px rgba(0,0,0,.18);
}
.kkc-header h1{font-size:23px;font-weight:800;margin:0;letter-spacing:.5px;}
.kkc-header p{font-size:12px;margin:5px 0 0;opacity:.85;}

.kkc-card{background:white;border-left:4px solid var(--g);
  border-radius:8px;padding:16px 20px;margin-bottom:14px;
  box-shadow:0 2px 10px rgba(0,0,0,.06);}
.kkc-card h3{color:var(--b);font-size:14px;margin:0 0 10px;font-weight:700;}

.metric-tile{background:white;border-radius:8px;padding:14px 10px;
  text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.07);border-top:3px solid var(--g);}
.metric-tile .val{font-size:30px;font-weight:800;}
.metric-tile .lbl{font-size:11px;color:var(--gr);margin-top:3px;}

.step-card{background:#FAFBFF;border:1px solid #E2E8F0;
  border-left:3px solid var(--g);border-radius:6px;
  padding:12px 16px;margin:8px 0;}
.step-num{background:var(--b);color:white;width:26px;height:26px;
  border-radius:50%;display:inline-flex;align-items:center;
  justify-content:center;font-size:11px;font-weight:800;
  margin-right:8px;vertical-align:middle;}
.step-cat{color:var(--g);font-weight:700;font-size:12px;vertical-align:middle;}
.step-risk{background:#FFF3CD;border-left:3px solid #F0A500;
  padding:6px 10px;border-radius:4px;margin:8px 0;
  font-size:12px;color:#7D4900;}
.step-proc{color:var(--dk);font-size:12.5px;white-space:pre-line;
  line-height:1.65;margin:8px 0;}
.step-meta{font-size:11px;margin-top:8px;display:flex;gap:16px;flex-wrap:wrap;}
.step-sa{color:var(--b);}
.step-ias{color:#1A5276;font-weight:600;}
.step-kkc{color:var(--gr);}
.step-ass{color:#1E8449;font-weight:600;}

.indas-badge{display:inline-block;background:#EBF5FB;color:#1A5276;
  font-size:10px;font-weight:700;padding:2px 7px;border-radius:8px;
  margin-left:4px;border:1px solid #AED6F1;}
.nfra-badge{display:inline-block;background:#C0392B;color:white;
  font-size:10px;font-weight:700;padding:2px 7px;border-radius:8px;margin-left:4px;}
.rev-badge{display:inline-block;background:#7CB542;color:white;
  font-size:10px;font-weight:700;padding:2px 7px;border-radius:8px;margin-left:4px;}

.obj-box{background:var(--lb);border-left:3px solid var(--b);
  border-radius:5px;padding:10px 14px;font-size:12px;
  color:var(--dk);margin-bottom:8px;line-height:1.6;}
.risk-box{background:var(--am);border-left:3px solid #F0A500;
  border-radius:5px;padding:10px 14px;font-size:12px;
  color:#5D4037;margin-bottom:10px;line-height:1.6;}

section[data-testid="stSidebar"]{background:#1A2535;}
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{color:#E8EDF5 !important;}

.stDownloadButton>button{
  background:linear-gradient(120deg,#7CB542,#5A9C2A)!important;
  color:white!important;font-size:15px!important;font-weight:700!important;
  border-radius:7px!important;border:none!important;width:100%;
  box-shadow:0 4px 12px rgba(124,181,66,.4)!important;}
div.stButton>button{background:var(--b)!important;color:white!important;
  font-weight:700!important;border-radius:6px!important;border:none!important;}

.kkc-footer{text-align:center;color:var(--gr);font-size:11px;
  margin-top:40px;padding-top:14px;border-top:1px solid #E0E4EC;}
.indas-info{background:#EBF5FB;border:1px solid #AED6F1;border-radius:8px;
  padding:12px 16px;margin:10px 0;font-size:12px;color:#1A5276;}
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="kkc-header">
  <h1>📋 KKC Audit Work Program Generator  <span style="font-size:14px;opacity:.75;">v4.0</span></h1>
  <p>KKC &amp; Associates LLP, Chartered Accountants &nbsp;·&nbsp;
     Mumbai · Pune · Bengaluru · Ahmedabad &nbsp;·&nbsp;
     Mapped to ICAI SAs, All Ind AS (MCA) &amp; KKC Audit Manual 2026 &nbsp;·&nbsp;
     NFRA Inspection Focus Included</p>
</div>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Engagement Details")
    st.markdown("---")
    company     = st.text_input("Client / Company Name", value="Anand Rathi Wealth Limited")
    period      = st.text_input("Period of Audit",       value="Year ended 31 March 2026")
    materiality = st.text_input("Overall Materiality (₹)", placeholder="e.g. ₹9.81 Crores")
    ep          = st.text_input("Engagement Partner",    value="")
    em          = st.text_input("Engagement Manager",    value="")

    st.markdown("---")
    st.markdown("### 📚 Source Documents")
    st.markdown("""<small style='color:#9EB3CC;'>
✅ KKC Audit Manual 2026 (511 pages)<br>
✅ ICAI SA Checklist – All 38 SAs (1,344 pages)<br>
✅ All Ind AS merged PDF (MCA, 1,591 pages)<br>
✅ ARWL Annual Report FY 2024-25<br>
✅ NFRA Inspection Reports 2021–2024
</small>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🆕 v4.0 Enhancements")
    st.markdown("""<small style='color:#9EB3CC;'>
<b>Ind AS Updates (All Ind AS reviewed):</b><br>
• Ind AS 115: Variable consideration constraint,<br>
&nbsp;&nbsp;over-time vs point-in-time PO<br>
• Ind AS 109: SPPI test, dirty/clean price,<br>
&nbsp;&nbsp;derecognition criteria, FVTPL gains<br>
• Ind AS 37: Three-condition provision test<br>
• Ind AS 19: OCI vs P&L split, G-Sec discount rate<br>
• Ind AS 116: Reasonably certain, IBR, SaaS<br>
• Ind AS 12: All temp differences, DTA recoverability<br>
• Ind AS 24: KMP compensation, full disclosure<br>
• Ind AS 36: VIU, CGU, annual impairment test<br><br>
<b>Revenue Area:</b> 15 detailed steps<br>
Stream A: 9 steps (RTA reconciliation)<br>
Stream B: 6 steps (Structured products)<br><br>
<b>New Excel sheet:</b> Ind AS Modifications
</small>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🏷️ Assertions")
    st.markdown("""<small style='color:#9EB3CC;'>
OCC=Occurrence | COM=Completeness<br>
ACC=Accuracy | COF=Cut-off | CLA=Classification<br>
EXI=Existence | R&O=Rights & Obligations<br>
VAL=Valuation | P&D=Presentation & Disclosure
</small>""", unsafe_allow_html=True)

# ── AREA GROUPS ───────────────────────────────────────────────────────────────
AREA_GROUPS = {
    "📊 Income & Revenue": [
        "Revenue from Operations",
        "Other Income",
    ],
    "💼 Expenses": [
        "Employee Benefits Expenses",
        "Other Expenses",
        "Finance Costs",
    ],
    "🏦 Assets": [
        "Investments",
        "Trade Receivables & Accrued Income",
        "Cash & Bank Balances",
        "Fixed Assets & Intangibles",
        "Leases (Ind AS 116)",
    ],
    "📋 Liabilities & Equity": [
        "Borrowings",
        "Provisions & Other Liabilities",
        "Share Capital, Reserves & Equity",
        "Contingent Liabilities & Commitments",
    ],
    "🔍 Risk, Fraud & Estimates": [
        "Risk Assessment – FSLI",
        "Fraud Risk Assessment",
        "Significant Judgements & Estimates",
        "Related Party Transactions",
        "Going Concern",
    ],
    "🖥️ IT, Tax & Compliance": [
        "IT Application & ITGC Testing",
        "SEBI LODR & Statutory Compliance",
        "Taxation – Current & Deferred",
    ],
    "✅ Completion & Quality": [
        "Audit Completion & Reporting",
        "NFRA Inspection Focus Areas",
    ],
}

# Ind AS banner for special areas
IND_AS_TAGS = {
    "Revenue from Operations":          "Ind AS 115 + Ind AS 109",
    "Investments":                       "Ind AS 109 + Ind AS 36",
    "Leases (Ind AS 116)":               "Ind AS 116",
    "Employee Benefits Expenses":        "Ind AS 19 + Ind AS 102",
    "Borrowings":                        "Ind AS 109 + Ind AS 32",
    "Provisions & Other Liabilities":    "Ind AS 37",
    "Taxation – Current & Deferred":     "Ind AS 12",
    "Related Party Transactions":        "Ind AS 24",
    "Significant Judgements & Estimates":"Ind AS 1",
    "Share Capital, Reserves & Equity":  "Ind AS 33",
    "Fixed Assets & Intangibles":        "Ind AS 16 + Ind AS 38",
    "Going Concern":                     "Ind AS 1",
    "Trade Receivables & Accrued Income":"Ind AS 109 (ECL)",
    "NFRA Inspection Focus Areas":       "NFRA",
}

# ── INIT SESSION STATE ────────────────────────────────────────────────────────
if "selected_areas" not in st.session_state:
    st.session_state.selected_areas = set(AUDIT_AREAS)

# ── MAIN LAYOUT ───────────────────────────────────────────────────────────────
left_col, right_col = st.columns([3, 2])

with left_col:
    # Ind AS notice
    st.markdown("""<div class="indas-info">
    <b>📖 Ind AS Integration Notice:</b> This tool has been updated based on a review of
    <b>All_IND_AS_merged.pdf (MCA, 1,591 pages)</b> covering all Indian Accounting Standards.
    Key modifications include: Ind AS 115 variable consideration constraint for trail commissions,
    Ind AS 109 SPPI test and dirty/clean price separation for structured product gains,
    Ind AS 37 three-condition provision test, and Ind AS 19 discount rate verification.
    A dedicated <b>Ind AS Modifications</b> sheet is included in the Excel output.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="kkc-card"><h3>🎯 Select Audit Areas</h3>', unsafe_allow_html=True)

    btn1, btn2, btn3 = st.columns(3)
    if btn1.button("✅ Select All"):
        st.session_state.selected_areas = set(AUDIT_AREAS)
        for area in AUDIT_AREAS:
            st.session_state[f"chk_{area}"] = True
        st.rerun()
    if btn2.button("❌ Clear All"):
        st.session_state.selected_areas = set()
        for area in AUDIT_AREAS:
            st.session_state[f"chk_{area}"] = False
        st.rerun()
    if btn3.button("⭐ Core Areas"):
        core = {
            "Revenue from Operations","Employee Benefits Expenses","Investments",
            "Related Party Transactions","Fraud Risk Assessment","Risk Assessment – FSLI",
            "Significant Judgements & Estimates","Audit Completion & Reporting",
            "NFRA Inspection Focus Areas",
        }
        st.session_state.selected_areas = core
        for area in AUDIT_AREAS:
            st.session_state[f"chk_{area}"] = area in core
        st.rerun()

    selected = []
    for group_name, group_areas in AREA_GROUPS.items():
        with st.expander(group_name, expanded=True):
            gcols = st.columns(2)
            for idx, area in enumerate(group_areas):
                col = gcols[idx % 2]
                tag = IND_AS_TAGS.get(area, "")
                is_nfra = "NFRA" in area
                is_rev  = "Revenue" in area and "Other" not in area
                prefix  = "🔴 " if is_nfra else ("🟢 " if is_rev else "")
                label   = f"{prefix}{area}"
                if tag and not is_nfra:
                    label += f"  [{tag}]"
                checked = col.checkbox(label, value=(area in st.session_state.selected_areas), key=f"chk_{area}")
                if checked:
                    selected.append(area)
                    st.session_state.selected_areas.add(area)
                else:
                    st.session_state.selected_areas.discard(area)
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    total_steps = sum(len(WORKPROGRAMS[a]["steps"]) for a in selected if a in WORKPROGRAMS)
    unique_sas  = set()
    unique_ias  = set()
    for a in selected:
        if a not in WORKPROGRAMS: continue
        for s in WORKPROGRAMS[a]["steps"]:
            for p in s.get("sa_ref","").split("|"):
                p = p.strip()
                if p.startswith("SA"):
                    unique_sas.add(" ".join(p.split()[:2])[:9])
                elif p.startswith("Ind AS"):
                    unique_ias.add(p.split("Para")[0].strip()[:12])

    # Metrics
    st.markdown('<div class="kkc-card"><h3>📊 Program Statistics</h3>', unsafe_allow_html=True)
    m1,m2,m3,m4 = st.columns(4)
    for col,(val,lbl,color) in zip([m1,m2,m3,m4],[
        (str(len(selected)),     "Areas",     "#2C3E6B"),
        (str(total_steps),       "Steps",     "#2C3E6B"),
        (str(len(unique_sas)),   "SAs",       "#7CB542"),
        (str(len(unique_ias)),   "Ind AS",    "#1A5276"),
    ]):
        col.markdown(
            f'<div class="metric-tile"><div class="val" style="color:{color};">{val}</div>'
            f'<div class="lbl">{lbl}</div></div>', unsafe_allow_html=True)

    if unique_ias:
        st.markdown("<br>**Ind AS Referenced:**", unsafe_allow_html=True)
        st.markdown(" ".join(f'<span class="indas-badge">{s}</span>' for s in sorted(unique_ias)),
                    unsafe_allow_html=True)
    if unique_sas:
        st.markdown("**SAs Referenced:**")
        st.markdown(", ".join(f"`{s}`" for s in sorted(unique_sas)))
    st.markdown('</div>', unsafe_allow_html=True)

    # Revenue highlight card
    if "Revenue from Operations" in selected:
        rev_steps = WORKPROGRAMS["Revenue from Operations"]["steps"]
        mf_steps = [s for s in rev_steps if s["no"] <= 9]
        sp_steps = [s for s in rev_steps if s["no"] >= 10]
        st.markdown(f"""<div class="kkc-card" style="border-left-color:#1A5276;">
        <h3>🟢 Revenue Deep-Dive Summary</h3>
        <small>
        <b>Stream A – MF Distribution ({len(mf_steps)} steps):</b><br>
        Ind AS 115 five-step model · CAMS RTA reconciliation · KFintech RTA reconciliation ·
        AUM vs AMFI published data · Folio-level verification · Upfront AMFI ban check ·
        SIP PO treatment · Form 26AS TDS cross-check · SA 240 JE testing<br><br>
        <b>Stream B – Structured Products ({len(sp_steps)} steps):</b><br>
        Ind AS 109 SPPI test · NSDL/CDSL demat verification · Dirty/clean price separation ·
        MLD redemption computation · Anti-MTM double-count check · CAAT 100% recomputation ·
        Ind AS 109 Para 3.2.3 derecognition · Related party arm's length (Ind AS 24)
        </small></div>""", unsafe_allow_html=True)

# ── PREVIEW ───────────────────────────────────────────────────────────────────
if selected:
    st.markdown("---")
    st.markdown("## 🔍 Work Program Preview")

    def tab_label(area):
        is_nfra = "NFRA" in area
        is_rev  = "Revenue" in area and "Other" not in area
        prefix  = "🔴 " if is_nfra else ("🟢 " if is_rev else "")
        return f"{prefix}{area[:26]}"

    preview_areas = selected[:10]
    if len(selected) > 10:
        st.info(f"Preview shows first 10 of {len(selected)} areas. All areas included in Excel output.")

    tabs = st.tabs([tab_label(a) for a in preview_areas])

    for tab, area in zip(tabs, preview_areas):
        with tab:
            data = WORKPROGRAMS.get(area)
            if not data:
                st.warning(f"Work program data unavailable for '{area}'.")
                continue

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f'<div class="obj-box"><b>📌 Audit Objective</b><br><br>{data["objective"]}</div>',
                            unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="risk-box"><b>⚠️ Risk Overview (Ind AS Basis)</b><br><br>{data["risk_overview"]}</div>',
                            unsafe_allow_html=True)

            # Show Ind AS tag for this area
            ias_tag = IND_AS_TAGS.get(area, "")
            if ias_tag:
                if "NFRA" in ias_tag:
                    st.markdown(f'<span class="nfra-badge">NFRA FOCUS</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<span class="indas-badge">📖 {ias_tag}</span>', unsafe_allow_html=True)

            st.markdown(f"**{len(data['steps'])} audit procedures:**")

            for step in data["steps"]:
                proc_html = step["procedure"].replace("\n","<br>")
                assertions_text = "  |  ".join(
                    f"<b>{ASSERTION_MAP.get(c,c)}</b>" for c in step["assertions"])

                full_ref = step.get("sa_ref","")
                sa_parts    = " | ".join(p.strip() for p in full_ref.split("|")
                               if p.strip().startswith("SA") or p.strip().startswith("SQC"))
                ind_as_parts= " | ".join(p.strip() for p in full_ref.split("|")
                               if p.strip().startswith("Ind AS") or p.strip().startswith("SEBI") or
                                  p.strip().startswith("Companies") or p.strip().startswith("Rule"))

                st.markdown(f"""
                <div class="step-card">
                  <span class="step-num">{step['no']}</span>
                  <span class="step-cat">{step['category']}</span>
                  <div class="step-risk">⚠️ {step['risk']}</div>
                  <div class="step-proc">{proc_html}</div>
                  <div class="step-meta">
                    <span class="step-sa">📖 {sa_parts}</span>
                    {'<span class="step-ias">📘 ' + ind_as_parts + '</span>' if ind_as_parts else ''}
                    <span class="step-kkc">📁 {step['kkc_ref']}</span>
                    <span class="step-ass">🏷️ {assertions_text}</span>
                  </div>
                </div>
                """, unsafe_allow_html=True)

# ── GENERATE ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 📥 Generate & Download Audit Work Program")

if not company or not period:
    st.warning("⚠️ Enter Company Name and Period of Audit in the sidebar first.")
elif not selected:
    st.warning("⚠️ Select at least one audit area.")
else:
    gc1, gc2, gc3 = st.columns([1,3,1])
    with gc2:
        st.markdown(f"""<div class="kkc-card">
        <h3>📋 Generation Summary</h3>
        <table width="100%" style="font-size:13px;">
          <tr><td style="color:#808285;width:42%">Client</td>
              <td style="font-weight:700;color:#1F2D3D">{company}</td></tr>
          <tr><td style="color:#808285">Period</td>
              <td style="font-weight:700;color:#1F2D3D">{period}</td></tr>
          <tr><td style="color:#808285">Audit Areas</td>
              <td style="font-weight:700;color:#1F2D3D">{len(selected)}</td></tr>
          <tr><td style="color:#808285">Total Steps</td>
              <td style="font-weight:700;color:#1F2D3D">{total_steps}</td></tr>
          <tr><td style="color:#808285">Ind AS Referenced</td>
              <td style="font-weight:700;color:#1A5276">{len(unique_ias)} standards</td></tr>
          <tr><td style="color:#808285">SAs Referenced</td>
              <td style="font-weight:700;color:#2C3E6B">{len(unique_sas)} standards</td></tr>
          <tr><td style="color:#808285">Materiality</td>
              <td style="font-weight:700;color:#1F2D3D">{materiality or "Not specified"}</td></tr>
          <tr><td style="color:#808285">Format</td>
              <td style="font-weight:700;color:#7CB542">Excel (.xlsx) – KKC Branded, Multi-Sheet</td></tr>
        </table>
        </div>""", unsafe_allow_html=True)

        if st.button("🚀  Generate Audit Work Program (Excel)", use_container_width=True):
            with st.spinner("Building KKC-branded Excel workbook with Ind AS updates..."):
                excel_bytes = generate_excel(
                    company=company, period=period, areas=selected,
                    materiality=materiality, ep=ep, em=em,
                )
            fname = (f"KKC_Audit_WP_v4_{company.replace(' ','_')[:25]}_"
                     f"{datetime.today().strftime('%Y%m%d')}.xlsx")
            st.success(f"✅ Work Program generated — {len(excel_bytes)//1024} KB")
            st.download_button(
                label="⬇️  Download Excel Work Program",
                data=excel_bytes, file_name=fname,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
            )

        st.markdown("""<div style="background:#F4F6FA;border-radius:6px;
                         padding:10px 14px;margin-top:10px;font-size:11px;color:#808285;">
        <b>Excel includes:</b>&nbsp;
        📄 Cover Page &nbsp;|&nbsp; 📊 Summary Dashboard &nbsp;|&nbsp;
        📘 <b>Ind AS Modifications Sheet (NEW)</b> &nbsp;|&nbsp;
        📋 One detailed sheet per audit area (KKC branded, frozen headers, sign-off rows) &nbsp;|&nbsp;
        Each sheet has separate SA Reference and Ind AS / Regulatory Reference columns.
        </div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="kkc-footer">
  KKC &amp; Associates LLP, Chartered Accountants &nbsp;|&nbsp;
  Mumbai · Pune · Bengaluru · Ahmedabad<br>
  Audit Work Program Generator v4.0 &nbsp;|&nbsp;
  Standards: ICAI SAs · All Ind AS (MCA, 1,591 pages) · KKC Audit Manual 2026<br>
  Revenue: MF Distribution (CAMS+KFintech RTA reconciliation) · Structured Products (Ind AS 109 SPPI + Dirty/Clean price)<br>
  <small>For professional use by KKC engagement teams only. Adapt all procedures to engagement-specific circumstances.</small>
</div>
""", unsafe_allow_html=True)
