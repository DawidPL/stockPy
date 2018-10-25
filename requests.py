import requests
import main

URL = 'https://api.iextrading.com/1.0/stock/'
PARAMS = {'symbol': ticket, 'constans':'/chart/', 'range': chart_range_eng}
r = requests.get(url = URL, params=PARAMS)

data = r.json()
print(i)
