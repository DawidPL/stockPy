class StopLooseLevel:

    @staticmethod
    def stop_loss_level(market_entry_price: float, sl_level: float = 0.00) -> float:
        x = (market_entry_price / 100) * sl_level
        level = round(market_entry_price - x, 2)
        return level
