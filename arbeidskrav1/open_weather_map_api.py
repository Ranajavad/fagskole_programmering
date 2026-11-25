
from datetime import datetime, timedelta
import keyring

from openweathermap_api import OpenWeatherMapApi
from sunrise_sunset_api import SunriseSunsetApi


# API URLs
geo_url: str = "http://api.openweathermap.org/geo/1.0/direct"
sun_url: str = "https://api.sunrise-sunset.org/v2"


# Hent API-nøkkel fra Keyring
apikey = keyring.get_password("openweathermap", "api-key")

if apikey is None:
    raise ValueError("OpenWeatherMap API key not found in Keyring")


# -------------------------------------------------
# OPENWEATHERMAP API
# -------------------------------------------------

cities: list[str] = [
    "Oslo,NO",
    "Bergen,NO",
    "Trondheim,NO"
]

coordinates = {}

for city in cities:

    geo_params: dict = {
        "q": city,
        "limit": 1,
        "appid": apikey
    }

    geo_api = OpenWeatherMapApi(geo_url, geo_params)

    geo_data = geo_api.get_results()

    coordinates[geo_data.city] = geo_data

    print(geo_data)


# Bruk Oslo sine koordinater
oslo = coordinates["Oslo"]

lat = oslo.lat
lon = oslo.lon


# -------------------------------------------------
# SUNRISE-SUNSET API
# -------------------------------------------------

today: str = datetime.now().strftime("%Y-%m-%d")


def get_sun_data(date_start: str, date_end: str):

    sun_params: dict = {
        "lat": lat,
        "lng": lon,
        "date_start": date_start,
        "date_end": date_end
    }

    sun_api = SunriseSunsetApi(sun_url, sun_params)

    return sun_api.get_results()


# -------------------------------------------------
# OPPGAVE 3.1 OG 3.3
# DAGENS SOL- OG MÅNEINFORMASJON
# -------------------------------------------------

print("\n--- Today's sun and moon information ---")

today_data = get_sun_data(today, today)

today_result = today_data[0]

print(today_result)
print(f"Sunrise: {today_result.sunrise}")
print(f"Sunset: {today_result.sunset}")
print(f"Day length: {timedelta(seconds=today_result.day_length)}")

print(f"Moon phase: {today_result.moon_phase}")
print(f"Moon illumination: {today_result.moon_illumination}%")
print(f"Moonrise: {today_result.moonrise}")
print(f"Moonset: {today_result.moonset}")


# -------------------------------------------------
# OPPGAVE 3.2
# HELE SEPTEMBER
# -------------------------------------------------

print("\n--- September 2026 ---")

september_days = get_sun_data(
    "2026-09-01",
    "2026-09-30"
)

for day in september_days:
    print(day)

first_day = september_days[0]
last_day = september_days[-1]

difference_seconds = (
    first_day.day_length - last_day.day_length
)

difference = timedelta(seconds=difference_seconds)

print(
    f"September 1 day length: "
    f"{timedelta(seconds=first_day.day_length)}"
)

print(
    f"September 30 day length: "
    f"{timedelta(seconds=last_day.day_length)}"
)

print(f"Days became shorter by: {difference}")


# -------------------------------------------------
# OPPGAVE 3.4
# SISTE SEKS MÅNEDER
# -------------------------------------------------

print("\n--- Moon analysis: last six months ---")

today_datetime = datetime.now()
six_months_ago = today_datetime - timedelta(days=183)

start_date = six_months_ago.strftime("%Y-%m-%d")
end_date = today_datetime.strftime("%Y-%m-%d")

six_months_days = get_sun_data(start_date, end_date)

brightest_day = max(
    six_months_days,
    key=lambda day: day.moon_illumination
)

print(f"Period: {start_date} to {end_date}")
print(f"Brightest moon date: {brightest_day.date}")
print(f"Moon phase: {brightest_day.moon_phase}")
print(f"Moon illumination: {brightest_day.moon_illumination}%")


# -------------------------------------------------
# OPPGAVE 3.5
# EGEN ANALYSE
# -------------------------------------------------

print("\n--- Own analysis ---")

print(
    f"In Oslo, daylight decreased by {difference} "
    "from September 1 to September 30, 2026."
)


# -------------------------------------------------
# DATETIME OG TIMEDELTA TEST
# -------------------------------------------------

print("\n--- Datetime test ---")

dt: datetime = datetime.fromisoformat(
    "2026-09-15T07:59:52+02:00"
)

print(dt)
print(dt.date())
print(dt.time())

dt2: datetime = datetime.fromisoformat(
    "2026-09-16T07:59:52+02:00"
)

duration: timedelta = dt2 - dt

print(duration)

formatted: str = dt.strftime("%Y-%m-%d %H:%M:%S")

print(formatted)
