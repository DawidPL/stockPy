class Global():
    """ global indicators properties """
    def __init__(self, current_value, sell_alert_value, buy_alert_value):
        self.current_value = current_value
        self.sell_alert_value = sell_alert_value
        self.buy_alert_value = buy_alert_value

    def indicator_alert(self):
        sell_alert = "Sygnał sprzedaży"
        buy_alert = "Sygnał kupna"
        neutral_alert = "Brak sygnału"
        if self.current_value >= self.sell_alert_value:
            return sell_alert
        elif self.sell_alert_value > self.current_value < self.buy_alert_value:
            return "nie ma nic" + neutral_alert
        elif self.current_value <= self.buy_alert_value:
            return buy_alert
        else:
            return "test"

    # def get_value(self):

# main rsi properties


rsi = Global(72, 70, 30)
print(rsi.indicator_alert())
