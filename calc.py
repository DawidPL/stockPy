# calculations
import math

''' Only for tests '''

input_value = int(input())
return_percent  = int(input())
investment_time = int(input())

shares_amount = int(input('Liczba akcji'))
bought_price = float(input('Cena kupna'))
reward_percent = float(input('Ile procent chcesz zarobić'))
risk_percent = float(input('Ile procent możesz stracić'))
commition = float(input('Prowizja transakcji'))

class Calculations():

    def __init__(self, input_value, return_percent, investment_time, shares_amount, bought_price, 
                 reward_percent, risk_percent, commition):
      self.input_value = input_value
      self.return_percent = return_percent
      self.investment_time = investment_time
      self.shares_amount = shares_amount
      self.bought_price = bought_price
      self.reward_percent = reward_percent
      self.risk_percent = risk_percent
      self.commition = commition
        
    # Folding Precentage
    def foldingPercentage(self):
      n = 0
      return_list = []
      while n != investment_time:
        value = input_value + ((return_percent / 100 ) * input_value)
        return_list.append(value)
        input_value = return_list[n]
        n += 1
      for number in return_list:
        print(round(number, 2))
        
    # Calculate cash amount to enter position in specified risk to reward ratio
    def positionCounter(self):
      reward = bought_price + (commition / shares_amount) + ((bought_price / 100) * reward_percent)
      lost = bought_price - (commition / shares_amount) - ((bought_price / 100) * risk_percent)
      print ('Kupujesz {} akcji po cenie {}. Aby zarobić {}% lub ewentualnie stracić {}% podstaw TP na poziomie {} a SL {}'
             . format(shares_amount, bought_price, reward_percent, risk_percent, reward, lost))
 
 
calc = Calculations()
print(calc.positionCounter(input_value, return_percent, investment_time, investment_timeb, investment_timec, investment_timedb))
print(calc.positionCounter(shares_amount, bought_price, reward_percent, risk_percent, commition))
