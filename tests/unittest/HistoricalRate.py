import requests


def get_historical_currency_rate(currency_code: str, currency_date: str) -> float:
    url = requests.get(
        f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{currency_date}/?format=json')
    r = url.json()
    rate: float = r['rates'][0]['mid']
    return round(rate, 2)


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





