import requests
from datetime import datetime
from typing import Any


class OptionChain:
    url = requests.get(f'https://query1.finance.yahoo.com/v7/finance/options/{company_name}')
    r = url.json()
    base_endpoint: Any = f"{r}['optionChain']['result'][0]"

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def option_chain_call(cls, name) -> None:
        option_expiration_dates = cls.base_endpoint + "['expirationDates']"
        option_lastprice = cls.base_endpoint + f"['options'][0][{name}][0]['lastPrice']"
        option_bid = cls.base_endpoint + f"['options'][0][{name}][0]['bid']"
        option_ask = cls.base_endpoint + f"['options'][0][{name}][0]['ask']"
        option_strike = cls.base_endpoint + f"['options'][0][{name}][0]['strike']"
        option_volume = cls.base_endpoint + f"['options'][0][{name}][0]['volume']"
        option_interest = cls.base_endpoint + f"['options'][0][{name}][0]['openInterest']"
        option_stock_fullname = cls.base_endpoint + "['quote']['longName']"
        option_instrument_type = cls.base_endpoint + "['quote']['quoteType']"
        option_exchange_name = cls.base_endpoint + "['quote']['fullExchangeName']"
        option_market_state = cls.base_endpoint + "['quote']['marketState']"
        option_average_daily_volume_10d = cls.base_endpoint + "['quote']['averageDailyVolume10Day']"
        option_average_daily_volume_3m = cls.base_endpoint + "['quote']['averageDailyVolume3Month']"
        option_regular_market_volume = cls.base_endpoint + "['quote']['regularMarketVolume']"
        option_regular_market_price = cls.base_endpoint + "['quote']['regularMarketPrice']"
        option_regular_market_time = cls.base_endpoint + "['quote']['regularMarketTime']"
        option_regular_market_change = cls.base_endpoint + "['quote']['regularMarketChange']"
        option_regular_market_change_percent = cls.base_endpoint + "['quote']['regularMarketChangePercent']"
        option_regular_market_day_range = cls.base_endpoint + "['quote']['regularMarketDayRange']"
        option_regular_market_open = cls.base_endpoint + "['quote']['regularMarketOpen']"
        option_regular_market_previous_close = cls.base_endpoint + "['quote']['regularMarketPreviousClose']"
        option_regular_market_day_hight = cls.base_endpoint + "['quote']['regularMarketDayHigh']"
        option_regular_market_day_low = cls.base_endpoint + "['quote']['regularMarketDayLow']"
        option_regular_market_bid = cls.base_endpoint + "['quote']['bid']"
        option_regular_market_bidsize = cls.base_endpoint + "['quote']['bidSize']"
        option_regular_market_ask = cls.base_endpoint + "['quote']['ask']"
        option_regular_market_asksize = cls.base_endpoint + "['quote']['askSize']"

    @classmethod
    def option_expiration_dates(cls, name) -> any:
        try:
            option_expiration_date = cls.base_endpoint + "['expirationDates']"
            for exp in option_expiration_date:
                expiration_dates = requests.get(f'{cls.url}/{name}?=date={exp}')
                exp_data = expiration_dates.json()
                unix_time = int(exp)
                return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d')
        except IndexError:
            return 'Ta spółka uniemożliwia handel opcjami'
