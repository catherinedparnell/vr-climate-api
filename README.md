# vr-climate-api

## Root URL:

```https://vr-climate-api.herokuapp.com```

## Endpoints
```/``` Gets data for particular scenario in a given year

**PARAMS** via URL query parameters
* ```year``` (2020-2099) Year
* ```scenario``` (0, 1, 2) Scenario given by SSP/RCP models in increasing order

**RETURNS** JSON with following attributes:
* ```precipitation``` in mm (daily average computed by taking yearly average / icelandic average precipitation days per year)
* ```temperature``` json object with with ```celsius``` and ```fahrenheit``` attributes
* ```sea_level``` in m

```/decade``` Gets data for particular scenario in a given decade

**PARAMS** via URL query parameters
* ```year``` (2020, 2090) Starting year per 10-year decade
* ```scenario``` (0, 1, 2) Scenario given by SSP/RCP models in increasing order

**RETURNS** JSON with following attributes:
* ```precipitation``` in mm (daily average computed by taking yearly average / icelandic average precipitation days per year)
* ```temperature json``` object with with ```celsius``` and ```fahrenheit``` attributes
* ```sea_level``` in m
