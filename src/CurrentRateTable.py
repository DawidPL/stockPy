import requests


class CurrentRateTable:

    @staticmethod
    def currencies_table() -> any:
        url = requests.get(f'http://api.nbp.pl/api/exchangerates/tables/b/?format=json')
        r = url.json()
        for i in range(0, 100):
            default_path = r[0]['rates'][i]
            name: str = default_path['currency']
            code: str = default_path['code']
            mid: float = default_path['mid']
            print(f'{name} | {code} | {mid}')

