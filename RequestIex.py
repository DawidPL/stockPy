import requests
from typing import List


class RequestIex:

    url: str = 'https://cloud.iexapis.com/beta/stock/'
    key: str = '/quote?token=?'

    @classmethod
    def get_company_info(cls, value):
        return requests.get(f'{cls.url}+{value}+{cls.key}').json()


class Global:
    url = 'https://cloud.iexapis.com/beta/stock'
    
    def __init__(self, name: str, names: List[str]) -> None:
        self.name = name
        self.names = names
        
    def get_company_info(self) -> None:
        r = requests.get(f'{self.url}/{self.name}/company')
        print(r.status_code)
        data = r.json()
        print(data['industry'] + '\n' + data['companyName'])

    def current_quote(self) -> None:
        r = requests.get(f'{self.url}/{self.name}/book')
        print(r.status_code)
        data = r.json()
        print(data['quote']['latestPrice'])

    def batch_test(self) -> None:
        for name in names:
          r = requests.get(f'{self.url}/market/batch?symbols={name}&types=quote')
          print(r.status_code)
          data = r.json()
          print(*data, sep=',')

    def earnings(self) -> None:
        r = requests.get(f'{self.url}/{self.name}/earnings')
        print(r.status_code)
        data = r.json()
        print(data)

    def news(self) -> None:
        r = requests.get(f'{self.url}/{self.name}/news/last/5')
        print(r.status_code)
        data = r.json()
        print(data)


global_company_info = Global(company_name_input, company_names)

