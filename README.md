# Macro Relative Value Discretionary Terminal

[![Macro Relative Value Discretionary Terminal CI](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal/actions/workflows/ci.yml/badge.svg)](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal/actions/workflows/ci.yml)

![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Description:**
Discretionary relative value desk evaluating quantitative statistical arbitrage Z-score pair divergences against macro catalysts, fundamental earnings risk, and structural regime shifts.

## 📌 Architecture & Strategy

1. **Statistical Screener:** Monitors pair cointegration and flags Z-score spread divergences ($>= |2.0|$).
2. **Fundamental & Macro Overlay:** Filters execution through binary event calendars (imminent earnings, regulatory actions) and macro tailwind alignment.
3. **Execution Decision Engine:** Converts raw mean-reversion signals into actionable risk allocations (Full Position, Half Position, or Rejection due to structural break risk).

## 🛠 Quickstart

```bash
git clone [https://github.com/stefan931025-sys/macro-rv-discretionary-terminal.git](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal.git)
cd macro-rv-discretionary-terminal
python macro_rv_filter.py
