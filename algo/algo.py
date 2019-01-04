
import pandas as pd

def ma(inClose, inPeriod):
    return inClose.rolling(inPeriod).mean()

def bband(inClose, inPeriod, n):
    std = inClose.rolling(inPeriod).std()

    mid = ma(inClose, inPeriod)
    high = mid + n*std
    low = mid - n*std
    return high, mid\
        , low

