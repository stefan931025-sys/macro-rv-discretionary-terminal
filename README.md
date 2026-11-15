# Macro Relative Value Discretionary Terminal

![CI Workflow](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A discretionary relative value desk decision-support terminal evaluating quantitative statistical arbitrage z-score pair divergences against macro catalysts, fundamental earnings risk, and structural regime shifts.

## 🚀 Core Strategy & Architecture

* **Statistical Screener:** Monitors cointegration residuals and flags Z-score spread divergences ($\vert Z \vert \ge 2.0$).
* **Fundamental & Macro Overlay:** Filters execution signals through binary event calendars (imminent earnings, regulatory actions) and macro factor tailwind alignment.
* **Execution Decision Engine:** Converts raw mean-reversion signals into actionable risk allocations (Full Position, Half Position, or Rejection due to structural break risk).

---

## 📊 Mathematical Specifications

### 1. Macro-Adjusted Spread Divergence

$$Z_t^{\text{macro}} = \frac{(Y_t - \beta X_t) - \mu}{\sigma_t} \cdot w_{\text{macro}}$$

Where $w_{\text{macro}}$ penalizes positioning when macro factor volatility or earnings event risk is elevated.

---

## 📁 Repository Structure

```text
macro-rv-discretionary-terminal/
├── .devcontainer/             # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions automated test workflow
├── core/
│   └── rv_filter.py           # Macro-conditioned RV & spread filter modules
├── tests/
│   └── test_macro_rv.py       # Automated pytest suite
├── main.py                    # Main execution pipeline script
├── repo_auditor.py            # Static AST analysis governance tool
├── requirements.txt           # Python dependencies
└── README.md                  # System documentation
