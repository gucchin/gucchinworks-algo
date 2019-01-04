# -*- coding: utf-8 -*-
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web

import algo.algo

class Stock:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.df = None

    def save(self):
        pass

def main():
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2019,1, 4)
    nikkei225 = web.DataReader("NIKKEI225", "fred", start, end)

    h, m, l = algo.algo.bband(nikkei225, 5, 2.0)

    price = nikkei225.copy()
    price["mid"] = m
    price["high"] = h
    price["low"] = l
    price.plot()
    plt.show()

if __name__ == '__main__':
    main()