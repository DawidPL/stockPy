import requests
from request import get_historical_currency_rate
 
class HistoricalCurrencyRate:
    def __init__(self, date: float, currency_code: str, currency_date: str) -> None:
        self.date = date
        self.currency_code = currency_code
        self.currency_date = currency_date
 
    def get_historical_currency_rate(self ) -> float:
        # date format is : 2000-12-01
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{self.currency_code}/{self.currency_date}/?format=json')
        r = url.json()
        rate: float = r['rates'][0]['mid']
        return rate
 
    def get_data(self) ->float:
        return get_historical_currency_rate('usd', '2012-05-18')
 
historical_currency_rate = HistoricalCurrencyRate
 
class Taxes:
 
    def __init__(self, asset_amount: int, asset_bought_price: float, asset_sold_price: float, asset_bought_fee: float = 0.0, asset_sold_fee: float = 0.0) -> None:
        self.asset_amount = asset_amount
        self.asset_bought_price = asset_bought_price
        self.asset_sold_price = asset_sold_price
        self.asset_bought_fee = asset_bought_fee
        self.asset_sold_fee = asset_sold_fee
 
    def expanse_income(self, rate) -> float:
        return (self.asset_amount * self.asset_bought_price) * rate + self.asset_bought_fee
 
tax = Taxes
