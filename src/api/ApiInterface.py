from typing import Dict
from collections import defaultdict
from abc import abstractmethod, ABC

from requests.exceptions import HTTPError
import requests


class ApiInterface(ABC):

    Response = requests.models.Response

    @abstractmethod
    def serialize_to_json(self) -> Dict:
        pass

    @abstractmethod
    def __check_response_status(self) -> Response:
        pass

    @abstractmethod
    def __get_url_response(self) -> Response:
        pass

class ApiSerializerFactory(ApiInterface):

    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def serialize_to_json(self) -> Dict:
        format_data = self.__check_response_status().json()
        return format_data

    def __check_response_status(self) -> Response:
        try:
            self.__get_url_response().raise_for_status()
            url_is_valid = self.__get_url_response()
            return url_is_valid
        except HTTPError as http_err:
            print(f'Http error occured: {http_err}')

    def __get_url_response(self) -> Response:
        response_url = requests.get(self.api_url)
        return response_url
