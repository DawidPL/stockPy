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
    def risk_reward_ratio(exchange_entry_price: float, shares_amount: int, expected_profit: float) -> float:
        enter_value = exchange_entry_price * shares_amount
        wanted_exchange_price: float = 0
        while wanted_exchange_price * shares_amount <= enter_value + expected_profit:
            wanted_exchange_price += 0.01
        return round(wanted_exchange_price, 2)

    @staticmethod
    def sl_price_level(exchange_entry_price: float, sl_level: float = 0,) -> float:
        x = (exchange_entry_price / 100) * sl_level
        y = round(exchange_entry_price - x, 2)
        return y


print(UserCalc.folding_percentage(1000, 10.0, 12))
print(UserCalc.risk_reward_ratio(1.24, 1000, 160))
print(UserCalc.sl_price_level(10, 3.25))
