# Macro Relative Value Discretionary Terminal

[![Macro RV CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A discretionary relative value desk decision-support terminal evaluating quantitative statistical arbitrage Z-score pair divergences against macro catalysts, fundamental earnings risk, and structural regime shifts.

---

## Core Strategy & Architecture

1. **Statistical Screener:** Monitors cointegration residuals and flags $Z\text{-score}$ spread divergences ($\vert{}Z\vert{} \ge 2.0$).
2. **Fundamental & Macro Overlay:** Filters execution signals through binary event calendars (imminent earnings, regulatory actions) and macro factor tailwind alignment.
3. **Execution Decision Engine:** Converts raw mean-reversion signals into actionable risk allocations (Full Position, Half Position, or Rejection due to structural break risk).

---

## Mathematical Specifications

### 1. Macro-Adjusted Spread Divergence
$$Z_t^{\text{macro}} = \frac{(Y_t - \beta X_t) - \mu_t}{\sigma_t} \cdot w_{\text{macro}}$$
Where $w_{\text{macro}}$ penalizes positioning when macro factor volatility or earnings event risk is elevated.

---

## System Architecture & Data Flow

