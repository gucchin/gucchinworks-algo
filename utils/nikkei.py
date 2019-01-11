import requests
from bs4 import BeautifulSoup

baseURL = "https://www.nikkei.com/nkd/company/"


def __get_stock_price_at_close(bs):
    close = bs.find("dd", class_="m-stockPriceElm_value now").text.split()[0]
    close = "".join(close.split(","))

    return float(close)


def __get_stock_price_at_open(bs):
    stock = bs.find_all("span", class_="m-stockInfo_detail_value")
    open = "".join(stock[0].text.split()[0].split(","))

    return float(open)


def __get_stock_high_price(bs):
    stock = bs.find_all("span", class_="m-stockInfo_detail_value")
    high = "".join(stock[1].text.split()[0].split(","))
    return float(high)


def __get_stock_low_price(bs):
    stock = bs.find_all("span", class_="m-stockInfo_detail_value")
    low = "".join(stock[2].text.split()[0].split(","))
    return float(low)


def __get_stock_volume(bs):
    stock = bs.find_all("span", class_="m-stockInfo_detail_value")
    volume = "".join(stock[3].text.split()[0].split(","))
    return float(volume)


def __get_date(bs):
    date = bs.find("div", class_="m-stockInfo_date").text
    return date


def get_stock_price_from_nikkei(stock_code):
    html = requests.get(baseURL + "?scode=%d" % stock_code)
    bs = BeautifulSoup(html.text, "lxml")

    close = __get_stock_price_at_close(bs)
    open = __get_stock_price_at_open(bs)
    high = __get_stock_high_price(bs)
    low = __get_stock_low_price(bs)
    volume = __get_stock_volume(bs)
    date = __get_date(bs)

    return close, open, high, low, volume, date
