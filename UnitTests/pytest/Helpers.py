import pytest

from HistoricalRate import get_historical_currency_rate


@pytest.fixture
def gold_loop_helper(func, date, rates):
    for i in range(len(rates)):
        result = func(date[i])
        assert result == rates[i]

