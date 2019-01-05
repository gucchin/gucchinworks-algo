# -*- coding : utf-8
"""
copyright 2019 gucchin all right reserved.
"""

import numpy as np
import pandas as pd


def sma(inClose, inPeriod=9):
    """sma is simple moving average"""
    return inClose.rolling(inPeriod, min_periods=1).mean()


def ema(inClose, inPeriod=9):
    """ema is exponential moving average"""
    s = sma(inClose, inPeriod)

    e = np.zeros_like(s)
    e[:inPeriod] = s[:inPeriod]

    for i in range(inPeriod, len(s)):
        e[i] = e[i - 1] + (inClose[i] - e[i - 1]) * 2.0 / (inPeriod + 1)

    return pd.Series(data=e, index=inClose.index)


def macd(inClose, shortPeriod=12, longPeriod=26, signalPeriod=9):
    """macd is moving average convergence divergence"""
    mac = ema(inClose, shortPeriod) - ema(inClose, longPeriod)
    sig = ema(mac, signalPeriod)
    return mac, sig


def bband(inClose, inPeriod, n):
    """bband is bollinger bands"""
    std = inClose.rolling(inPeriod).std()

    mid = sma(inClose, inPeriod)
    high = mid + n*std
    low = mid - n*std

    return pd.DataFrame({'Bband_high': high, 'Bband_low': low, 'Bband_mid': mid})


def hv(inClose, inPeriod=20, convert=252):
    """hv is historical volatility"""
    x = inClose.shift(1)
    s = np.log(inClose / x)
    return s.rolling(inPeriod).std(ddof=1) * 100 * np.sqrt(convert)
