
class GeoData:

    def __init__(self, rec: dict):
        self.city: str = rec.get("name", "Unknown")
        self.lat: float = rec.get("lat", 0.0)
        self.lon: float = rec.get("lon", 0.0)

    def __str__(self) -> str:
        return (
            f"Coordinates of {self.city}: "
            f"{self.lat}, {self.lon}"
        )

    def to_dict(self) -> dict:
        return self.__dict__


class SunData:

    def __init__(self, rec: dict):
        self.date: str = rec.get("date", "")
        self.sunrise: str = rec.get("sunrise", "")
        self.sunset: str = rec.get("sunset", "")
        self.day_length: int = rec.get("day_length", 0)
        self.moon_phase: str = rec.get("moon_phase", "")
        self.moon_illumination: float = rec.get(
            "moon_illumination", 0.0
        )
        self.moonrise: str = rec.get("moonrise", "")
        self.moonset: str = rec.get("moonset", "")

    def __str__(self) -> str:
        return (
            f"Sun information for {self.date}: "
            f"Sunrise {self.sunrise}, "
            f"Sunset {self.sunset}"
        )

    def to_dict(self) -> dict:
        return self.__dict__
