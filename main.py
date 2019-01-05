# -*- coding: utf-8 -*-
import algo.algo
import matplotlib.finance
import matplotlib.pyplot as plt
from read_csv import read_csv


class Stock:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.df = None

    def save(self):
        pass


def candlestick(ax, price, periods=30):
    matplotlib.finance.candlestick2_ohlc(ax, price['Open'][-periods:], price['High'][-periods:],
                                         price['Low'][-periods:], price['Close'][-periods:], width=0.5, colorup="b")


def bband_plot(ax, df, periods):
    ax.plot(df.index[-periods:], df['Bband_mid'][-periods:], label="bband_mid")
    ax.plot(df.index[-periods:], df['Bband_high'][-periods:], label="bband_high")
    ax.plot(df.index[-periods:], df['Bband_low'][-periods:], label="bband_mid")


def show_hv(ax, price, periods=30):
    hv = algo.algo.hv(price['Close'])
    ax.plot(hv.index[-periods:], hv[-periods:])
    ax.hlines(20, hv.index[-periods], hv.index[-1])


def main():
    period = 90

    price = read_csv("./data/7267_2018.csv")
    bband = algo.algo.bband(price['Close'], 9, 2)

    _, *ax = plt.subplots(nrows=2, figsize=(15, 8), sharex=True)

    candlestick(ax[0][0], price, periods=period)
    bband_plot(ax[0][0], bband, periods=period)

    show_hv(ax[0][1], price, periods=period)

    plt.show()

if __name__ == '__main__':
    main()