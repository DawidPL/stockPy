from HistoricalRate import historical_rate_currency


class Taxes:
    __slots__ = ['asset_amount', 'asset_bought_price', 'asset_sold_price', 'rate', 'asset_bought_fee',
                 'asset_sold_fee']

    def __init__(self, asset_amount: int, asset_bought_price: float, asset_sold_price: float,
                 rate: float, asset_bought_fee: float = 0.0, asset_sold_fee: float = 0.0) -> None:
        self.asset_amount = asset_amount
        self.asset_bought_price = asset_bought_price
        self.asset_sold_price = asset_sold_price
        self.rate = rate
        self.asset_bought_fee = asset_bought_fee
        self.asset_sold_fee = asset_sold_fee

    def expanse_income(self) -> float:
        self.rate = historical_rate_currency.get_historical_currency_rate()
        return (self.asset_amount * self.asset_bought_price) * self.rate + self.asset_bought_fee

    def income(self) -> float:
        pass

    def revenue(self) -> float:
        # dochód
        return self.income() - self.expanse_income()

    @staticmethod
    def client_info() -> str:
        pass


# if __name__ == "__main__":
#     tax = Taxes(8, 6.30, 7.70, 0.4, 0.4)
#     tax.revenue()
#     tax.expanse_income()
