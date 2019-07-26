class Indicators:
    __slots__ = ['current_value', 'sell_alert_value', 'buy_alert_value']

    def __init__(self, current_value: float, sell_alert_value: float, buy_alert_value: float) -> None:
        self.current_value = current_value
        self.sell_alert_value = sell_alert_value
        self.buy_alert_value = buy_alert_value

    def indicator_current_status(self) -> int:
        """
        Current value of the indicator
        :return: int
        """
        if self.current_value > 70:
            return 1
        elif self.current_value < 30:

            return -1
        elif 70 > self.current_value > 30:
            return 0

    def indicator_alert(self) -> str:
        """
        Returns buy, sell or neutral indicator alert
        :return: str
        """
        sell_alert: str = "Sygnał sprzedaży"
        buy_alert: str = "Sygnał kupna"
        neutral_alert: str = "Brak sygnału"
        if self.current_value >= self.sell_alert_value:
            return sell_alert
        elif self.sell_alert_value > self.current_value < self.buy_alert_value:
            return neutral_alert
        elif self.current_value <= self.buy_alert_value:
            return buy_alert
        else:
            return "test"


if __name__ == "__main__":
    rsi = Indicators(72, 77, 30)
    rsi.indicator_alert()
