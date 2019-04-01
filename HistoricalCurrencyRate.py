import requests
import json


class HistoricalCurrencyRates:
    def __init__(self, date: float, currency_code: str, currency_date: str) -> None:
        self.date = date
        self.currency_code = currency_code
        self.currency_date = currency_date

    def get_historical_currency_rate(self) -> float:
        # date format is : 2000-12-01
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{self.currency_code}/{self.currency_date}/?format=json')
        r = url.json()
        rate: float = r['rates'][0]['mid']
        return round(rate, 2)


historical_currency_rate = HistoricalCurrencyRates(3.33, 'usd', '2019-01-21')

try:
    print(historical_currency_rate.get_historical_currency_rate())
except json.decoder.JSONDecodeError:
    print('Brak danych - w ten dzień giełda była zamknięta')


