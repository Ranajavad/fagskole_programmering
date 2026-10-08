import keyring
import os


# Gammel metode: hente API-nøkkelen direkte fra Keyring
# key: str = str(keyring.get_password("openweathermap", "api-key"))

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


env_key = get_env_property("OPENWEATHER_API_KEY")
secret_key = get_secret("openweathermap", "api-key")

print("Fant env-nøkkel:", bool(env_key))
print("Fant secret-nøkkel:", bool(secret_key))

cities: list[str] = ["Oslo,NO", "Bergen,NO", "Trondheim,NO"]

for city in cities:
    print(city)