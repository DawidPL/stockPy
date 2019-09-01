import pytest
from typing import Any
from Helpers import api_response_status_helper, api_data_type_return_helper


@pytest.mark.parametrize('actual', api_response_status_helper())
def test_if_api_response_status_is_correct(actual) -> Any:

    assert 200 == actual


@pytest.mark.parametrize('actual', api_data_type_return_helper())
def test_if_api_return_dict_or_list_data_type(actual) -> Any:

    assert type(actual) is dict or list
