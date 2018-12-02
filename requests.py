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

class OptionChain():
  url = 'https://query1.finance.yahoo.com/v7/finance/options'
  name = company_name_input
  r = requests.get('{}/{}'.format(url, name))
  print(r.status_code)
  data = r.json()
 
  def optionChainAll(self, name):
    self.name = company_name_input
 
  def optionChainCall(self, name):
      self.name = option_type
      option_expirationDates = OptionChain.data['optionChain']['result'][0]['expirationDates']
      option_lastprice = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['lastPrice']
      option_bid = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['bid']
      option_ask = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['ask']
      option_strike = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['strike']
      option_volume = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['volume']
      option_interest = OptionChain.data['optionChain']['result'][0]['options'][0][self.name][0]['openInterest']
      option_stock_fullname = OptionChain.data['optionChain']['result'][0]['quote']['longName']
      option_instrument_type = OptionChain.data['optionChain']['result'][0]['quote']['quoteType']
      option_exchange_name = OptionChain.data['optionChain']['result'][0]['quote']['fullExchangeName']
      option_market_state = OptionChain.data['optionChain']['result'][0]['quote']['marketState']
      option_average_daily_volume_10d = OptionChain.data['optionChain']['result'][0]['quote']['averageDailyVolume10Day']
      option_average_daily_volume_3m = OptionChain.data['optionChain']['result'][0]['quote']['averageDailyVolume3Month']
      option_regular_market_volume = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketVolume']
      option_regular_market_price = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketPrice']
      option_regular_market_time = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketTime']
      option_regular_market_change = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketChange']
      option_regular_market_change_percent = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketChangePercent']
      option_regular_market_day_range = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayRange']
      option_regular_market_open = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketOpen']
      option_regular_market_previous_close = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketPreviousClose']
      option_regular_market_day_hight = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayHigh']
      option_regular_market_day_low = OptionChain.data['optionChain']['result'][0]['quote']['regularMarketDayLow']
      option_regular_market_bid = OptionChain.data['optionChain']['result'][0]['quote']['bid']
      option_regular_market_bidsize = OptionChain.data['optionChain']['result'][0]['quote']['bidSize']
      option_regular_market_ask = OptionChain.data['optionChain']['result'][0]['quote']['ask']
      option_regular_market_asksize = OptionChain.data['optionChain']['result'][0]['quote']['askSize']
 
      unix_time = int(option_regular_market_time)
      print(datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))
      print(option_strike, option_instrument_type)
 
  def optionExpirationDates(self, name):
    try:
      option_expirationDates = OptionChain.data['optionChain']['result'][0]['expirationDates']
      for exp in option_expirationDates:
        expirationDates = requests.get('{}/{}?=date={}'.format(self.url, self.name, exp))
        exp_data = expirationDates.json()
        unix_time = int(exp)
        print(datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d'), sep ='\n')
    except IndexError:
        print('Ta spółka nie umożliwia handlu opcjami')
 
 
option_chain = OptionChain()
option_chain.optionExpirationDates(company_name_input)
option_chain.optionChainCall(option_type)


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


