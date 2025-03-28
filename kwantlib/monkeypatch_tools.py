import pandas as pd
from .cma_tools import cross_moving_average, zscore, clip_via_zscore
from .pnl_tools import shift_ignoring_nan, shift_with_sample
from .metrics_tools import plotx

def monkeypatch():
    pd.Series.shift_ignoring_nan = shift_ignoring_nan
    pd.DataFrame.shift_ignoring_nan = shift_ignoring_nan

    pd.Series.shift_with_sample = shift_with_sample
    pd.DataFrame.shift_with_sample = shift_with_sample

    pd.Series.cross_moving_average = cross_moving_average
    pd.DataFrame.cross_moving_average = cross_moving_average

    pd.Series.zscore = zscore
    pd.DataFrame.zscore = zscore

    pd.Series.clip_via_zscore = clip_via_zscore
    pd.DataFrame.clip_via_zscore = clip_via_zscore

    pd.Series.plotx = plotx
    pd.DataFrame.plotx = plotx


