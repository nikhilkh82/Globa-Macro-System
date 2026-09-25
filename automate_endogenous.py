# -*- coding: utf-8 -*-
"""
Automate USA_Endogenous_Driver_Analysis_June_2026.xlsx
======================================================
Turns the "US Endo' Score" dashboard into a live, self-calculating model:
  * Rate column (E) pulls the LATEST value from each indicator's data sheet.
  * Score column (F) is computed via LOOKUP() against embedded ascending
    threshold/score tables (so scores update automatically).
  * Subtotals / scale / overall SCORE are existing formulas -> recalc on open.
  * Adds an "as-of" date stamp and STALE flags for the Govt balance-sheet rows
    (whose data only runs to 2017 Q2 in this workbook).

Implementation = direct xlsx zip/XML surgery (NO openpyxl round-trip) so that
all 52 charts, drawings, styles, web-extensions and printer settings are
preserved byte-for-byte.
"""

import zipfile
import shutil
import re
import os

SRC = "USA_Endogenous_Driver_Analysis_June_2026.xlsx"
DST = "USA_Endogenous_Driver_Analysis_Automated_June_2026.xlsx"

SCORE_XML = "xl/worksheets/sheet1.xml"      # "US Endo' Score"
SHARED_XML = "xl/sharedStrings.xml"

# Sheet name in formulas (the dashboard sheet contains an apostrophe)
SC = "'US Endo'' Score'"  # not needed, we edit that sheet itself
MACRO = "'US Macro_data_Summary 2015 to 2'"


# ----------------------------------------------------------------------------
# Scoring tables  ->  (threshold, score) pairs, ASCENDING by threshold.
# Designed/curated from each indicator's built-in scoring curve so the
# automated score applies that curve consistently.  Thresholds for the
# monthly %-change indicators are expressed in PERCENT (rate decimal * 100).
# ----------------------------------------------------------------------------
ISM    = [(30,-10),(35,-10),(38,-8),(42,-6),(45,-3),(48,0),(50,0),(52,2),(54,4),(56,6),(58,8),(60,10),(62,10),(65,10)]
NMI    = [(35,-10),(40,-8),(44,-5),(48,-2),(50,0),(52,2),(54,4),(56,5),(58,6),(60,8),(62,10),(65,10)]
UMCSI  = [(45,-8),(46,-7),(47,-6),(48,-5),(49,-4),(50,-3),(51,-2),(52,-1),(53,-1),(54,0),(55,10),(56,10),(57,9),(58,9),(59,8),(60,7),(61,6),(62,5),(63,-10),(64,-9),(65,-8),(66,-7),(67,-6),(68,-5),(69,-4),(70,-3),(71,-2),(72,-1),(73,-1),(74,0),(75,0),(76,1),(77,1),(78,2),(79,2),(80,3),(81,3),(82,4),(83,4),(84,5),(85,5),(86,6),(87,6),(88,7),(89,7),(90,8),(91,8),(92,9),(93,9),(94,10),(95,10),(96,-5),(97,-5),(98,-6),(99,-6),(100,-7),(101,-8),(102,-9),(103,-9),(104,-10),(105,-10)]
PERMIT = [(400,10),(500,10),(600,10),(700,7),(800,-8),(900,-5),(1000,-3),(1100,0),(1200,2),(1300,3),(1400,4),(1500,5),(1600,8),(1700,9),(1800,10),(1900,-7),(2000,-9),(2100,-10),(2200,-10),(2300,-10),(2400,-10)]
CPI    = [(-0.7,10),(-0.6,10),(-0.5,8),(-0.4,6),(-0.3,-10),(-0.2,-8),(-0.1,-6),(0,0),(0.3,0),(0.4,4),(0.6,6),(0.8,8),(1,10),(1.2,6),(1.4,3)]
CORECPI= [(-0.35,10),(-0.3,9),(-0.25,8),(-0.2,7),(-0.15,-10),(-0.1,-8),(-0.05,-8),(0,-4),(0.2,0),(0.4,4),(0.6,6),(0.8,8),(1,10),(1.2,6),(1.4,3)]
PPI    = [(-1.25,10),(-1,10),(-0.75,-8),(-0.5,-4),(-0.25,-2),(0,0),(0.25,0),(0.5,2),(0.75,4),(1,8),(1.5,10),(1.75,6),(2,3)]
COREPPI= [(-1.25,10),(-1,10),(-0.75,6),(-0.5,-10),(-0.25,-8),(0,-6),(0.25,0),(0.5,6),(0.75,8),(1,10),(1.5,10),(1.75,6),(2,3)]
NFP    = [(-0.6,10),(-0.5,10),(-0.4,10),(-0.3,8),(-0.2,-10),(-0.1,-8),(0,-6),(0.1,3),(0.2,5),(0.3,7),(0.4,4),(0.5,2)]
M2     = [(-50,10),(-40,10),(-30,10),(-20,10),(-15,8),(-10,6),(-5,4),(0,4),(10,4),(15,6),(20,8),(30,10),(40,6),(50,4)]
IR     = [(-60,-10),(-50,-10),(-40,-9),(-30,-8),(-20,7),(-15,5),(-10,3),(-5,0),(0,0),(5,-3),(10,-6),(15,-9),(20,-10),(30,0),(40,0),(50,0),(60,0)]
T10    = [(0,10),(0.01,10),(0.02,8),(0.03,6),(0.04,4),(0.05,2),(0.06,0),(0.07,-1),(0.08,-2),(0.09,-3),(0.1,-4),(0.11,-5),(0.12,-6),(0.13,-7),(0.14,-8),(0.15,-9),(0.16,-10)]
DEBT   = [(0,0),(5,1),(10,1),(15,2),(20,2),(25,3),(30,3),(35,4),(40,4),(45,5),(50,5),(55,6),(60,6),(65,7),(70,7),(75,8),(80,8),(85,9),(90,9),(95,10),(100,10)]
DEFICIT= [(-10,10),(-9.5,10),(-9,9),(-8.5,9),(-8,8),(-7.5,8),(-7,7),(-6.5,7),(-6,6),(-5.5,6),(-5,5),(-4.5,5),(-4,4),(-3.5,4),(-3,3),(-2.5,3),(-2,2),(-1.5,2),(-1,1),(-0.5,1),(0,0),(0.5,-1),(1,-1),(1.5,-2),(2,-2),(2.5,-3),(3,-3),(3.5,-4),(4,-4),(4.5,-5),(5,-5),(5.5,-6),(6,-6),(6.5,-7),(7,-7),(7.5,-8),(8,-8),(8.5,-9),(9,-9),(9.5,-10),(10,-10)]
INTEREST=[(0,0),(0.5,-2),(1,-4),(1.5,-6),(2,-8),(2.5,-10),(3,-10),(3.5,-10),(4,-10),(4.5,-10),(5,-10)]
LIQ    = [(0,-10),(1,-9),(2,-8),(3,-7),(4,-6),(5,-5),(6,-4),(7,-3),(8,-2),(9,-1),(10,0),(11,2),(12,4),(13,6),(14,8),(15,10)]
CBBS   = [(0,0),(5,1),(10,1),(15,2),(20,2),(25,3),(30,3),(35,4),(40,4),(45,5),(50,5),(55,6),(60,6),(65,7),(70,7),(75,8),(80,8),(85,9),(90,9)]

# ----------------------------------------------------------------------------
# Helper-table placement on the score sheet.
# Layout (ascending threshold / score pairs) in columns R:S onward, one block
# per driver, stacked vertically starting row 45.  Col R = threshold, S=score.
# ----------------------------------------------------------------------------
HELPER_START_ROW = 45
HELPER_COL_TH = "R"     # 18
HELPER_COL_SC = "S"     # 19

# Each driver: (label, table, [the two columns where its rate/score sit on the dash])
# rate-pull formula + the helper block reference is derived below.
DRIVERS = [
    # row5: ISM mfg  -> last level in ISM!B:B
    ("ISM_mfg",      ISM,    5,  "rate", "LOOKUP(9.9E+307,ISM!B:B)"),
    ("NMI_services", NMI,    6,  "rate", "LOOKUP(9.9E+307,NMI!B:B)"),
    ("UMCSI",        UMCSI,  7,  "rate", "LOOKUP(9.9E+307,UMCSI!B:B)"),
    ("Permits",      PERMIT, 8,  "rate", "LOOKUP(9.9E+307,PermitsSA!B:B)"),
    ("M2",           M2,    12,  "rate", "LOOKUP(9.9E+307,M2!F:F)"),
    ("FedFunds",     IR,    14,  "rate", f"LOOKUP(9.9E+307,{MACRO}!B:B)"),
    ("CPI",          CPI,   16,  "pct",  "LOOKUP(9.9E+307,CPIAUCSL!C:C)*100"),
    ("CoreCPI",      CORECPI,17, "pct",  "LOOKUP(9.9E+307,CPILFESL!C:C)*100"),
    ("PPI",          PPI,   18,  "pct",  "LOOKUP(9.9E+307,PPIFGS!D:D)*100"),
    ("CorePPI",      COREPPI,19, "pct",  "LOOKUP(9.9E+307,PPILFE!D:D)*100"),
    ("NFP",          NFP,   23,  "pct",  "LOOKUP(9.9E+307,NFP!D:D)*100"),
    ("DebtGDP",      DEBT,  26,  "govt", "LOOKUP(9.9E+307,Govt!D:D)*100"),
    ("Deficit",      DEFICIT,27, "govt", "LOOKUP(9.9E+307,Govt!H:H)*100"),
    ("Interest",     INTEREST,28,"govt", "LOOKUP(9.9E+307,Govt!J:J)*100"),
    ("Liquidity",    LIQ,   29,  "govt", "LOOKUP(9.9E+307,Govt!K:K)"),
    ("T10",          T10,   30,  "rate", "LOOKUP(9.9E+307,'T10%'!B:B)"),
    ("CBBS",         CBBS,  31,  "rate", "LOOKUP(9.9E+307,CBBS!D:D)*100"),
]


def col_to_num(letters):
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch.upper()) - 64)
    return n


def num_to_col(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


# ----------------------------------------------------------------------------
# XML cell builders
# ----------------------------------------------------------------------------
def xml_num_cell(ref, style, formula):
    """A numeric/formula cell that keeps its style and sets a formula (no cached value)."""
    return f'<c r="{ref}" s="{style}"><f>{formula}</f></c>'


def xml_const_num_cell(ref, style, value):
    return f'<c r="{ref}" s="{style}"><v>{value}</v></c>'


def xml_str_cell(ref, style, si_index):
    return f'<c r="{ref}" s="{style}" t="s"><v>{si_index}</v></c>'


# ----------------------------------------------------------------------------
# Step 1: load source files
# ----------------------------------------------------------------------------
shutil.copy(SRC, DST)
zin = zipfile.ZipFile(SRC, "r")
parts = {name: zin.read(name) for name in zin.namelist()}
zin.close()

score_xml = parts[SCORE_XML].decode("utf-8")
shared_xml = parts[SHARED_XML].decode("utf-8")

# ----------------------------------------------------------------------------
# Step 2: append new shared strings for labels; record their indices
# ----------------------------------------------------------------------------
m = re.search(r'uniqueCount="(\d+)"', shared_xml)
unique = int(m.group(1))
ss_base_unique = unique  # original count, captured before any si_for() increments
# Parse existing string texts to avoid duplicates (simple <t> extraction)
existing = {}
for i, sim in enumerate(re.finditer(r'<si>(.*?)</si>', shared_xml, re.S)):
    tm = re.search(r'<t[^>]*>(.*?)</t>', sim.group(1), re.S)
    if tm:
        existing[tm.group(1)] = i

new_strings = [
    "Automated model \u2013 scores calculated from embedded scoring tables",
    "Data as-of (latest monthly print):",
    "STALE \u2013 Govt balance-sheet data ends 2017 Q2; paste current Govt rows to refresh",
    "Driver", "Threshold", "Score", "Helper scoring tables (ascending)",
]

extra_si = []
def si_for(text):
    global unique
    if text in existing:
        return existing[text]
    extra_si.append(f'<si><t xml:space="preserve">{text}</t></si>')
    existing[text] = unique
    unique += 1
    return existing[text]

label_idx = {s: si_for(s) for s in new_strings}
# NOTE: sharedStrings rewrite is deferred to the END (after all si_for() calls,
# including driver-name labels added during helper-table construction below).

# ----------------------------------------------------------------------------
# Step 3: build helper tables block XML, and record each driver's helper range.
# We render whole new <row> elements in columns R..S and a label in Q.
# These rows live BELOW the visible dashboard (row >= 45).
# ----------------------------------------------------------------------------
driver_range = {}  # name -> (th_range, sc_range) e.g. "$R$45:$R$58"

# Collect cells PER ROW to inject into the EXISTING rows. Rows 45..367 already
# exist in the sheet (it spans A1:DO536), so we must NOT create new <row>
# elements (that would duplicate row numbers and corrupt the file). We instead
# inject R/S cells into the existing rows. Map: rownum -> concatenated cell XML.
helper_cells_by_row = {}
r = HELPER_START_ROW
hdr_si = label_idx["Helper scoring tables (ascending)"]
helper_cells_by_row[r] = f'<c r="Q{r}" t="s"><v>{hdr_si}</v></c>'
r += 1

for name, table, dashrow, kind, rate_formula in DRIVERS:
    first = r
    lab_si = si_for(name)
    for i, (th, sc) in enumerate(table):
        cells = ""
        if i == 0:
            cells += f'<c r="Q{r}" t="s"><v>{lab_si}</v></c>'
        cells += f'<c r="{HELPER_COL_TH}{r}"><v>{th}</v></c>'
        cells += f'<c r="{HELPER_COL_SC}{r}"><v>{sc}</v></c>'
        helper_cells_by_row[r] = cells
        r += 1
    last = r - 1
    driver_range[name] = (f"${HELPER_COL_TH}${first}:${HELPER_COL_TH}${last}",
                          f"${HELPER_COL_SC}${first}:${HELPER_COL_SC}${last}")

# ----------------------------------------------------------------------------
# Step 4: replace dashboard E (rate) and F (score) cells with formulas.
# We edit existing <c ...> elements for each driver row, preserving their
# style attribute (s="...").  Strategy: regex-replace the specific cell.
# ----------------------------------------------------------------------------
def replace_cell(xml, ref, new_cell_xml):
    # match the existing cell for this exact ref (with optional style and content)
    pat = re.compile(r'<c r="' + ref + r'"[^>]*?(?:/>|>.*?</c>)')
    if not pat.search(xml):
        raise RuntimeError(f"cell {ref} not found in score sheet")
    return pat.sub(lambda m: new_cell_xml, xml, count=1)

# First, capture original styles so formulas keep their formatting.
style_cache = {}
for _, _, dashrow, _, _ in DRIVERS:
    for col in ("E", "F"):
        ref = f"{col}{dashrow}"
        mm = re.search(r'<c r="' + ref + r'" s="(\d+)"', score_xml)
        style_cache[ref] = mm.group(1) if mm else "0"

# Build rate + score formulas per driver and apply.
for name, table, dashrow, kind, rate_formula in DRIVERS:
    e_ref = f"E{dashrow}"
    f_ref = f"F{dashrow}"
    e_style = style_cache[e_ref]
    f_style = style_cache[f_ref]
    th_rng, sc_rng = driver_range[name]
    score_formula = f"LOOKUP({e_ref},{th_rng},{sc_rng})"
    score_xml = replace_cell(score_xml, e_ref, xml_num_cell(e_ref, e_style, rate_formula))
    score_xml = replace_cell(score_xml, f_ref, xml_num_cell(f_ref, f_style, score_formula))

# ----------------------------------------------------------------------------
# Step 5: add an "as-of" date stamp + automation banner + STALE flags.
# IMPORTANT: the sheet already has rows 1..536 defined, so we must NOT insert new
# <row> elements (that would create duplicate row numbers and corrupt the file).
# Instead we inject cells into FREE columns (M-P / 13-16) of EXISTING rows.
#   Row 39 (header area, free)  M39: "Data as-of", N39: =MAX(latest monthly dates)
#   Row 40                       M40: banner string
#   Govt rows 26-29              M-col: STALE flag (col M is free on those rows)
# ----------------------------------------------------------------------------
def inject_cell_into_row(xml, rownum, cell_xml):
    """Insert cell_xml into the existing <row r=rownum> just before its </row>
    (or convert a self-closing row to a paired row). Columns must be in order;
    we append at the end which is safe since we target high columns (M+)."""
    # paired row
    pat = re.compile(r'(<row r="' + str(rownum) + r'"[^>]*>)(.*?)(</row>)', re.S)
    m = pat.search(xml)
    if m:
        return xml[:m.start()] + m.group(1) + m.group(2) + cell_xml + m.group(3) + xml[m.end():]
    # self-closing row -> convert
    pat2 = re.compile(r'(<row r="' + str(rownum) + r'"[^>]*)/>')
    m2 = pat2.search(xml)
    if m2:
        return xml[:m2.start()] + m2.group(1) + ">" + cell_xml + "</row>" + xml[m2.end():]
    raise RuntimeError(f"row {rownum} not found for cell injection")

date_si = label_idx["Data as-of (latest monthly print):"]
banner_si = label_idx["Automated model \u2013 scores calculated from embedded scoring tables"]
stale_si = label_idx["STALE \u2013 Govt balance-sheet data ends 2017 Q2; paste current Govt rows to refresh"]

# Date stamp: label in M39, formula in N39
score_xml = inject_cell_into_row(score_xml, 39,
    f'<c r="M39" t="s"><v>{date_si}</v></c>'
    f'<c r="N39" s="0"><f>MAX(UMCSI!A:A,ISM!A:A,NMI!A:A,PermitsSA!A:A,M2!A:A,CPIAUCSL!A:A,NFP!A:A)</f></c>')
# Banner in M40
score_xml = inject_cell_into_row(score_xml, 40, f'<c r="M40" t="s"><v>{banner_si}</v></c>')

# STALE flags on Govt rows 26-29 (Debt/GDP, Deficit, Interest, Liquidity) in column M
for gr in (26, 27, 28, 29):
    score_xml = inject_cell_into_row(score_xml, gr, f'<c r="M{gr}" t="s"><v>{stale_si}</v></c>')


# ----------------------------------------------------------------------------
# Step 6: inject helper-table cells into the EXISTING rows (45..367) in columns
# Q/R/S. These rows already exist (sheet spans to row 536), so we add cells
# rather than whole rows, avoiding duplicate row numbers.
# ----------------------------------------------------------------------------
for rownum, cells_xml in sorted(helper_cells_by_row.items()):
    score_xml = inject_cell_into_row(score_xml, rownum, cells_xml)

# ----------------------------------------------------------------------------
# Step 6b: NOW that every si_for() call is done, rewrite sharedStrings with the
# final uniqueCount and the collected <si> entries appended before </sst>.
# ----------------------------------------------------------------------------
if extra_si:
    shared_xml = shared_xml.replace(
        f'uniqueCount="{ss_base_unique}"',
        f'uniqueCount="{unique}"'
    )
    shared_xml = shared_xml.replace("</sst>", "".join(extra_si) + "</sst>")

# ----------------------------------------------------------------------------
# Step 7: write everything back into the destination zip (all other parts copied)
# ----------------------------------------------------------------------------
parts[SCORE_XML] = score_xml.encode("utf-8")
parts[SHARED_XML] = shared_xml.encode("utf-8")

# remove any cached calcChain entries that reference our changed cells? calcChain is
# optional; Excel rebuilds it. Leave as-is (we kept it). Writing the zip:
if os.path.exists(DST):
    os.remove(DST)
zout = zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED)
for name, data in parts.items():
    zout.writestr(name, data)
zout.close()

print("WROTE", DST)
print("helper ranges:")
for name,(th,sc) in driver_range.items():
    print(f"  {name:14s} {th} / {sc}")
