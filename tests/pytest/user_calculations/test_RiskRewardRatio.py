from user_calculations.RiskRewardRatio import RiskRewardRatio
from .assert_helpers import loop_assertion


def test_if_risk_reward_ratio_is_correct():
    expected_value = [150, 120]
    actual_value = [RiskRewardRatio.risk_reward_ratio(100, 10, 500),
                    RiskRewardRatio.risk_reward_ratio(100, 100, 2000),
                    ]
    loop_assertion(expected_value, expected_value, actual_value)
