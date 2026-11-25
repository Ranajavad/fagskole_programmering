
from abc import ABC, abstractmethod
from typing import Any
import requests
import json


class ApiBase(ABC):

    def __init__(self, url: str, params: dict):
        self.url: str = url
        self.params: dict = params

    @abstractmethod
    def get_results(self) -> Any:
        pass

    def getrequest(self) -> Any:

        response = requests.get(self.url, self.params)

        if response.status_code == 200:
            return json.loads(response.text)

        else:
            raise Exception(
                f"Request failed to retrieve data. "
                f"Status code {response.status_code}"
            )
