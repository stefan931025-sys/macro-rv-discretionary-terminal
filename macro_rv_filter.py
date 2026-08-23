import pandas as pd

class MacroRelativeValueFilter:
    """
    Evaluates quantitative Stat-Arb Z-score divergences against discretionary
    fundamental and macro parameters before trade execution.
    """
    def __init__(self, pair_ticker: str, current_zscore: float, spread_mean: float):
        self.pair_ticker = pair_ticker
        self.current_zscore = current_zscore
        self.spread_mean = spread_mean

    def assess_pair(self, earnings_imminent: bool, structural_break_risk: bool, macro_tailwind: str) -> dict:
        action = "HOLD / MONITOR"
        trade_size_pct = 0.0

        # Discretionary overlay logic to prevent trading into structural breaks or binary events
        if abs(self.current_zscore) >= 2.0:
            if earnings_imminent:
                action = "REJECT (Imminent Binary Event Risk)"
            elif structural_break_risk:
                action = "REJECT (Potential Structural Regime Shift)"
            else:
                direction = "LONG SPREAD" if self.current_zscore < -2.0 else "SHORT SPREAD"
                if macro_tailwind.upper() == "ALIGNED":
                    action = f"EXECUTE {direction} (Full Position)"
                    trade_size_pct = 1.0
                else:
                    action = f"EXECUTE {direction} (Half Position - Macro Neutral)"
                    trade_size_pct = 0.5

        return {
            "Pair": self.pair_ticker,
            "Z-Score": round(self.current_zscore, 2),
            "Trade_Action": action,
            "Allocation_Scale": f"{trade_size_pct:.0%}"
        }

if __name__ == "__main__":
    rv_filter = MacroRelativeValueFilter("ASML / AMAT", current_zscore=-2.45, spread_mean=0.0)
    decision = rv_filter.assess_pair(
        earnings_imminent=False,
        structural_break_risk=False,
        macro_tailwind="ALIGNED"
    )
    
    print("--- Macro RV Discretionary Decision ---")
    for k, v in decision.items():
        print(f"{k}: {v}")
