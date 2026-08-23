
---

### 2. `macro-rv-discretionary-terminal`

```markdown
# Macro Relative Value Discretionary Terminal

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Description:**  
Discretionary relative value desk evaluating quantitative statistical arbitrage Z-score pair divergences against macro catalysts, fundamental earnings risk, and structural regime shifts.

---

## 📌 Architecture & Strategy

1. **Statistical Screener:** Monitors pair cointegration and flags $Z$-score spread divergences ($\ge |2.0\sigma|$).
2. **Fundamental & Macro Overlay:** Filters execution through binary event calendars (imminent earnings, regulatory actions) and macro tailwind alignment.
3. **Execution Decision Engine:** Converts raw mean-reversion signals into actionable risk allocations (Full Position, Half Position, or Rejection due to structural break risk).

---

## 🛠️ Quickstart

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/macro-rv-discretionary-terminal.git](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal.git)
cd macro-rv-discretionary-terminal

# Run the discretionary pair filter
python macro_rv_filter.py
