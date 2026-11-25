# fagskole_programmering

# API-prosjekt – Dataanalyse

## Endringer

I Arbeidskrav 2 er prosjektet fra Arbeidskrav 1 videreutviklet ved å organisere koden i egne klasser og bruke arv.

De viktigste endringene er:

- Opprettet `data_models.py` med klassene `GeoData` og `SunData`, som gjør API-data om til Python-objekter.
- Opprettet `api_base.py` med en abstrakt klasse kalt `ApiBase`.
- `ApiBase` inneholder felles funksjonalitet for API-forespørsler gjennom metoden `getrequest()`.
- Opprettet `OpenWeatherMapApi` og `SunriseSunsetApi`, som begge arver fra `ApiBase`.
- API-klassene implementerer metoden `get_results()` og gjør om dataene fra API-ene til objekter av riktig klasse.
- Hovedprogrammet bruker nå klassene til å hente og behandle API-data.

Funksjonaliteten fra Arbeidskrav 1 er beholdt.

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

## Prosjektstruktur

```text
fagskole_programmering/
│
├── arbeidskrav1/
│   ├── open_weather_map_api.py
│   ├── api_base.py
│   ├── data_models.py
│   ├── openweathermap_api.py
│   └── sunrise_sunset_api.py
│
├── .gitignore
└── README.md
```

## Kjøre programmet

Åpne terminalen i prosjektmappen og kjør:

```bash
python arbeidskrav1/open_weather_map_api.py
```

Før programmet kjøres må OpenWeatherMap API-nøkkelen være lagret i Keyring.

## Hva programmet gjør

Programmet:

- Henter koordinater for Oslo, Bergen og Trondheim fra OpenWeatherMap.
- Bruker koordinatene fra OpenWeatherMap som input til Sunrise-Sunset API.
- Henter dagens soloppgang og solnedgang.
- Henter dagens månefase og månebelysning.
- Henter solinformasjon for alle dagene i september 2026.
- Beregner hvor mye kortere dagslyset blir fra 1. til 30. september.
- Finner dagen med høyest månebelysning de siste seks månedene.
- Gjennomfører en egen analyse av endringen i dagslengde.
- Demonstrerer bruk av `datetime`, `timedelta` og ISO 8601-datoformat.

## Klasser og arv

Prosjektet bruker objektorientert programmering for å organisere API-kallene og dataene.

### ApiBase

`ApiBase` er en abstrakt baseklasse som inneholder felles funksjonalitet for API-forespørsler. Klassen bruker `ABC` og `abstractmethod` fra Python-biblioteket `abc`.

### GeoData og SunData

Disse klassene brukes til å representere dataene som hentes fra API-ene. De tar imot dictionaries fra API-responsene og gjør dataene om til Python-objekter.

### OpenWeatherMapApi og SunriseSunsetApi

Disse klassene arver fra `ApiBase` og implementerer egne metoder for å hente og behandle data fra hvert sitt API.

## API-er

### OpenWeatherMap

OpenWeatherMap brukes til å hente geografiske koordinater basert på bynavn.

API: https://openweathermap.org/api

### Sunrise-Sunset API

Sunrise-Sunset API brukes til å hente informasjon om soloppgang, solnedgang og måneinformasjon basert på breddegrad, lengdegrad og dato.

API: https://sunrise-sunset.org/api

## Bruk av KI

ChatGPT har blitt brukt som et støtteverktøy under arbeidet med Arbeidskrav 2. Bruken har hovedsakelig vært knyttet til å forstå objektorientert programmering, strukturering av Python-kode og feilsøking.

KI har blitt brukt til å diskutere mulige løsninger, få forklaringer på konsepter som arv og abstrakte klasser, samt få innspill til hvordan eksisterende kode kan forbedres og organiseres.

Eksempler på spørsmål om temaene i oppgaven:

- Hva er forskjellen på en klasse og en funksjon i Python?
- Hvorfor bruker man `def` inni en klasse?
- Hva gjør `__init__` og hvorfor trenger man `self`?
- Hva betyr arv i Python, og hvorfor bruker man det?
- Hva er en abstrakt klasse, og hvorfor trenger man det?
- Hva gjør `super().__init__()`?
- Hvordan kan jeg gjøre data fra et API om til objekter i Python?
- Hva er forskjellen på `@abstractmethod` og en vanlig metode?

## Viktig om API-nøkkelen

API-nøkkelen skal ikke legges direkte inn i Python-koden eller lastes opp til GitHub.

Hver bruker må skaffe sin egen OpenWeatherMap API-nøkkel og lagre den lokalt i Keyring.
