import unittest


class Helpers(unittest.TestCase):

    def currency_loop_helper(self, func, date, rates, codes):
        for i in range(len(rates)):
            result = func(codes[i], date[i])
            self.assertEqual(result, rates[i])

    def gold_loop_helper(self, func, date, rates):
        for i in range(len(rates)):
            result = func(date[i])
            self.assertEqual(result, rates[i])


helper = Helpers()