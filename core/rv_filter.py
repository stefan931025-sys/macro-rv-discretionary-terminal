import argparse
import numpy as np
import pandas as pd
import yfinance as yf

class MacroRelativeValueFilter:
    """
    Live Statistical Arbitrage & Discretionary Macro Filter Program.
    """
    def __init__(self, ticker_a: str, ticker_b: str):
        self.ticker_a = ticker_a
        self.ticker_b = ticker_b

    def calculate_live_zscore(self, lookback: int = 60) -> float:
        data = yf.download([self.ticker_a, self.ticker_b], period="6m", progress=False)['Close']
        data = data.dropna()
        
        spread = np.log(data[self.ticker_a]) - np.log(data[self.ticker_b])
        rolling_mean = spread.rolling(window=lookback).mean()
        rolling_std = spread.rolling(window=lookback).std()
        
        zscore = (spread - rolling_mean) / rolling_std
        return float(zscore.iloc[-1])

    def assess_pair(self, earnings_risk: bool, structural_break: bool, macro_alignment: str) -> dict:
        zscore = self.calculate_live_zscore()
        action = "MONITOR / HOLD"
        allocation = 0.0

        if abs(zscore) >= 2.0:
            if earnings_risk:
                action = "REJECT (Imminent Binary Event Risk)"
            elif structural_break:
                action = "REJECT (Structural Regime Shift Detected)"
            else:
                direction = f"LONG {self.ticker_a} / SHORT {self.ticker_b}" if zscore < -2.0 else f"SHORT {self.ticker_a} / LONG {self.ticker_b}"
                if macro_alignment.upper() == "ALIGNED":
                    action = f"EXECUTE {direction} (100% Size)"
                    allocation = 1.0
                else:
                    action = f"EXECUTE {direction} (50% Size - Neutral Macro)"
                    allocation = 0.5

        return {
            "Pair": f"{self.ticker_a} / {self.ticker_b}",
            "Live_Z_Score": round(zscore, 2),
            "Earnings_Risk": earnings_risk,
            "Structural_Break": structural_break,
            "Macro_Alignment": macro_alignment,
            "Trade_Action": action,
            "Target_Allocation": f"{allocation:.0%}"
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Macro RV Discretionary Terminal")
    parser.add_argument("--ticker_a", type=str, default="AMD", help="Primary Equity/Asset Ticker")
    parser.add_argument("--ticker_b", type=str, default="NVDA", help="Secondary Equity/Asset Ticker")
    parser.add_argument("--earnings", action="store_true", help="Flag if earnings release is imminent")
    parser.add_argument("--macro", type=str, default="ALIGNED", help="Macro alignment status: ALIGNED or NEUTRAL")
    args = parser.parse_args()

    terminal = MacroRelativeValueFilter(ticker_a=args.ticker_a, ticker_b=args.ticker_b)
    output = terminal.assess_pair(earnings_risk=args.earnings, structural_break=False, macro_alignment=args.macro)

    print("\n================ MACRO RV DISCRETIONARY TERMINAL ================")
    for k, v in output.items():
        print(f"{k:<22}: {v}")
    print("=================================================================\n")
