import requests
import re


class RequestAv:

    url = 'https://www.alphavantage.co/query?function=SECTOR&apikey=demo'

    @classmethod
    def sectors_performance(cls):
        return requests.get(cls.url).json()
