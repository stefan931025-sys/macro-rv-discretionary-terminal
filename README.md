# Macro Relative Value Discretionary Terminal

![CI Workflow](https://github.com/stefan931025-sys/macro-rv-discretionary-terminal/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A discretionary relative value desk decision-support terminal evaluating quantitative statistical arbitrage $Z$-score pair divergences against macro catalysts, fundamental earnings risk, and structural regime shifts[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span).

## 🚀 Core Strategy & Architecture

1. **Statistical Screener:** Monitors cointegration residuals and flags $Z$-score spread divergences ($\vert{}Z\vert{} \geq 2.0$)[span_2](start_span)[span_2](end_span).
2. **Fundamental & Macro Overlay:** Filters execution signals through binary event calendars (imminent earnings, regulatory actions) and macro factor tailwind alignment[span_3](start_span)[span_3](end_span).
3. **Execution Decision Engine:** Converts raw mean-reversion signals into actionable risk allocations (Full Position, Half Position, or Rejection due to structural break risk)[span_4](start_span)[span_4](end_span).

---

## 📊 Mathematical Specifications

### 1. Macro-Adjusted Spread Divergence

$$Z_t^{\text{macro}} = \frac{(Y_t - \beta X_t) - \mu}{\sigma_t} \cdot w_{\text{macro}}$$

Where $w_{\text{macro}}$ penalizes positioning when macro factor volatility or earnings event risk is elevated[span_5](start_span)[span_5](end_span).

---

## 📁 Repository Structure

```text
macro-rv-discretionary-terminal/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── rv_filter.py   # Macro-conditioned RV & spread filter modules
├── tests/
│   └── test_macro_rv.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements.txt   # Python dependencies
└── README.md          # System documentation
