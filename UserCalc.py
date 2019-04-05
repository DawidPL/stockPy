from typing import List


class UserCalc:

    @staticmethod
    def folding_percentage(start_value: float, return_rate: float, time_period: int, ) -> List[float]:
        folding_percentage_list: List[float] = []
        n: int = 0
        while n != time_period:
            while n == 0:
                x: float = round(start_value + (start_value * (return_rate/100)), 2)
                folding_percentage_list.append(x)
                n += 1
            x: float = round(folding_percentage_list[n-1] + (folding_percentage_list[n-1] * (return_rate/100)), 2)
            folding_percentage_list.append(x)
            n += 1
        return folding_percentage_list

    @staticmethod
    def risk_reward_ratio(exchange_price: float, shares_amount: int, expected_profit: float, stoploss_level: float = 0, fee: float = 0) -> float:
        enter_value = exchange_price * shares_amount
        wanted_exchange_price: float = 0
        while wanted_exchange_price * shares_amount <= enter_value + expected_profit:
            wanted_exchange_price += 0.01
        return round(wanted_exchange_price, 2)


print(UserCalc.folding_percentage(1000, 10.0, 12))
print(UserCalc.risk_reward_ratio(1.00, 1000, 100, 0.90, 0.20))
