import requests
from typing import List
from security.encrypting import get_token

endpoints_list: List[str] = ['http://api.nbp.pl/api/cenyzlota/?format=json',
                             'http://api.nbp.pl/api/exchangerates/rates/a/EUR/?format=json',
                             'https://query1.finance.yahoo.com/v7/finance/options/FORD',
                             'http://api.nbp.pl/api/exchangerates/tables/b/?format=json',
                             'https://www.alphavantage.co/query?function=SECTOR&apikey=demo',
                             'http://api.nbp.pl/api/exchangerates/rates/a/EUR/2015-06-23/?format=json',
                             f'https://cloud.iexapis.com/beta/stock/AMD/quote?token={get_token()}']


def api_response_status_helper() -> List[str]:
    endpoints_status: List[str] = []
    for i in endpoints_list:
        status = requests.get(i)
        endpoints_status.append(status.status_code)
    return endpoints_status


def api_data_type_return_helper() -> List[str]:
    endpoints_type: List[str] = []
    for i in endpoints_list:
        status = requests.get(i)
        r = status.json()
        endpoints_type.append(r)
    return endpoints_type
