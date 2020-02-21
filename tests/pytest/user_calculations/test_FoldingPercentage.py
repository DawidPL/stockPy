import pytest

from user_calculations.FoldingPercentage import folding_percentage
from .assert_helpers import nested_loop_assertion
from . import fixtures as fx


#@pytest.mark.parametrize('actual, expected', fx.faker_helper('faker.number(), faker.float(), faker.number()', num=50))
def test_if_folding_percentage_return_correct_value_in_each_step():

    expected_value = [
        [101, 102.01, 103.03, 104.06, 105.1, 106.15, 107.21, 108.29, 109.37, 110.46, 111.57, 112.68],
        [1517.1, 1534.39, 1551.89, 1569.58, 1587.47, 1605.57, 1623.87, 1642.38, 1661.11, 1680.04],
        [137.76, 169.44, 208.42],
        [1148395.7, 1173890.09, 1199950.45, 1226589.35, 1253819.63],
        [101.25, 102.29, 103.33, 104.38, 105.45],
        [12947.35, 13378.5]]
    actual_value = [folding_percentage.folding_percentage(100, 1.0, 12),
                    folding_percentage.folding_percentage(1500, 1.14, 10),
                    folding_percentage.folding_percentage(112, 23, 3),
                    folding_percentage.folding_percentage(1123455, 2.22, 5),
                    folding_percentage.folding_percentage(100.23, 1.02, 5),
                    folding_percentage.folding_percentage(12530.1, 3.33, 2)]
    nested_loop_assertion(expected_value, expected_value, actual_value)

