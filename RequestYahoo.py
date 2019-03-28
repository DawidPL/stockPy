import requests
from datetime import datetime

company_name_input: int = input("Company name")


class OptionChain:
    url: str = 'https://query1.finance.yahoo.com/v7/finance/options'
    r = requests.get(f'{url}/{company_name_input}')
    print(r.status_code)
    data = r.json()

    def __init__(self, name: str) -> None:
        self.name = name

    def option_chain_call(self) -> str:
        self.name = option_type
        self.base_endpoint = f"{OptionChain.data}['optionChain']['result'][0]"
        option_expiration_dates = OptionChain.data['optionChain']['result'][0]['expirationDates']
        option_lastprice = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['lastPrice']
        option_bid = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['bid']
        option_ask = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['ask']
        option_strike = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['strike']
        option_volume = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['volume']
        option_interest = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['openInterest']
        option_stock_fullname = OptionChain.data['optionChain']['result'][0]['quote']['longName']
        option_instrument_type = OptionChain.data['optionChain']['result'][0]['quote']['quoteType']
        option_exchange_name = OptionChain.data['optionChain']['result'][0]['quote']['fullExchangeName']
        option_market_state = OptionChain.data['optionChain']['result'][0]['quote']['marketState']
        option_average_daily_volume_10d = OptionChain.data['optionChain']['result'][0]['quote'][
            'averageDailyVolume10Day']
        option_average_daily_volume_3m = OptionChain.data['optionChain']['result'][0]['quote'][
            'averageDailyVolume3Month']
        option_regular_market_volume = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketVolume']
        option_regular_market_price = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketPrice']
        option_regular_market_time = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketTime']
        option_regular_market_change = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketChange']
        option_regular_market_change_percent = OptionChain.data['optionChain']['result'][0]['quote'][
            'regularMarketChangePercent']
        option_regular_market_day_range = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayRange']
        option_regular_market_open = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketOpen']
        option_regular_market_previous_close = OptionChain.data['optionChain']['result'][0]['quote'][
            'regularMarketPreviousClose']
        option_regular_market_day_hight = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayHigh']
        option_regular_market_day_low = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayLow']
        option_regular_market_bid = OptionChain.data['optionChain']['result'][0]['quote']['bid']
        option_regular_market_bidsize = OptionChain.data['optionChain']['result'][0]['quote']['bidSize']
        option_regular_market_ask = OptionChain.data['optionChain']['result'][0]['quote']['ask']
        option_regular_market_asksize = OptionChain.data['optionChain']['result'][0]['quote']['askSize']

        unix_time = int(option_regular_market_time)
        print(datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))
        print(option_strike, option_instrument_type)

    def option_expiration_dates(self) -> str:
        try:
            option_expiration_dates = OptionChain.data['optionChain']['result'][0]['expirationDates']
            for exp in option_expiration_dates:
                expiration_dates = requests.get(f'{self.url}/{self.name}?=date={exp}')
                exp_data = expiration_dates.json()
                unix_time = int(exp)
                print(datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d'), sep='\n')
        except IndexError:
            print('Ta spółka nie umożliwia handlu opcjami')


option_chain = OptionChain(company_name_input)

