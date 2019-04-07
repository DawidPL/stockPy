from HistoricalRate import historical_rate_currency


class Taxes:

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
        return 100

    def revenue(self) -> float:
        # dochód
        return self.income() - self.expanse_income()

    @staticmethod
    def client_info() -> str:
        return 'Test'


tax = Taxes(8, 6.30, 7.70, 0.4, 0.4)

print(tax.revenue())
print(tax.expanse_income())
