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



'''


import requests
import main

userinput = input('Podaj nazwe spolki:')
frame = input('Podaj przedział czasowy:')
def user_search(symbol, rang):
    URL = f"https://api.iextrading.com/1.0/stock/{symbol}/chart/{rang}"
    response = requests.get(URL)
    r = response.json()
    if response.status_code == requests.codes.ok:
        print(response.status_code)
        print(r)
    else:
        print('Wystąpił problem z połączenem')
user_search(userinput, frame)'''


