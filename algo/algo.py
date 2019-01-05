import numpy as np
import pandas as pd


def ma(inClose, inPeriod):
    return inClose.rolling(inPeriod).mean()

def bband(inClose, inPeriod, n):
    std = inClose.rolling(inPeriod).std()

    mid = ma(inClose, inPeriod)
    high = mid + n*std
    low = mid - n*std

    return pd.DataFrame({'Bband_high': high, 'Bband_low': low, 'Bband_mid': mid})


def hv(inClose, inPeriod=20, convert=252):
    x = inClose.shift(1)

    s = np.log(inClose / x)
    print(s.tail())
    return s.rolling(inPeriod).std(ddof=1) * 100 * np.sqrt(convert)
