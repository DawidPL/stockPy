def loop_assertion(list_range, expected_value, actual_value):
    for i in range(len(list_range)):
        assert expected_value[i] == actual_value[i]
        # try:
        #     assert expected_value[i] == actual_value[i], "Wartości nie są równe!"
        # except AssertionError as msg:
        #     print(msg)


def nested_loop_assertion(list_range, expected_value, actual_value):
    for i in range(len(list_range)):
        assert expected_value[0][i] == actual_value[i]
