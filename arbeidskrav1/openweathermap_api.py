
from api_base import ApiBase
from data_models import GeoData


class OpenWeatherMapApi(ApiBase):

    def __init__(self, url: str, params: dict):
        super().__init__(url, params)

    def get_results(self) -> GeoData:

        data: list[GeoData] = self.getresults()

        if len(data) > 0:
            return data[0]

        raise FileNotFoundError("No geodata found")

    def getresults(self) -> list[GeoData]:

        data: list[GeoData] = []

        parser = self.getrequest()

        for rec in parser:
            data.append(GeoData(rec))

        return data
