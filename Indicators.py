class Indicators:
    """ global indicators properties """
    def __init__(self, current_value: float, sell_alert_value: float, buy_alert_value: float) -> None:
        self.current_value = current_value
        self.sell_alert_value = sell_alert_value
        self.buy_alert_value = buy_alert_value

    def indicator_alert(self) -> str:
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

    # def get_value(self):

# main rsi properties


rsi = Indicators(72, 77, 30)
print(rsi.indicator_alert())
