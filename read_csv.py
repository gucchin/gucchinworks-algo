import codecs

import pandas as pd


def read_csv(fn):
    with codecs.open(fn, "r", "Shift-JIS", "ignore") as f:
        df = pd.read_csv(f, names=["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"], index_col=0,
                         skiprows=2)
    return df.dropna()
