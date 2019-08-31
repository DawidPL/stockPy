import pytest
from typing import Any
from Helpers import api_response_status_helper, api_data_type_return_helper


@pytest.mark.parametrize('actual', api_response_status_helper())
def test_api_response_status(actual) -> Any:

    """

    Test if connection with API is working

    """
    assert 200 == actual


@pytest.mark.parametrize('actual', api_data_type_return_helper())
def test_api_data_type_return(actual) -> Any:
    assert type(actual) is dict or list
