
from api_base import ApiBase
from data_models import SunData


class SunriseSunsetApi(ApiBase):

    def __init__(self, url: str, params: dict):
        super().__init__(url, params)

    def get_results(self) -> list[SunData]:

        parser = self.getrequest()

        data: list = parser["days"]

        results: list[SunData] = []

        for rec in data:
            results.append(SunData(rec))

        return results
