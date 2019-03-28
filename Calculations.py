from typing import List
# Only for testing


class Calculations:
    input_value: int = int(input())
    return_percent: int = int(input())
    investment_time: int = int(input())
    shares_amount: int = int(input('Liczba akcji'))
    bought_price: float = float(input('Cena kupna'))
    reward_percent: float = float(input('Ile procent chcesz zarobić'))
    risk_percent: float = float(input('Ile procent możesz stracić'))
    fee: float = float(input('Prowizja transakcji'))

    def __init__(self, input_value: int, return_percent: int, investment_time: int, shares_amount: int, bought_price: float,
                 reward_percent: float, risk_percent: float, fee: float) -> None:
        self.input_value = input_value
        self.return_percent = return_percent
        self.investment_time = investment_time
        self.shares_amount = shares_amount
        self.bought_price = bought_price
        self.reward_percent = reward_percent
        self.risk_percent = risk_percent
        self.fee = fee

    def folding_percentage(self) -> None:
        n: int = 0
        return_list: List[float] = []
        while n != self.investment_time:
            value: float = self.input_value + ((self.return_percent / 100) * self.input_value)
            return_list.append(value)
            self.input_value = return_list[n]
            n += 1
        for number in return_list:
            print(round(number, 2))

    def position_counter(self) -> str:
        # Calculate cash amount to enter position in specified risk to reward ratio
        reward: float = self.bought_price + (self.fee / self.shares_amount) + ((self.bought_price / 100) * self.reward_percent)
        lost: float = self.bought_price - (self.fee / self.shares_amount) - ((self.bought_price / 100) * self.risk_percent)
        return(
            f'Kupujesz {self.shares_amount} akcji po cenie {self.bought_price}. Aby zarobić {self.reward_percent}'
            f'% lub ewentualnie stracić {self.risk_percent}% podstaw TP na poziomie {reward} a SL {lost}'
            )
