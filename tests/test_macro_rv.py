"""Automated Unit Tests for Macro RV Discretionary Terminal."""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch
from macro_rv_filter import MacroRelativeValueFilter


def test_initialization():
    """Validates that the filter initializes correctly with ticker pair."""
    filter_obj = MacroRelativeValueFilter("AAPL", "MSFT")
    assert filter_obj.ticker_a == "AAPL"
    assert filter_obj.ticker_b == "MSFT"


@patch('macro_rv_filter.yf.download')
def test_calculate_live_zscore(mock_download):
    """Validates Z-score calculation with mocked historical price data."""
    dates = pd.date_range(start='2025-01-01', periods=100, freq='B')
    
    # Create yfinance-style MultiIndex columns ('Close', 'AAPL') and ('Close', 'MSFT')
    columns = pd.MultiIndex.from_tuples([
        ('Close', 'AAPL'),
        ('Close', 'MSFT')
    ], names=['Price', 'Ticker'])
    
    mock_multi_df = pd.DataFrame(
        np.column_stack([
            np.linspace(100, 150, 100),
            np.linspace(200, 250, 100)
        ]),
        index=dates,
        columns=columns
    )
    mock_download.return_value = mock_multi_df

    filter_obj = MacroRelativeValueFilter("AAPL", "MSFT")
    zscore = filter_obj.calculate_live_zscore(lookback=30)
    
    assert isinstance(zscore, float)


@patch('macro_rv_filter.yf.download')
def test_assess_pair_rejection(mock_download):
    """Validates that earnings risk and structural breaks trigger proper rejections."""
    dates = pd.date_range(start='2025-01-01', periods=100, freq='B')
    
    columns = pd.MultiIndex.from_tuples([
        ('Close', 'AAPL'),
        ('Close', 'MSFT')
    ], names=['Price', 'Ticker'])
    
    mock_multi_df = pd.DataFrame(
        np.column_stack([
            np.linspace(100, 110, 100),
            np.linspace(200, 280, 100)
        ]),
        index=dates,
        columns=columns
    )
    mock_download.return_value = mock_multi_df

    filter_obj = MacroRelativeValueFilter("AAPL", "MSFT")
    
    # Test binary event risk rejection
    result_earnings = filter_obj.assess_pair(
        earnings_risk=True, 
        structural_break=False, 
        macro_alignment="ALIGNED"
    )
    assert result_earnings["Trade_Action"] == "REJECT (Imminent Binary Event Risk)"

    # Test structural regime shift rejection
    result_break = filter_obj.assess_pair(
        earnings_risk=False, 
        structural_break=True, 
        macro_alignment="ALIGNED"
    )
    assert result_break["Trade_Action"] == "REJECT (Structural Regime Shift Detected)"
