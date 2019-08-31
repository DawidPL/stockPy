import pytest
import mock
from typing import List, Tuple
from src.HistoricalRates import HistoricalRates


def currency_loop_helper() -> List[Tuple[int, float]]:
    historical_rates_mock = mock.Mock(HistoricalRates)
    dates_rate: List[str] = ['2018-05-25', '2017-02-20', '2013-12-11']
    currencies_codes: List[str] = ['JPY', 'AUD', 'GBP']
    expected_rates: List[float] = [0.03, 3.12, 4.98]
    actual_rates: List[int] = []
    for i in range(len(dates_rate)):
        historical_rates_mock.get_historical_currency_rate.return_value = expected_rates[i]
        result = historical_rates_mock.get_historical_currency_rate(currencies_codes[i], dates_rate[i])
        actual_rates.append(result)
    actual_list = [(a, b) for a, b in zip(actual_rates, expected_rates)]
    return actual_list


@pytest.fixture
def gold_loop_helper(func, date, rates):
    for i in range(len(rates)):
        result = func(date[i])
        assert result == rates[i]
    pass




