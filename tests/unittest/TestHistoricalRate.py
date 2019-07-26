import unittest

from Helpers import helper
from src.HistoricalRates import get_historical_currency_rate, get_historical_gold_rate


class TestHistoricalRates(unittest.TestCase):

    dates_rate = ['2018-05-25', '2017-02-20', '2013-12-11', '2016-10-12']

    def test_currency_code(self):

        """

        Test if currency code is correct with given date and rate

        """
        currencies_codes = ['JPY', 'AUD', 'GBP', 'EUR']
        rates = [0.03, 3.12, 4.98, 4.28]
        helper.currency_loop_helper(get_historical_currency_rate, TestHistoricalRates.dates_rate,
                                    rates, currencies_codes)

    def test_currency_rate(self):

        """

        Test if currency rate is correct with given date

        """
        currency_name = ['USD'] * 4
        rates = [3.67, 4.07, 3.04, 3.89]
        helper.currency_loop_helper(get_historical_currency_rate, TestHistoricalRates.dates_rate,
                                    rates, currency_name)

    def test_get_historical_gold_rate(self):

        """

        Test if gold rate is correct with given date

        """
        rates = [153.50, 162.49, 123.86, 155.10]
        helper.gold_loop_helper(get_historical_gold_rate, TestHistoricalRates.dates_rate, rates)


