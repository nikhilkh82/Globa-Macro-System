# -*- coding: utf-8 -*-
"""
build_uk_workbook.py
====================
Build UK_Endogenous_Driver_Analysis.xlsx from the data cache produced by
refresh_uk_data.py. Mirrors the US automated file's logic & layout:
  * one data sheet per driver (Date / Value / %change + embedded scoring table)
  * a 'UK Endo' Score' dashboard with live LOOKUP formulas (E=latest rate,
    F=score from an embedded ascending helper table) and roll-up subtotals
  * Sources, Cycles (UK recessions), GDP Quarterly sheets

Run:  py build_uk_workbook.py      (after refresh_uk_data.py)
"""
from __future__ import annotations

import os
import json
from datetime import datetime, date
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "uk_data_cache.json")
OUT = os.path.join(HERE, "UK_Endogenous_Driver_Analysis.xlsx")

# ---- styling ----
HDR_FILL = PatternFill("solid", fgColor="1F4E78")
HDR_FONT = Font(color="FFFFFF", bold=True, size=11)
GROUP_FONT = Font(bold=True, size=12, color="1F4E78")
TITLE_FONT = Font(bold=True, size=14, color="1F4E78")
SUB_FONT = Font(italic=True, size=10, color="808080")
WARN_FONT = Font(italic=True, size=9, color="C00000")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
SCORE_FILL = PatternFill("solid", fgColor="FFF2CC")
SC_TABLE_HDR = PatternFill("solid", fgColor="D9E1F2")


def load_cache():
    with open(CACHE, encoding="utf-8") as f:
        return json.load(f)


def latest(series):
    """Return (iso_date, value) of last non-null point, or (None, None)."""
    pts = [(d, v) for d, v in series if v is not None]
    return pts[-1] if pts else (None, None)


# ===========================================================================
# Data-sheet builder
# ===========================================================================
def build_data_sheet(wb, sheet_name, series, header_label, *,
                     value_col_letter="B", pct=True, date_freq="monthly",
                     extra_notes=None):
    """Create a sheet with Date / Value (and % change) history + a title.

    Returns the worksheet. The scoring table is added separately by the caller
    because its threshold/score ranges are driver-specific.
    """
    ws = wb.create_sheet(sheet_name)
    ws["A1"] = "Date"
    ws["B1"] = header_label
    ws["C1"] = "% Change" if pct else "Change"
    for c in ("A1", "B1", "C1"):
        ws[c].fill = HDR_FILL; ws[c].font = HDR_FONT; ws[c].border = BORDER
    r = 2
    prev = None
    for d_iso, v in series:
        if v is None:
            continue
        try:
            dt = datetime.fromisoformat(d_iso).date()
        except Exception:
            continue
        ws.cell(row=r, column=1, value=dt).number_format = "yyyy-mm-dd"
        ws.cell(row=r, column=2, value=float(v))
        if prev and prev != 0:
            ws.cell(row=r, column=3, value=f"=(B{r}-B{r-1})/ABS(B{r-1})").number_format = "0.00%"
        prev = v
        r += 1
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 12
    if extra_notes:
        ws.cell(row=1, column=5, value=extra_notes).font = SUB_FONT
    ws.freeze_panes = "A2"
    return ws, r - 1  # last data row


def add_score_table(ws, start_col, start_row, thresholds_scores, title):
    """Write an ascending (threshold, score) table at start_col/start_row.
    thresholds_scores: list of (threshold, score) ASCENDING by threshold.
    Returns (th_range, sc_range) e.g. ('$F$5:$F$18','$G$5:$G$18')."""
    tc = get_column_letter(start_col)
    sc = get_column_letter(start_col + 1)
    ws.cell(row=start_row, column=start_col, value=title).font = Font(bold=True, size=10)
    ws.cell(row=start_row, column=start_col + 1, value="Score").font = Font(bold=True, size=10)
    first = start_row + 1
    for i, (th, scv) in enumerate(thresholds_scores):
        ws.cell(row=first + i, column=start_col, value=th)
        ws.cell(row=first + i, column=start_col + 1, value=scv)
    last = first + len(thresholds_scores) - 1
    return f"${tc}${first}:${tc}${last}", f"${sc}${first}:${sc}${last}"


# ===========================================================================
# Scoring tables — UK-tuned (anchored to reference UK values)
#   each list is ASCENDING by threshold
# ===========================================================================
# PMIs (Manufacturing/Services): 50 = breakeven; >55 strong, <48 weak
PMI = [(-50,-10),(0,-10),(35,-10),(40,-8),(44,-5),(48,-2),(50,0),(52,2),(54,4),(56,6),(58,8),(60,10),(65,10)]
# Consumer confidence (OECD CSCICP02, around -20 to +5 for UK): low score = deeply negative
CONF = [(-50,-10),(-40,-10),(-35,-8),(-30,-6),(-25,-4),(-20,-2),(-15,0),(-10,2),(-5,4),(0,6),(5,8),(10,10)]
# Building approvals: number of new housing approvals (thousands); high = inflationary
BP = [(0,-10),(20,-8),(40,-5),(60,-2),(80,2),(100,4),(120,6),(140,8),(160,10),(200,10)]
# M4 broad money YoY %: ~0-5 normal (used when YoY col D is populated)
M4 = [(-10,-10),(-5,-8),(0,-4),(2,0),(4,2),(6,4),(8,6),(10,8),(12,10),(15,10)]
# M4 level (£bn) fallback table — used when only the level is available (sparse history).
# Anchored near current UK broad money ~£2,200bn.
M4_LEVEL = [(0,-10),(500,-8),(1000,-4),(1500,0),(1800,2),(2000,4),(2200,6),(2500,8),(3000,10),(4000,10)]
# Bank Rate % : low = inflationary/QE
IR = [(-1,-10),(-0.5,-10),(0,10),(0.5,8),(1,6),(2,4),(3,2),(4,0),(5,-2),(6,-4),(8,-6),(10,-8),(12,-10)]
# CPI monthly % (decimal*100): UK ~0.1-0.5/mo. Anchored: 0.06->0
CPI = [(-1,10),(-0.5,10),(-0.3,-10),(-0.2,-8),(-0.1,-6),(0,-4),(0.05,0),(0.1,0),(0.2,2),(0.3,4),(0.5,6),(0.8,8),(1,10),(1.5,6),(2,3)]
CORECPI = [(-1,10),(-0.5,10),(-0.3,9),(-0.2,8),(-0.1,-8),(0,-4),(0.05,0),(0.1,0),(0.2,2),(0.3,4),(0.5,6),(0.8,8),(1,10),(1.5,6),(2,3)]
# PPI monthly %
PPI = [(-2,10),(-1.5,10),(-1,10),(-0.5,-4),(-0.25,-2),(0,0),(0.25,0),(0.5,2),(0.75,4),(1,8),(1.5,10),(2,3)]
COREPPI = PPI
# Unemployment % (used as the Employment driver, INVERTED: high unemployment = deflationary/bearish)
UNEMP = [(0,-10),(2,-8),(3,-6),(3.5,-4),(4,0),(4.5,4),(5,6),(5.5,8),(6,10),(8,10),(10,10)]
# Govt debt/GDP % (high = default/inflate risk -> high score)
DEBT = [(0,0),(20,2),(40,4),(60,6),(70,7),(80,8),(90,9),(100,10),(110,10),(120,10)]
# Deficit % GDP (negative = borrowing/injection = inflationary -> high score)
DEFICIT = [(-15,10),(-12,10),(-10,10),(-8,9),(-6,8),(-4,6),(-2,3),(0,0),(2,-3),(4,-6),(6,-8),(8,-10)]
# Interest/GDP % (high = deflationary drag)
INTEREST = [(0,0),(0.5,-2),(1,-4),(1.5,-6),(2,-8),(2.5,-10),(3,-10),(4,-10),(5,-10)]
# Liquidity (interest cover ratio, high = healthy/inflationary)
LIQ = [(0,-10),(1,-9),(2,-8),(3,-7),(5,-5),(8,-2),(10,0),(12,2),(14,4),(16,6),(18,8),(20,10)]
# 10Y gilt % (fraction; low = inflationary/QE)
T10 = [(-0.01,10),(0,10),(0.005,9),(0.01,8),(0.02,6),(0.03,4),(0.04,2),(0.05,0),(0.06,-2),(0.07,-4),(0.08,-6),(0.1,-8),(0.12,-10)]
# CB balance sheet % GDP (BoE APF; high = inflationary)
CBBS = [(0,0),(5,1),(10,2),(15,3),(20,4),(25,5),(30,6),(35,7),(40,8),(50,10),(60,10)]


# ===========================================================================
# Driver definitions: (row, group, name, code, score_table, source, manual_flag)
# rate_formula filled in build_dashboard once data-sheet value columns known.
# ===========================================================================
DRIVERS = [
    # Leading indicators
    (5,  "Leading Indicators",   "Business Sentiment - UK Manufacturing PMI", "PMI",  PMI,  "S&P Global / CIPS (MANUAL)", True),
    (6,  "",                     "Business Sentiment - UK Services PMI",      "PMI",  PMI,  "S&P Global / CIPS (MANUAL)", True),
    (7,  "",                     "Consumer Confidence (OECD)",                "CONF", CONF, "FRED CSCICP02GBM460S", False),
    (8,  "",                     "Building Permits / Housing Approvals",      "BP",   BP,   "DLUHC (MANUAL)", True),
    # Money & rates
    (12, "Money Supply",         "M4 Broad Money",                            "M4",   M4_LEVEL, "FRED MANMM101GBM189S (£bn level; YoY col added when full history loads)", True),
    (14, "Interest Rates",       "Bank of England Bank Rate",                 "IR",   IR,   "BoE / FRED IRSTCI01GBM156N", False),
    # Inflation
    (16, "Inflation",            "Consumer Inflation",                        "CPI",  CPI,  "ONS D7G7 (CPI rate)", False),
    (17, "",                     "Core CPI",                                  "CPI",  CORECPI, "ONS DKO8 (core CPI rate)", False),
    (18, "",                     "PPI Output",                                "PPI",  PPI,  "ONS GB7S (PPI output)", False),
    (19, "",                     "PPI Input",                                 "PPI",  COREPPI,"ONS GHIK (PPI input)", False),
    # Employment
    (23, "Employment",           "Unemployment Rate",                         "UNEMP",UNEMP,"ONS MGSX / FRED LRHUTTTTGBM156S", False),
    # Balance sheets
    (26, "Balance Sheets and Sovereign Risk", "Government Debt to GDP Ratio", "Govt", DEBT, "ONS A3PW (Maastricht)", False),
    (27, "",                     "Government Deficit % GDP",                  "Govt", DEFICIT, "ONS J5II (PS borrowing)", False),
    (28, "",                     "Interest / GDP",                            "Govt", INTEREST, "Derived (manual)", True),
    (29, "",                     "Liquidity Cover",                           "Govt", LIQ,   "Derived (manual)", True),
    (30, "",                     "UK 10Y Gilt Benchmark",                     "Govt", T10,   "FRED IRLTLT01GBM156N", False),
    (31, "",                     "BoE Balance Sheet % GDP (APF)",             "CBBS", CBBS,  "BoE APEXLPMA (MANUAL)", True),
]


# ===========================================================================
# Main builder
# ===========================================================================
def build():
    cache = load_cache()
    wb = openpyxl.Workbook()
    # remove default sheet; we'll create dashboard first
    wb.remove(wb.active)

    # ---- dashboard ----
    dash = wb.create_sheet("UK Endo' Score")

    # ---- data sheets + scoring tables ----
    # Map driver row -> (sheet_name, value_col_for_lookup, score_th_range, score_sc_range)
    driver_meta = {}
    score_col_cursor = 6  # place scoring tables starting col F on each data sheet

    def make_series_sheet(name, series, label):
        ws, last = build_data_sheet(wb, name, series or [], label)
        return ws, last

    # Build the per-driver data sheets. For manual ones, write a single
    # placeholder row with a known value column so LOOKUP works; flag clearly.
    def manual_sheet(name, label, latest_val, source_note):
        ws = wb.create_sheet(name)
        ws["A1"] = "Date"; ws["B1"] = label
        ws["A1"].fill = HDR_FILL; ws["A1"].font = HDR_FONT
        ws["B1"].fill = HDR_FILL; ws["B1"].font = HDR_FONT
        # placeholder latest row
        ws["A2"] = date.today()
        ws["B2"] = latest_val if latest_val is not None else 0
        ws["E1"] = "MANUAL — paste current value in B2 each period. Source: " + source_note
        ws["E1"].font = WARN_FONT
        ws.column_dimensions["A"].width = 12
        ws.column_dimensions["B"].width = 14
        return ws, 2

    # --- Leading indicators ---
    # PMI mfg (manual; ref value 53.3)
    ws, _ = manual_sheet("PMI_Mfg", "UK Manufacturing PMI", 48.0, "S&P Global/CIPS Manufacturing PMI")
    driver_meta[5] = ("PMI_Mfg", "B")
    # PMI services (manual; ref 52.3)
    ws, _ = manual_sheet("PMI_Svc", "UK Services PMI", 50.9, "S&P Global/CIPS Services PMI")
    driver_meta[6] = ("PMI_Svc", "B")
    # Consumer confidence (FRED) - monthly index
    ws, _ = make_series_sheet("UMCSI", cache.get("consumer_conf", []), "Consumer Confidence")
    driver_meta[7] = ("UMCSI", "B")
    # Building permits (manual)
    ws, _ = manual_sheet("BP", "Housing Approvals (k)", 84.1, "DLUHC housebuilding approvals")
    driver_meta[8] = ("BP", "B")

    # --- Money / rates ---
    # M4 YoY (compute from broad money level series)
    m4 = cache.get("m4", [])
    ws, last = make_series_sheet("M4", m4, "Broad Money £m")
    # add YoY % column D and point dashboard at it
    if last > 13:
        ws.cell(row=1, column=4, value="YoY %").font = HDR_FONT
        ws.cell(row=1, column=4).fill = HDR_FILL
        for r in range(14, last + 1):
            ws.cell(row=r, column=4, value=f"=(B{r}-B{r-12})/B{r-12}").number_format = "0.00%"
    driver_meta[12] = ("M4", "B")   # level col (£bn); YoY col D added when full history loads
    ws["E1"] = "Level £bn shown (YoY% col D auto-computes once FRED history loads). Refresh via refresh_uk_data.py"
    ws["E1"].font = SUB_FONT
    # Bank rate
    ws, _ = make_series_sheet("IR%", cache.get("bank_rate", []), "Bank Rate %")
    driver_meta[14] = ("IR%", "B")

    # --- Inflation (ONS rate series are already in %; place in B, %change in C) ---
    ws, _ = make_series_sheet("CPI", cache.get("cpi_rate", []), "CPI YoY %")
    driver_meta[16] = ("CPI", "B")
    ws, _ = make_series_sheet("CoreCPI", cache.get("corecpi_rate", []), "Core CPI YoY %")
    driver_meta[17] = ("CoreCPI", "B")
    # PPI output/input: index levels -> compute YoY% in col C usage; place index in B
    ws, last_ppi = make_series_sheet("PPI_Output", cache.get("ppi_output", []), "PPI Output idx")
    # add YoY % in col D
    if last_ppi > 13:
        ws.cell(row=1, column=4, value="YoY %").font = HDR_FONT; ws.cell(row=1,column=4).fill=HDR_FILL
        for r in range(14, last_ppi+1):
            ws.cell(row=r, column=4, value=f"=(B{r}-B{r-12})/B{r-12}").number_format = "0.00%"
    driver_meta[18] = ("PPI_Output", "D")
    ws, last_ppii = make_series_sheet("PPI_Input", cache.get("ppi_input", []), "PPI Input idx")
    if last_ppii > 13:
        ws.cell(row=1, column=4, value="YoY %").font = HDR_FONT; ws.cell(row=1,column=4).fill=HDR_FILL
        for r in range(14, last_ppii+1):
            ws.cell(row=r, column=4, value=f"=(B{r}-B{r-12})/B{r-12}").number_format = "0.00%"
    driver_meta[19] = ("PPI_Input", "D")

    # --- Employment ---
    ws, _ = make_series_sheet("Unemp", cache.get("unemp", []), "Unemployment %")
    driver_meta[23] = ("Unemp", "B")

    # --- Balance sheets ---
    # Govt sheet: combine debt/GDP, deficit, (interest, liquidity manual) in one sheet like US 'Govt'
    govt = wb.create_sheet("Govt")
    govt["A1"] = "Date"; govt["B1"] = "Real GDP (£m)"; govt["C1"] = "Debt (£m)"; govt["D1"] = "Debt/GDP %"
    govt["E1"] = "Receipts"; govt["F1"] = "Outlays"; govt["G1"] = "Surplus/Deficit"; govt["H1"] = "Deficit %GDP"
    govt["I1"] = "Interest Bill"; govt["J1"] = "Interest/GDP"; govt["K1"] = "Liquidity Cover"
    for c in "ABCDEFGHIJK":
        govt[c+"1"].fill = HDR_FILL; govt[c+"1"].font = HDR_FONT
    # write debt/gdp series into col D (we only have the ratio, not the components)
    debt = cache.get("debt_gdp", [])
    gr = 2
    for d_iso, v in debt:
        try: dt = datetime.fromisoformat(d_iso).date()
        except: continue
        govt.cell(row=gr, column=1, value=dt).number_format = "yyyy-mm-dd"
        govt.cell(row=gr, column=4, value=float(v))
        gr += 1
    govt.cell(row=1, column=13, value="Debt/GDP from ONS A3PW (Maastricht). Interest/GDP & Liquidity are MANUAL.").font = SUB_FONT
    driver_meta[26] = ("Govt", "D")
    # deficit: write PS borrowing into a separate small block (col H needs %GDP; we have £m -> put £m in G, leave H manual-ish)
    # Simpler: dedicated Deficit sheet with the £m series and compute rolling 12m / GDP manually later.
    defi = wb.create_sheet("Deficit")
    defi["A1"]="Date"; defi["B1"]="PS Net Borrowing £m"; defi["C1"]="YoY %"
    for c in "ABC":
        defi[c+"1"].fill=HDR_FILL; defi[c+"1"].font=HDR_FONT
    dser = cache.get("deficit", [])
    dr=2; prev=None
    for d_iso,v in dser:
        try: dt=datetime.fromisoformat(d_iso).date()
        except: continue
        defi.cell(row=dr,column=1,value=dt).number_format="yyyy-mm-dd"
        defi.cell(row=dr,column=2,value=float(v))
        if prev is not None and prev!=0:
            defi.cell(row=dr,column=3,value=f"=(B{dr}-B{dr-12})/ABS(B{dr-12})").number_format="0.00%"
        prev=v; dr+=1
    driver_meta[27] = ("Deficit", "C")  # use YoY% as the driver rate proxy
    # interest/GDP manual
    ws = manual_sheet("Interest", "Interest/GDP %", 2.15, "ONS public sector debt interest / GDP")
    driver_meta[28] = ("Interest", "B")
    # liquidity manual
    ws = manual_sheet("Liquidity", "Liquidity Cover (receipts/interest)", 17.96, "Derived")
    driver_meta[29] = ("Liquidity", "B")
    # 10Y gilt
    ws,_ = make_series_sheet("Gilt10Y", cache.get("gilt10y", []), "10Y Gilt %")
    driver_meta[30] = ("Gilt10Y", "B")
    # CBBS manual
    ws = manual_sheet("CBBS", "BoE APF % GDP", 46.73, "Bank of England APEXLPMA (APF stock / GDP)")
    driver_meta[31] = ("CBBS", "B")

    # ---- add scoring tables to each data sheet (cols F/G) ----
    score_ranges = {}
    for (row, group, name, code, table, source, manual) in DRIVERS:
        sheet_name = driver_meta[row][0]
        ws = wb[sheet_name]
        th_rng, sc_rng = add_score_table(ws, 6, 1, table, f"{code} threshold")
        score_ranges[row] = (th_rng, sc_rng)

    # ---- build the dashboard ----
    build_dashboard(dash, driver_meta, score_ranges, cache)

    # ---- Sources & Cycles & GDP sheets ----
    build_sources(wb, cache)
    build_cycles(wb)
    build_gdp_quarterly(wb, cache)

    # order sheets: dashboard first
    wb.move_sheet("UK Endo' Score", offset=-len(wb.sheetnames))
    wb.active = 0

    wb.save(OUT)
    print(f"✓ Wrote {os.path.basename(OUT)}  ({len(wb.sheetnames)} sheets)")


def build_dashboard(dash, driver_meta, score_ranges, cache):
    # Title
    dash["B2"] = "UK Endogenous Driver Analysis"
    dash["B2"].font = TITLE_FONT
    dash["C2"] = "Driver"; dash["D2"] = "Code"; dash["E2"] = "Rate"
    dash["F2"] = "Score I/D"; dash["G2"] = "Total"; dash["I2"] = "State"; dash["J2"] = "Comment"; dash["K2"] = "Source"
    for c in ("C2","D2","E2","F2","G2","I2","J2","K2"):
        dash[c].font = HDR_FONT
    dash["H42"] = "Data source: ONS · FRED · Bank of England. Refresh via refresh_uk_data.py"
    dash["H42"].font = SUB_FONT
    dash["E44"] = "As-of:"; dash["F44"] = datetime.now().date()

    # drivers
    for (row, group, name, code, table, source, manual) in DRIVERS:
        if group:
            dash.cell(row=row, column=2, value=group).font = GROUP_FONT
        dash.cell(row=row, column=3, value=name)
        dash.cell(row=row, column=4, value=code)
        sheet_name, vcol = driver_meta[row]
        # E = latest value
        dash.cell(row=row, column=5,
                  value=f"=LOOKUP(9.9E+307,'{sheet_name}'!{vcol}:{vcol})")
        # number format for percent-ish series
        if code in ("CPI","PPI","M4","IR") and code not in ("BP",):
            dash.cell(row=row, column=5).number_format = "0.00"
        # F = score via helper table on the data sheet
        th_rng, sc_rng = score_ranges[row]
        dash.cell(row=row, column=6,
                  value=f"=LOOKUP(E{row},'{sheet_name}'!{th_rng},'{sheet_name}'!{sc_rng})")
        dash.cell(row=row, column=6).fill = SCORE_FILL
        dash.cell(row=row, column=7, value=10)  # total scale
        dash.cell(row=row, column=9, value="MANUAL input" if manual else "live")
        dash.cell(row=row, column=11, value=source)

    # subtotals
    dash["F10"] = "=SUM(F5:F9)";   dash["G10"] = "=SUM(G5:G9)"
    dash["F21"] = "=SUM(F16:F20)"; dash["G21"] = "=SUM(G16:G20)"
    dash["F33"] = "=SUM(F26:F32)"; dash["G33"] = "=SUM(G26:G32)"
    for c in ("F10","F21","F33"):
        dash[c].font = Font(bold=True); dash[c].fill = SCORE_FILL

    # scale rows (mirror US file)
    dash["F36"] = "High Scale"; dash["G36"] = "=G10+G12+G14+G21+G23+G33"
    dash["F37"] = "Low Scale";  dash["G37"] = -150
    dash["F38"] = "Full Scale"; dash["G38"] = "=G36-G37"
    dash["F39"] = "Half Scale"; dash["G39"] = "=G36-G38/2"
    dash["H37"] = "SCORE";      dash["H38"] = "=F10+F12+F14+F21+F23+F33"
    for r in (36,37,38,39):
        dash.cell(row=r, column=6).font = Font(bold=True)
    dash["H38"].font = Font(bold=True, size=14, color="C00000")

    # column widths
    for col, w in {"A":3,"B":26,"C":40,"D":8,"E":11,"F":10,"G":8,"H":10,"I":16,"J":30,"K":40}.items():
        dash.column_dimensions[col].width = w

    # GDP growth row
    dash["B42"] = "GDP Growth"; dash["C42"] = "Real GDP Growth (annual %)"
    lg = latest(cache.get("earnings", []))  # placeholder; real GDP below
    dash["E42"] = 0.5  # placeholder long-term avg


def build_sources(wb, cache):
    ws = wb.create_sheet("Sources")
    ws["A1"] = "UK Endogenous Driver Analysis — Data Sources"; ws["A1"].font = TITLE_FONT
    rows = [
        ("Driver", "Source", "Series ID", "Frequency", "Notes"),
        ("CPI", "ONS", "D7G7 (mm23)", "Monthly", "CPI all-items annual rate %"),
        ("Core CPI", "ONS", "DKO8 (mm23)", "Monthly", "CPI excl. energy/food/alcohol/tobacco"),
        ("PPI Output", "ONS", "GB7S (ppi)", "Monthly", "Manufactured products output index"),
        ("PPI Input", "ONS", "GHIK (ppi)", "Monthly", "Materials & fuels input index"),
        ("Unemployment", "ONS", "MGSX (lms)", "Monthly", "Unemployment rate 16+ SA %"),
        ("Avg Earnings", "ONS", "KAC2 (emp)", "Monthly", "AWE total pay YoY %"),
        ("Debt/GDP", "ONS", "A3PW (pusf)", "Monthly", "General govt gross debt % GDP (Maastricht)"),
        ("PSND % GDP", "ONS", "HF6X (pusf)", "Monthly", "Public sector net debt excl. banks"),
        ("PS Borrowing", "ONS", "J5II (pusf)", "Monthly", "Net borrowing £m (signed)"),
        ("10Y Gilt", "FRED", "IRLTLT01GBM156N", "Monthly", "Long-term govt bond yield %"),
        ("Bank Rate", "FRED", "IRSTCI01GBM156N", "Monthly", "BoE policy rate %"),
        ("Consumer Conf.", "FRED", "CSCICP02GBM460S", "Monthly", "OECD consumer opinion balance"),
        ("Broad Money", "FRED", "MANMM101GBM189S", "Monthly", "Broad money £ (M1 proxy)"),
        ("Mfg/Services PMI", "S&P Global / CIPS", "—", "Monthly", "MANUAL — licensed, no free API"),
        ("Housing Approvals", "DLUHC", "—", "Monthly", "MANUAL"),
        ("BoE Balance Sheet", "Bank of England", "APEXLPMA", "Weekly", "MANUAL — APF stock / GDP"),
    ]
    for r, row in enumerate(rows, start=3):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            if r == 3:
                cell.font = HDR_FONT; cell.fill = HDR_FILL
    for col, w in {"A":22,"B":26,"C":20,"D":12,"E":44}.items():
        ws.column_dimensions[col].width = w
    fetched = cache.get("_meta", {}).get("fetched", "")
    ws.cell(row=len(rows)+5, column=1, value=f"Cache last refreshed: {fetched}").font = SUB_FONT


def build_cycles(wb):
    ws = wb.create_sheet("Cycles")
    ws["B3"] = "UK GDP Contractions (recessions)"
    ws["B3"].font = GROUP_FONT
    ws["B4"] = "Year Started"; ws["C4"] = "Year Ended"; ws["D4"] = "Length (quarters)"
    for c in ("B4","C4","D4"):
        ws[c].font = HDR_FONT; ws[c].fill = HDR_FILL
    recessions = [
        (1973,1975,5),(1979,1981,5),(1990,1991,3),(2008,2009,4),(2020,2020,2),(2022,2024,0),
    ]
    r = 5
    for ys, ye, q in recessions:
        ws.cell(row=r, column=2, value=ys); ws.cell(row=r, column=3, value=ye)
        ws.cell(row=r, column=4, value=q if q else "—")
        r += 1
    ws.cell(row=r+1, column=2, value="Source: ONS GDP quarterly series").font = SUB_FONT
    for col, w in {"B":16,"C":16,"D":18}.items():
        ws.column_dimensions[col].width = w


def build_gdp_quarterly(wb, cache):
    ws = wb.create_sheet("GDP Quarterly")
    ws["A1"] = "Period"; ws["B1"] = "UK GDP (£m, current)"
    for c in ("A1","B1"):
        ws[c].font = HDR_FONT; ws[c].fill = HDR_FILL
    # We don't have a clean UK nominal GDP series in cache; leave a stub note
    ws["A2"] = "—"; ws["B2"] = "Add ONS GDP series (e.g. YBHA) to refresh_uk_data.py"
    ws["A2"].font = SUB_FONT
    ws.column_dimensions["A"].width = 14
    ws.column_dimensions["B"].width = 22


if __name__ == "__main__":
    build()
