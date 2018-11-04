import requests
import main

userinput = input('Podaj nazwe spolki:')
frame = input('Podaj przedział czasowy:')
def user_search(symbol, rang):
    URL = "https://api.iextrading.com/1.0/stock/%s/chart/%s" % (symbol, rang)
    response = requests.get(URL)
    r = response.json()
    if response.status_code == requests.codes.ok:
        print(response.status_code)
        print(r)
    else:
        print('Wystąpił problem z połączenem')
user_search(userinput, frame)
