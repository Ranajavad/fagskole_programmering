
from typing import Any
import keyring
import os
import requests
import json

# Gammel metode: hente API-nøkkelen direkte fra Keyring
# key: str = str(keyring.get_password("openweathermap", "api-key"))

def get_env_property(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        print(f"Feil: Fant ikke miljøvariabelen '{name}'")
        return ""

    return value

def getrequest(url: str, args: dict = {}) -> Any:
    response = requests.get(url, args)

    if response.status_code == 200:
        data: str = response.text
        print(data)
        return json.loads(response.text)
    else:
        raise SystemError(f"Failed to retrieve data. Status code {response.status_code}")

def get_secret(app: str, name: str) -> str:
    value = keyring.get_password(app, name)

    if value is None:
        print(f"Feil: Fant ikke nøkkelen '{name}' for '{app}'")
        return ""

    return value



env_key = get_env_property("OPENWEATHER_API_KEY")
apikey = get_secret("openweathermap", "api-key")

print("Fant env-nøkkel:", bool(env_key))
print("Fant secret-nøkkel:", bool(apikey))

base_url: str = "http://api.openweathermap.org/geo/1.0/direct"
limit: int = 1

cities: list[str] = ["Oslo,NO", "Bergen,NO", "Trondheim,NO"]

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

        print(f"City: {rcity}, coordinates: {lat},{lon}")