from .nikkei import get_stock_price_from_nikkei


class test_get_stock_price_from_nikkei():
    close, open, high, low, volume, date = get_stock_price_from_nikkei(7201)
    assert close == 905.5
    assert open == 902.0
    assert high == 906.9
    assert low == 900.5
    assert volume == 9491800
    assert date == "2019/1/11"
