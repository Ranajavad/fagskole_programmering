# fagskole_programmering
# API-prosjekt – Dataanalyse

## Om prosjektet

Dette prosjektet er et Python-program som henter og analyserer data fra to forskjellige API-er.

Programmet bruker:

1. **OpenWeatherMap Geocoding API** for å finne geografiske koordinater for norske byer.
2. **Sunrise-Sunset API** for å hente informasjon om soloppgang, solnedgang og månen basert på koordinatene.

Programmet bruker Oslo som eksempel for analysene.

## API-nøkkel

OpenWeatherMap krever en API-nøkkel. API-nøkkelen lagres trygt ved hjelp av Python `keyring` og ligger derfor ikke direkte i kildekoden.

For å lagre sin egen API-nøkkel i Keyring kan man bruke:

```bash
python -m keyring set openweathermap api-key
```

Deretter skriver man inn sin egen OpenWeatherMap API-nøkkel.

Sunrise-Sunset API krever ikke API-nøkkel.

## Installasjon

Programmet krever Python og følgende Python-pakker:

```bash
pip install requests keyring
```

Det anbefales å bruke et virtuelt miljø (`.venv`).

## Kjøre programmet

Åpne terminalen i prosjektmappen og kjør:

```bash
python arbeidskrav1/open_weather_map_api.py
```

Før programmet kjøres må OpenWeatherMap API-nøkkelen være lagret i Keyring.

## Hva programmet gjør

Programmet:

* Henter koordinater for Oslo, Bergen og Trondheim fra OpenWeatherMap.
* Bruker koordinatene fra OpenWeatherMap som input til Sunrise-Sunset API.
* Henter dagens soloppgang og solnedgang.
* Henter dagens månefase og månebelysning.
* Henter solinformasjon for alle dagene i september 2026.
* Beregner hvor mye kortere dagslyset blir fra 1. til 30. september.
* Finner dagen med høyest månebelysning de siste seks månedene.
* Gjennomfører en egen analyse av endringen i dagslengde.
* Demonstrerer bruk av `datetime`, `timedelta` og ISO 8601-datoformat.

## API-er

### OpenWeatherMap

OpenWeatherMap brukes til å hente geografiske koordinater basert på bynavn.

API:
https://openweathermap.org/api

### Sunrise-Sunset API

Sunrise-Sunset API brukes til å hente informasjon om soloppgang, solnedgang og måneinformasjon basert på breddegrad, lengdegrad og dato.

API:
https://sunrise-sunset.org/api

## Viktig om API-nøkkelen

API-nøkkelen skal ikke legges direkte inn i Python-koden eller lastes opp til GitHub.

Hver bruker må skaffe sin egen OpenWeatherMap API-nøkkel og lagre den lokalt i Keyring.
