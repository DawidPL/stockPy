import requests
 
def get_historical_currency_rate(currency_code: str, currency_date: str) -> float:
    # date format is : 2000-12-01
 
    url = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{currency_date}/?format=json')
    r = url.json()
    rate = r['rates'][0]['mid']
    return rate
 
print(get_historical_currency_rate('usd', '2012-05-18'))
