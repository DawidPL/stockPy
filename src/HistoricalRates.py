import requests


class HistoricalRates:
    __slots__ = ['date', 'currency_code', 'currency_date']

    def __init__(self, date: float, currency_code: str, currency_date: str) -> None:
        self.date = date
        self.currency_code = currency_code
        self.currency_date = currency_date

    def get_historical_currency_rate(self) -> float:
        """
        Return single currency rate from polish central bank
        date format is : yyyy-mm-dd
        :return: float
        """
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{self.currency_code}/{self.currency_date}/?format=json')
        r = url.json()
        rate: float = r['rates'][0]['mid']
        return round(rate, 2)

    @staticmethod
    def get_historical_currencies_table(date: str) -> None:
        """
        Display rates table with all available currencies from polish central bank.
        :param date: str
        :return: None
        """
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/b/{date}/?format=json')
        r = url.json()
        for i in range(0, 100):
            default_path = r[0]['rates'][i]
            name: str = default_path['currency']
            code: str = default_path['code']
            mid: float = default_path['mid']
            print(f'{name} | {code} | {mid}')

    @staticmethod
    def get_historical_gold_rate(date: str) -> float:
        """
        Return gold rate base on given date.
        :param date: str
        :return: float
        """
        url = requests.get(f'http://api.nbp.pl/api/cenyzlota/{date}/?format=json')
        r = url.json()
        rate: float = r[0]['cena']
        return rate


#historical_rates = HistoricalRates(3.33, 'usd', '2019-01-15')

# try:
#     print(historical_rate_currency.get_historical_currency_rate())
# except json.decoder.JSONDecodeError:
#     print('Brak danych - w ten dzień giełda była zamknięta')
# try:
#     print(HistoricalRates.get_historical_gold_rate('2014-05-12'))
# except json.decoder.JSONDecodeError:
#     print ('Brak danych - tego dnia handel na złocie się nie odbywał')
# try:
#     print(HistoricalRates.get_historical_currencies_table('2014-05-14'))
# except json.decoder.JSONDecodeError:
#     print ('Brak danych - tego dnia giełda była nieczynna')

