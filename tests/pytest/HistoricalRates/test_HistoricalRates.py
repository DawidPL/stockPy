import pytest
from typing import Any
from Helpers import currency_loop_helper


@pytest.mark.parametrize('expected, actual', currency_loop_helper())
def test_currency_rate_equal(expected, actual) -> Any:

    """

    Test if currency code is correct with given date and rate

    """
    assert expected == actual


# def test_currency_rate():
#
#     """
#
#     Test if currency rate is correct with given date
#
#     """
#     currency_name = ['USD'] * 4
#     rates = [3.67, 4.07, 3.04, 3.89]
#     currency_loop_helper(get_historical_currency_rate, dates_rate, rates, currency_name)
#

# def test_get_historical_gold_rate():
#
#     """
#
#     Test if gold rate is correct with given date
#
#     """
#     rates = [153.50, 162.49, 123.86, 155.10]
#     gold_loop_helper(get_historical_gold_rate, dates_rate, rates)


