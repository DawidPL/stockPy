import requests


class CurrentRate:

    @staticmethod
    def current_rate_currency(currency: str) -> str:
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json')
        r = url.json()
        rate: float = r['rates'][0]['mid']
        currency_name: str = r['currency']
        currency_code: str = r['code']
        return f'Dzisiejszy kurs waluty {currency_name}({currency_code}): {rate}'

    @staticmethod
    def current_rate_gold() -> str:
        url = requests.get(f'http://api.nbp.pl/api/cenyzlota/?format=json')
        r = url.json()
        rate: float = r[0]['cena']
        return f'Dzisiejszy kurs złota: {rate} PLN/gram'


print(CurrentRate.current_rate_currency('eur'))
print(CurrentRate.current_rate_gold())