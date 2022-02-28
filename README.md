# vr-climate-api

```/``` Gets data for particular scenario in a given year

**PARAMS** via URL query parameters
* ```year``` (2020-2099) Year
* ```scenario``` (0, 1, 2) Scenario given by SSP/RCP models in increasing order

**RETURNS** JSON with following attributes:
* ```precipitation``` in mm (daily average computed by taking yearly average / 365)
* ```temperature``` json object with with ```celsius``` and ```fahrenheit``` attributes
* ```sea_level``` in m

```/decade``` Gets data for particular scenario in a given decade

**PARAMS** via URL query parameters
* ```year``` (2020, 2090) Starting year per 10-year decade
* ```scenario``` (0, 1, 2) Scenario given by SSP/RCP models in increasing order

**RETURNS** JSON with following attributes:
* ```precipitation``` in mm (daily average computed by taking yearly average / 365)
* ```temperature json``` object with with ```celsius``` and ```fahrenheit``` attributes
* ```sea_level``` in m
