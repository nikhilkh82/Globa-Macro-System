---
title: "Commodities — Supply, Demand & the Cycle"
aliases: ["Commodities - Supply, Demand & the Cycle"]
category: commodities
type: live-read
data_asof: 2026-09-24
summary: "The oil spike has broken: WTI $96.41 / Brent $114.89 (09-22), off $10.61 / $15.91 from the 15 Sep peak, spread −$18.48. Gasoline has NOT followed ($4.478, +41% YoY) while crude stocks built. Copper/gold longs crowded."
tags: ["commodities", "supply-demand", "inflation", "cycle", "contango"]
updated: 2026-09-25
data_vintage: "FRED daily crude to 2026-09-22, gasoline to 2026-09-21 · Explorer weekly COMMOD prices still to 2026-08-31 (workbook not updated) · COT to 2026-09-15 (report did not advance) · EIA stocks to 2026-09-18 · breakevens to 2026-09-23 (FRED T5YIE / deck) and 2026-09-24 (Explorer INFEXP:BE5, BE10) · PPI/CPI to 2026-08 · IMF monthly to 2026-07 · Explorer catalogue re-read at vhash eb2c482311b9, asof 2026-09-24, 427 series / 357,808 obs"
sources: 8
---

# Commodities — Supply, Demand & the Cycle

Gliner's Ch 10 is the book's longest. Its organising claim: commodities are the one product group where **physical supply and demand set the price**, so the analytical unit is the balance (production, consumption, inventory) rather than a discount rate.

## Where the complex sits now

Each row carries **its own observation date** — the daily crude feed is now three weeks fresher than the weekly workbook series, and that gap is itself part of the story of the last month.

| Commodity | Level | As of | 1-yr | Percentile of own history | Series |
|---|---|---|---|---|---|
| WTI crude (spot) | **$96.41** | 2026-09-22 | **+53.1%** | not recomputed † | `DCOILWTICO` |
| Brent crude (spot) | **$114.89** | 2026-09-22 | **+71.8%** | not recomputed † | `DCOILBRENTEU` |
| WTI − Brent | **−$18.48** | 2026-09-22 | — | not recomputed † | `DCOILWTICO − DCOILBRENTEU` |
| Henry Hub nat gas | $2.97 | 2026-09-15 | −1.0% | not recomputed † | `DHHNGSP` (not re-pulled ‡) |
| Copper (COMEX) | $6.6875/lb | 2026-08-31 | **+48.0%** | **100.0** | `COMMOD:COPPER` |
| Iron ore 62% | $96.05 | 2026-08-31 | −5.7% | 39.2 | `COMMOD:IRONORE` |
| Lumber | $569.00 | 2026-08-31 | +3.7% | 95.1 | `COMMOD:LUMBER` |
| IMF commodity index | 193.20 | 2026-07 | +16.6% | 96.0 | `AU:COMD` / `PALLFNFINDEXM` |
| PPI all commodities | 287.93 | 2026-08 | +9.9% | **99.9** | `PPIACO` |
| US gasoline | **$4.478** | 2026-09-21 | **+41.1%** | **99.3** | `LEI:GAS` / `GASREGW` |

*(The crude and gasoline rows supersede the 2026-09-19 readings — WTI $107.02 / Brent $130.80 / spread −$23.78 at 2026-09-15 and gasoline $4.319 at 2026-09-14. Those remain the correct prints for their dates and are listed in [[log]]; they are no longer current levels. The gasoline 1-yr is measured against $3.173 in the week of 2025-09-22 and the percentile is a rank of the current value in the series' own 1,878 weekly observations, both computed this session from `LEI:GAS`.)*

† The daily-crude percentiles this page carried (WTI 92.8, Brent 93.3, spread 5.5) were computed from FRED's full daily history, which this vault does not cache; the 2026-09-19 and 2026-09-24 refreshes both worked from verified prints, not from the full series, so neither could recompute them. Those three stamps belong to the **2026-09-09** prices and are not repeated as current readings above.

‡ `DHHNGSP` is not in today's macro evidence pack, so the Henry Hub row is **carried unchanged from 2026-09-15 and is not a current read** — it is listed as unresolved below. The nearest re-verified gas figure is the IMF monthly (`PNGASUSUSDM`): **$2.963/MMBtu for 2026-07, −10.5% YoY** — a different series on a different frequency, quoted here only as a sanity check on the level.

The Explorer's own weekly crude series **still did not move**: `COMMOD:WTI` $85.76 and `COMMOD:BRENT` $90.49, still stamped 2026-08-31 (86.8th / 84.6th percentile). The build itself is current, and it has since been re-run: the catalogue on disk now stamps **asof 2026-09-24, vhash `eb2c482311b9`, 427 series, 357,808 observations** (`Workbook Explorer/wb_explorer.json`, `built` 2026-09-25T10:09:58, re-read this session). That supersedes the **asof 2026-09-23 / vhash `750401593e26` / 357,797-observation** build this section was first written against — but only as metadata: every COMMOD row below is byte-identical across the two builds. So the **COMMOD weekly group is stale because its source workbook was not updated**, not because the data stopped. *(The series count fell from 456 in the 2026-09-19 build to 427, and is still 427 in the newer build; nothing in either refresh explains the drop, so it is listed as unresolved.)* The gap to the daily feed has **narrowed to $10.65 on WTI and $24.40 on Brent** (it was $21.26 / $40.31 on 2026-09-19) — narrowed by the daily price falling, not by the workbook advancing. **Quote the daily series for anything current** and treat the copper / iron ore / lumber rows above as almost four-week-old by construction.

Read together: **the complex is still expensive, but the energy spike has broken.** WTI has given back $10.61 and Brent $15.91 from their 15 Sep prints, taking the year-over-year rates from +68.1% / +92.7% down to **+53.1% / +71.8%** — still extreme, no longer accelerating. The daily WTI path out of the peak is unbroken: 107.02 (09-15) → 103.62 (09-16) → 103.21 (09-17) → 101.44 (09-18) → 96.97 (09-21) → 96.41 (09-22). Copper is still at the very top of its recorded range and producer prices sit at the 99.9th percentile, while iron ore — the most China-levered of the set — remains mid-range and *down* on the year. That split (Western industrial/energy strength, Chinese construction weakness) is still the honest shape of the cycle. **What is new is that the two energy legs have separated:** crude is falling while US retail gasoline is still climbing ($4.157 → $4.319 → $4.478 over three weeks), which is the ordinary refinery/retail lag and means the *consumer* energy shock is still being delivered after the *barrel* shock has begun to unwind. A live cross-check from the trading deck's own front-month feed agrees on direction: WTI **$93.92** and copper **$6.74** on 2026-09-24, with WTI −7.84% on the week (see [[Global Macro Trading Deck (July 2026)]]).

The policy backdrop changed in the same week the spike topped. Both major central banks tightened as the oil move ran: the **Fed raised 25bp to a 3.75–4.00% target range effective 2026-09-17** (the first hike of the cycle; funds 3.88%, from 3.63%, and still 3.88% on 2026-09-22), and the **ECB lifted its deposit rate to 2.50% effective 2026-09-16**. With August PPI all-commodities at +9.85% YoY the complex was the live inflation argument for both — **and the argument has since weakened at the front of the pipeline**: WTI is ~10% below the 15 Sep peak that triggered the moves, and ~7% below its level on 17 Sep, the day the Fed's hike took effect. See [[Central Banks — Policy Rates, Balance Sheets & the Global Stance]].

One correction carried from the 2026-09-19 read: the IMF commodity index had been carried at **167.47, +0.8% YoY**. The Explorer and FRED's `PALLFNFINDEXM` both return **193.20, +16.6% YoY** for 2026-07 — re-confirmed unchanged in today's 2026-09-24 rebuild (`AU:COMD` 193.2045, still a July observation). The old figure came from a stale workbook vintage, not from a subsequent fall.

## Supply drivers, demand drivers, ending stock

The book's framework, and what this platform can and cannot see:

- **Supply** — production capacity, spare capacity, OPEC policy, weather, geopolitics, extraction cost. *Not directly observable here.* No production, spare-capacity or rig-count feed.
- **Demand** — industrial activity, construction, EM growth. Observable via proxies: [[Leading Indicators]] ISM, China PMIs (`CNPMI:*`), [[Cyclical Commodities]]. US demand is currently firm, not fading — retail sales **+6.01% YoY** in August, payrolls **+162k** (3-month average +71k), industrial production **+1.42% YoY**, initial claims **196k** in the week of 12 September (all re-verified 2026-09-24 from `macro_pack.json`: `RSAFS`, `PAYEMS`, `INDPRO`, `ICSA`). The companion **+1.24% m/m** on retail sales is *not* in the pack — the pack carries `RSAFS` levels and calendar-keyed YoY only — and is taken from the rebuilt `Monthly Report/Business Cycle Dashboard.html` (asof 2026-09-24, Coincident table).
- **Ending stock** — the book's key balance metric (`ending stock = beginning stock + production − consumption`), driving the inventory-to-price relationship. **Correction (2026-09-19): this page previously said there is no inventory feed on this platform. There is** — the Explorer carries four weekly EIA stock series, advanced in today's build to **2026-09-18** (superseding the 2026-09-11 readings): commercial crude ex-SPR **426,398k bbl** (81.0th percentile of 2,295 weeks, **+2.8% YoY**), crude including SPR **710,950k bbl** (**3.4th** percentile, −13.4% YoY), gasoline **206,046k bbl** (25.0th, −4.9%) and distillate **107,431k bbl** (14.4th, −12.7%) — percentiles and year-over-year computed this session against the observation 364 days back. **The three-week commercial crude draw has reversed**: 428,910 (08-21) → 424,460 → 424,069 → 423,429 (09-11) → **426,398 (09-18)**, a +2,969k bbl build in the week crude fell $5. Distillate stopped building (107,859 → 107,431) and gasoline drew (207,732 → 206,046) even as pump prices rose. So the US inventory leg turned *looser* exactly as the price broke — consistent with the move, though this is a US-only stock series and cannot adjudicate a Brent-led market. What is still missing is production and consumption, so the identity above still cannot be closed and ending stock is not computable here. The closest adjacent series remains the inventory/sales channel documented in [[Inventory-to-Sales Ratios & the Inflation Channel (July 2026)]] — a *manufacturing/retail* balance, not a commodity one; its own headline (total business inventories/sales **1.30**, 2026-07) was re-verified today.

## Contango and backwardation — concept present, data absent

The book leans hard on term structure: **contango** (forward above spot — carry cost, storage glut, negative roll yield for a long) versus **backwardation** (forward below spot — scarcity, positive roll yield). This is how a commodity index can lose money while spot rises.

**This platform holds spot/front-month prices, weekly EIA stocks and CFTC open interest, but no futures curve.** Roll yield is therefore *not computable* here, and no page should imply a curve read. The WTI−Brent spread is a **location/quality spread** between two crude benchmarks — not a term-structure signal, and it should never be presented as one.

That warning still matters, because the spread remains extreme even after the spike broke: **−$18.48 on 2026-09-22** (96.41 − 114.89), against −$4.73 on the Explorer's weekly stamp of 2026-08-31 (85.76 − 90.49) and −$4.70 on the one before it, 2026-08-28 (83.40 − 88.10) — both recomputed this session as `COMMOD:WTI − COMMOD:BRENT` in the `eb2c482311b9` build. *(Correction made within this refresh: this sentence previously read "−$4.69 on 2026-08-06". **There is no 2026-08-06 observation in the aligned weekly series at all** — its August dates are 08-07, 08-14, 08-21, 08-28 and 08-31 — and no August spread is −$4.69; the 08-07 point is −$5.37. The −$4.73 half of the comparison was and remains correct.)* It has narrowed **$5.30 from the −$23.78 peak of 09-15** — and it narrowed the way it widened, seaborne-first: over 09-15 → 09-22 Brent fell **−$15.91** (130.80 → 114.89) against WTI's **−$10.61** (107.02 → 96.41). *(Supersedes the 2026-09-19 read's −$23.78 as the current level; the widening path recorded there — −$5.44 (09-02) → −$7.97 (09-03) → −$9.55 (09-04) → −$11.91 (09-08) → −$12.25 (09-09) → −$17.41 (09-10) → −$16.79 (09-11) → −$18.83 (09-14) → −$23.78 (09-15) — stands as the record of how it built.)* No percentile is quoted: the 5.5th-percentile reading (9,795 aligned daily observations since 1987) belongs to the **−$12.25 print of 09-09** and has not been recomputed at either −$23.78 or −$18.48, because this vault caches no daily crude history. The platform still cannot say *why* (no curve, no cargo data, and the EIA stock series above are US-only), so this is recorded as the shape of the move and nothing more.

## Positioning is the crowding check

CFTC net-speculative positioning as % of open interest (`COT:*`, report date **2026-09-15**, percentile over 872 weekly reports since 2010). The Explorer was rebuilt again on **2026-09-24**, but **the COT report did not advance** — 2026-09-15 is still the newest of the 872 reports — so every figure in this table is **re-verified today, not restated**, and none of it sees the week crude broke. Prior column is the 2026-09-08 report:

| Market | Net specs %OI | Percentile | Was (2026-09-08) |
|---|---|---|---|
| Gold | +56.19% | **99.0** | +56.41%, 99.5 |
| Copper | +25.96% | 95.8 | +31.09%, **99.6** |
| Silver | +24.41% | 59.8 | +25.23%, 63.1 |
| WTI crude | +6.95% | **7.6** | +7.04%, 7.9 |
| Natural gas | −12.18% | 34.7 | −12.05%, 35.3 |

Three things worth stating plainly:

1. **Copper's crowded long came off; gold's did not.** Copper net specs fell 31.09% → 25.96% of OI in one week, taking the percentile from 99.6 to 95.8 — the largest move in the set and a partial realisation of exactly the reversal risk the last two reads flagged. Gold barely moved (56.41% → 56.19%) and is still inside the top percentile of a 16-year history. In the book's Ch 5 framing that is still a *reversal-risk* flag on gold, not a sell signal, and this platform treats it the same way (crowded longs get trimmed, not reversed — see [[Position Sizing, Unit Size & Volatility Adjustment]]).
2. **Silver drifted back rather than joined.** Net specs 25.23% → 24.41% OI, percentile 63.1 → 59.8. The September read's "silver has joined, partially" is weaker again: mid-range positioning, no chase.
3. **WTI's divergence is now untestable, and that is the honest statement.** Specs sat at the **7.6th percentile** with positioning essentially flat on the week (7.04% → 6.95% OI) as at 09-15 — they did not chase the spike. Price has since given the spike back (**+53.1% YoY on 09-22**, from +68.1% on 09-15), but the positioning feed has not advanced past 09-15, so **whether specs were right, or simply absent, cannot be checked from this platform yet** — the first report that covers the break is not in. *(This supersedes the 2026-09-19 framing, "the price side widened again": it narrowed.)* That remains an observation, not a thesis — the platform has no curve data, and the US-only stock series cannot adjudicate a Brent-led move.

**Cross-check on that last point.** The second in-house COT dataset — the PTM workbook feed in `Macro COT Trades/cotexcel_latest.json` — was rebuilt again today (`generated` **2026-09-24 16:09**), but its WTI sheet **still ends at the 2026-09-01 report**, so its reading is unchanged for a third refresh: WTI net specs **+4.9% of OI at the 61st percentile** of 892 reports. The *level* agrees with `COT:WTI` to about two points; the *percentile* does not agree at all. So the extremity of the WTI reading is dataset-dependent (different history window and net-position definition) even though the level is not. Quote the level with confidence; treat "7th/8th percentile" as one dataset's view until the two feeds are reconciled. The workbook feed remains two reports behind the live one.

## The commodity → inflation channel

Commodities are the fastest-moving input to the inflation complex, which is why they lead in the [[Conference Board LEI & Leading-Lagging Map]]:

- CPI energy component **+16.05% YoY** (2026-08, 321.148), at the 99.5th percentile (`INFEXP:CPIENG` / `CPIENGSL`) — re-verified 2026-09-24 and unchanged; August is still the newest print, so **none of the CPI evidence yet contains either the spike or its unwind**
- Gasoline **+41.1% YoY** (2026-09-21, $4.478), 99.3rd percentile (`LEI:GAS` / `GASREGW`) — supersedes +35.3% at $4.319 on 09-14, and it is *still rising* three weeks running while crude falls
- PPI all commodities **+9.85% YoY** (2026-08, 287.928), **+0.96% m/m**, 99.9th percentile of its 1913→2026 history (`PPIACO`, re-verified today against `macro_pack.json`) — the August print accelerated from **+8.70%** in July on FRED's current vintage. (The Explorer's own `INFL:PPIACO` still stops at 2026-07 and computes +8.27% off an older base; the two feeds differ by ~0.4pp on *July*, not on August. The "286.83, +10.1%" this page carried before was the workbook's *June* observation mislabelled as current; June's level was 286.827.)

And it is visible in the headline index: CPI **+3.35% YoY** in August (334.131, `CPIAUCSL`), up from +3.30% in July. *(The 09-16 read carried +3.71% for August CPI; FRED's `CPIAUCSL` gives +3.35%, corrected here — the superseded reading is listed in [[log]].)* Quote it with its companions, honestly — headline CPI's own 3-month annualised rate is only **+0.18%**, because June fell 0.42% m/m, and **core** CPI is just **+2.45% YoY** (+0.29% m/m, 3-month annualised 1.97%, up from 1.64% in July but still below 2%). The YoY headline is where the energy impulse shows; the 3-month is where June's collapse still dominates; and core says the pass-through into the rest of the basket has so far been small. Core PCE, on the other hand, is **+3.34%** (2026-07, no August print yet).

Against that, breakevens sit at **2.34% / 2.35%** on **2026-09-23** — the 5-year from FRED's daily `T5YIE` (`macro_pack.json` `T5YIE.latest`, 2.34 at 2026-09-23) and the 10-year from the deck's own build (`macro_deck.json` `swaps.bei_now.b10` = 2.35, `infladj.now.bei` = 2.35). *(Corrected attribution: this page previously credited both numbers to the Explorer's `INFEXP:BE5` / `INFEXP:BE10`. Those are a weekly series and do not carry a 09-23 point.)* The Explorer's own copies have since taken a step of their own: `INFEXP:BE5` **2.33%** and `INFEXP:BE10` **2.33%** at **2026-09-24**, against 2.31% / 2.33% at 09-18. So the two feeds sit ~1bp apart on the 5-year and ~2bp on the 10-year — the basis noted on 2026-09-19 is narrow, not closed. The path is the point: the Explorer's 5-year went 2.40% (09-11) → **2.31% (09-18)** → **2.33% (09-24)**, with FRED's daily at 2.34% on 09-23 in between — it gave back 9bp while crude ran to $107 and has added 2–3bp back while crude fell $5. **Breakevens are not tracking the barrel in either direction** — which is what "anchored" looks like from the inside, and it is a stronger statement now that the shock has run both ways within nine sessions. Every tenor on every feed sits in a 2.33–2.35% band with crude still +53% on the year; the deck's 5y5y forward is **2.36%** (92.5th percentile of 10 years — high, but not moving). The energy shock is still being discounted as a level effect that fades, not as a change in the long-run inflation regime, and the price action since the hike has reinforced rather than tested that. The tension between a hot commodity/PPI complex and broadly anchored breakevens is the same tension noted in [[Monetary Policy Tools, Transmission & Communication]], with the policy response now delivered and the trigger now receding.

## What this refresh could not verify (2026-09-24)

This refresh supersedes the **2026-09-19** readings above; the 2026-09-19 list below is kept as the record of what was open then.

- **Henry Hub is carried, not verified.** `DHHNGSP` is absent from today's macro evidence pack, so the $2.97 / −1.0% row still belongs to **2026-09-15**. The only gas figure re-verified today is the IMF monthly `PNGASUSUSDM` ($2.963, 2026-07, −10.5% YoY) — a different series.
- **The daily-crude percentiles are still not recomputed** (WTI 92.8 / Brent 93.3 / spread 5.5 belong to the 2026-09-09 prints). This vault caches no daily crude history and the pack carries levels and 1-yr changes only, not distributions.
- **The COMMOD weekly group did not advance for a fourth build.** Copper, iron ore and lumber remain stamped 2026-08-31; their source workbook has not been updated.
- **The Explorer's series count fell 456 → 427** between the 2026-09-19 build and the 2026-09-24 one, and the newer `eb2c482311b9` build re-read this session is still 427 series / **357,808 observations** (counted this session from `wb_explorer.json`). Nothing read in either refresh explains which 29 series left; not diagnosed here.
- **The COT report did not advance.** `COT:*` still reports 2026-09-15, so no positioning data covers the week crude broke. The workbook feed (`cotexcel_latest.json`, rebuilt today) still ends 2026-09-01, and the two feeds still disagree on the WTI percentile (7.6th vs 61st) — flagged, not resolved.
- **No futures curve** — unchanged. Roll yield remains uncomputable here and the contango/backwardation section stays conceptual.
- **Copper's correlation with the S&P 500** was again not recomputed and is not quoted.
- **No September inflation prints exist yet.** CPI, core CPI, CPI-energy and PPI are all still August observations, so the consumer-price evidence on this page contains neither the spike nor its unwind. (The Cleveland Fed nowcast in the Explorer, `INFEXP:CFNOW`, puts September headline CPI at **3.57%** and core at **2.39%** — a model, not a print, and not used above.)

## What this refresh could not verify (2026-09-19)

This refresh supersedes the **2026-09-16** readings on this page; the superseded values are listed in [[log]].

- **No futures curve** — unchanged. Roll yield remains uncomputable here and the contango/backwardation section stays conceptual.
- **Inventory: corrected, not missing.** The EIA weekly stock series are on the platform (above), current to 2026-09-11. What is still absent is production and consumption, so the ending-stock identity still cannot be closed.
- **The daily crude percentiles were not recomputed** (WTI 92.8 / Brent 93.3 / spread 5.5). Those stamps belong to the 2026-09-09 prints; this vault caches no daily crude history and FRED was not called this session.
- **The COMMOD weekly group did not advance.** Today's Explorer build is current but its source workbook was not updated, so copper, iron ore and lumber are still stamped 2026-08-31.
- **Copper's correlation with the S&P 500** was again not recomputed; the figure is no longer quoted here.
- **The two in-house COT feeds still disagree on the WTI percentile** (7.6th vs 61st) — flagged above, not resolved; the workbook feed is now two reports behind the live one.

Related: [[Energy, Metals & Agriculture — the Sub-Complexes]] · [[Cyclical Commodities]] · [[Commitment of Traders (COT)]] · [[Inventory-to-Sales Ratios & the Inflation Channel (July 2026)]] · [[Global Macro Trading (Gliner) — Curriculum Map]]
