import requests

company_name_input = input("Company name")
company_names = input("Company names").split(',')
print (company_names)

# main API GET class 

class Global():
  url = 'https://api.iextrading.com/1.0/stock'
  def getCompanyInfo(self, name):
    self.name = company_name_input 
    r = requests.get('%s/%s/company' % (self.url, self.name))
    print(r.status_code)
    data = r.json()
    print(data['industry'] +'\n' + data['companyName'])

  def currentQuote(self, name):
    self.name = company_name_input 
    r = requests.get('%s/%s/book' % (self.url, self.name))
    print(r.status_code)
    data = r.json()
    print(data['quote']['latestPrice'])

  def batchTest(self, names):
    self.names = company_names
    for name in names:
      r = requests.get('%s/market/batch?symbols=%s&types=quote' % (self.url, self.names))
      print(r.status_code)
      data = r.json()
      print(*data, sep =',')

  def earnings(self,names):
    self.name = company_name_input 
    r = requests.get('%s/%s/earnings' % (self.url, self.name))
    print(r.status_code)
    data = r.json()
    print(data)

  def news(self, names):
    self.name = company_name_input 
    r = requests.get('%s/%s/news/last/5' % (self.url, self.name))
    print(r.status_code)
    data = r.json()
    print(data)

global_company_info = Global()
global_company_info.getCompanyInfo(company_name_input)
global_company_info.currentQuote(company_name_input)
global_company_info.batchTest(company_names)
global_company_info.earnings(company_names)
global_company_info.news(company_names)

# main API Option chain GET class 

from datetime import datetime

company_name_input = input("Company name")

# main Options API GET class 

class GlobalOptionChain():
  url = 'https://query1.finance.yahoo.com/v7/finance/options'
  name = company_name_input
  r = requests.get('%s/%s' % (url, name))
  print(r.status_code)
  data = r.json()

  def optionChainAll(self, name):
    self.name = company_name_input
  
  def optionChainCall(self, name):
      option_lastprice = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['lastPrice']
      option_bid = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['bid']
      option_ask = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['ask'] 
      option_stock_fullname = GlobalOptionChain.data['optionChain']['result'][0]['quote']['longName']
      option_expirationDates = GlobalOptionChain.data['optionChain']['result'][0]['expirationDates']
      option_strike = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['strike']
      option_volume = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['volume']
      option_interest = GlobalOptionChain.data['optionChain']['result'][0]['options'][0]['calls'][0]['openInterest']

  def optionExpirationDates(self, name):
    try:
      option_expirationDates = GlobalOptionChain.data['optionChain']['result'][0]['expirationDates']
      for exp in option_expirationDates:
        expirationDates = requests.get('%s/%s?=date=%s' % (self.url, self.name, exp))
        exp_data = expirationDates.json()
        formatted_exp = int(exp)
        print(datetime.utcfromtimestamp(formatted_exp).strftime('%Y-%m-%d'), sep ='\n')
    except IndexError:
        print('Ta spółka nie umożliwia handlu opcjami')


option_chain = GlobalOptionChain()
option_chain.optionExpirationDates(company_name_input)


#https://www.strategic-options.com/insight/how-to-get-option-prices-for-free-api-yahoo/
#https://www.npmjs.com/package/finance

'''


import requests
import main

userinput = input('Podaj nazwe spolki:')
frame = input('Podaj przedział czasowy:')
def user_search(symbol, rang):
    URL = f"https://api.iextrading.com/1.0/stock/{symbol}/chart/{rang}"
#    URL = "https://api.iextrading.com/1.0/stock/" + symbol + "/chart/" + rang
#    URL = "https://api.iextrading.com/1.0/stock/%s/chart/%s" % (symbol, rang)
    response = requests.get(URL)
    r = response.json()
    if response.status_code == requests.codes.ok:
        print(response.status_code)
        print(r)
    else:
        print('Wystąpił problem z połączenem')
user_search(userinput, frame)'''


