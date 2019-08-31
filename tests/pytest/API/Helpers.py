import requests
from typing import List

endpoints_list: List[str] = ['http://api.nbp.pl/api/cenyzlota/?format=json',
                             'http://api.nbp.pl/api/exchangerates/rates/a/EUR/?format=json']


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
