
from typing import Any
from datetime import datetime, timedelta
import keyring
import os
import requests
import json


# API URLs
base_url: str = "http://api.openweathermap.org/geo/1.0/direct"
sun_url: str = "https://api.sunrise-sunset.org/v2"
limit: int = 1


def get_env_property(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        print(f"Feil: Fant ikke miljøvariabelen '{name}'")
        return ""

    return value


def get_secret(app: str, name: str) -> str:
    value = keyring.get_password(app, name)

    if value is None:
        print(f"Feil: Fant ikke nøkkelen '{name}' for '{app}'")
        return ""

    return value


def getrequest(url: str, args: dict = {}) -> Any:
    response = requests.get(url, params=args)

    if response.status_code == 200:
        data: str = response.text
        print(data)
        return json.loads(response.text)
    else:
        raise SystemError(
            f"Failed to retrieve data. Status code {response.status_code}"
        )


def get_sun_data(lat: float, lon: float, date: str) -> Any:
    sun_args: dict = {
        "lat": lat,
        "lng": lon,
        "date": date
    }

    return getrequest(sun_url, sun_args)


def get_sun_data_range(
    lat: float,
    lon: float,
    date_start: str,
    date_end: str
) -> Any:

    sun_args: dict = {
        "lat": lat,
        "lng": lon,
        "date_start": date_start,
        "date_end": date_end
    }

    return getrequest(sun_url, sun_args)


# ---------------------------------------------------------
# HENT API-NØKKEL
# ---------------------------------------------------------

env_key = get_env_property("OPENWEATHER_API_KEY")
apikey = get_secret("openweathermap", "api-key")

print("Fant env-nøkkel:", bool(env_key))
print("Fant secret-nøkkel:", bool(apikey))


# ---------------------------------------------------------
# HENT KOORDINATER FRA OPENWEATHERMAP
# ---------------------------------------------------------

cities: list[str] = [
    "Oslo,NO",
    "Bergen,NO",
    "Trondheim,NO"
]

coordinates: dict[str, tuple[float, float]] = {}

for city in cities:

    args: dict = {
        "q": city,
        "limit": limit,
        "appid": apikey
    }

    parser = getrequest(base_url, args)

    for rec in parser:
        rcity: str = rec.get("name", "Unknown")
        lat: float = rec.get("lat")
        lon: float = rec.get("lon")

        coordinates[rcity] = (lat, lon)

        print(f"City: {rcity}, coordinates: {lat},{lon}")


# Bruk Oslo sine koordinater
lat, lon = coordinates["Oslo"]


# ---------------------------------------------------------
# OPPGAVE 3.1
# DAGENS SOLINFORMASJON
# ---------------------------------------------------------

today: str = datetime.now().strftime("%Y-%m-%d")

today_data = get_sun_data(lat, lon, today)

print("\n--- Dagens solinformasjon ---")

print(f"Date: {today_data['date']}")
print(f"Sunrise: {today_data['sunrise']}")
print(f"Sunset: {today_data['sunset']}")

today_day_length: int = today_data["day_length"]

print(
    f"Day length: "
    f"{timedelta(seconds=today_day_length)}"
)


# ---------------------------------------------------------
# OPPGAVE 3.3
# MÅNENS LYSSTYRKE OG FASE I DAG
# ---------------------------------------------------------

print("\n--- Moon information today ---")

print(
    f"Moon phase: "
    f"{today_data['moon_phase']}"
)

print(
    f"Moon illumination: "
    f"{today_data['moon_illumination']}%"
)

print(
    f"Moonrise: "
    f"{today_data['moonrise']}"
)

print(
    f"Moonset: "
    f"{today_data['moonset']}"
)


# ---------------------------------------------------------
# OPPGAVE 3.2
# HELE SEPTEMBER
# ---------------------------------------------------------

print("\n--- September 2026 ---")

september_data = get_sun_data_range(
    lat,
    lon,
    "2026-09-01",
    "2026-09-30"
)

september_days = september_data["days"]


for day in september_days:

    print(f"Date: {day['date']}")
    print(f"Sunrise: {day['sunrise']}")
    print(f"Sunset: {day['sunset']}")

    day_length: int = day["day_length"]

    print(
        f"Day length: "
        f"{timedelta(seconds=day_length)}"
    )


# Første og siste dag
first_day = september_days[0]
last_day = september_days[-1]

first_day_length: int = first_day["day_length"]
last_day_length: int = last_day["day_length"]


# Beregn forskjellen i sekunder
difference_seconds: int = (
    first_day_length - last_day_length
)

difference: timedelta = timedelta(
    seconds=difference_seconds
)


print(
    f"\nSeptember 1 day length: "
    f"{timedelta(seconds=first_day_length)}"
)

print(
    f"September 30 day length: "
    f"{timedelta(seconds=last_day_length)}"
)

print(
    f"Days became shorter by: "
    f"{difference}"
)


# ---------------------------------------------------------
# OPPGAVE 3.4
# SISTE SEKS MÅNEDER
# ---------------------------------------------------------

print("\n--- Moon analysis: last six months ---")

today_datetime: datetime = datetime.now()

six_months_ago: datetime = (
    today_datetime - timedelta(days=183)
)

start_six_months: str = (
    six_months_ago.strftime("%Y-%m-%d")
)

end_six_months: str = (
    today_datetime.strftime("%Y-%m-%d")
)


six_months_data = get_sun_data_range(
    lat,
    lon,
    start_six_months,
    end_six_months
)

six_months_days = six_months_data["days"]


# Finn dagen med høyest månebelysning
brightest_day = max(
    six_months_days,
    key=lambda day: day["moon_illumination"]
)


print(
    f"Period: "
    f"{start_six_months} to {end_six_months}"
)

print(
    f"Brightest moon date: "
    f"{brightest_day['date']}"
)

print(
    f"Moon phase: "
    f"{brightest_day['moon_phase']}"
)

print(
    f"Moon illumination: "
    f"{brightest_day['moon_illumination']}%"
)


# ---------------------------------------------------------
# OPPGAVE 3.5
# EGEN ANALYSE
# ---------------------------------------------------------

print("\n--- Own analysis ---")

print(
    "Analysis: How much does daylight decrease "
    "during September?"
)

print(
    f"In Oslo, daylight decreased by "
    f"{difference} from September 1 to "
    f"September 30, 2026."
)


# ---------------------------------------------------------
# TEST AV DATETIME OG TIMEDELTA
# ---------------------------------------------------------

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


formatted: str = dt.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(formatted)
