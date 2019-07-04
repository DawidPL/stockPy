import requests
from typing import List


class RequestAv:

    url: str = 'https://www.alphavantage.co/query?function=SECTOR&apikey=demo'

    @classmethod
    def sectors_performance(cls):
        """
        All available sectors performance with different time range
        :return:
        """
        data = requests.get(cls.url).json()
        range_data: List[str] = ['info', 'aktualnie', '1 dzień', '5 dni', '1 miesiąc', '3 miesiące',
                                 '1 rok (do dnia dzisiejszego)', '1 rok', '3 lata', '5 lat', '10 lat']
        n: int = 0
        for i in data.values():
            print('---------')
            print(range_data[n])
            n += 1
            print('---------')
            for y, k in i.items():
                print(f'{y} | {k}')
