import pytest

from HistoricalRate import get_historical_currency_rate


@pytest.fixture
def currency_loop_helper():
    dates_rate = ['2018-05-25', '2017-02-20', '2013-12-11']
    currencies_codes = ['JPY', 'AUD', 'GBP']
    expected_rates = [0.03, 3.76, 4.44]
    actual_rates = []
    for i in range(len(dates_rate)):
        result = get_historical_currency_rate(currencies_codes[i], dates_rate[i])
        actual_rates.append(result)
    actual_list = [(a, b) for a, b in zip(actual_rates, expected_rates)]
    return actual_list


@pytest.mark.parametrize('expected, actual', currency_loop_helper)
def test_currency_rate_equal(expected, actual):

    """

    Test if currency code is correct with given date and rate

    """
    assert expected == actual



    #for (rate, rate_b) in zip(actual_rates_list, expected_rate_list):
        #assert rate == rate_b




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


