class RiskRewardRatio:

    @staticmethod
    def risk_reward_ratio(market_entry_price: float, shares_amount: int, expected_profit: float) -> float:
        entry_value: float = market_entry_price * float(shares_amount)
        wanted_exchange_price: float = 0
        while wanted_exchange_price * shares_amount <= entry_value + expected_profit:
            wanted_exchange_price += 0.01
        return round(wanted_exchange_price, 2)
