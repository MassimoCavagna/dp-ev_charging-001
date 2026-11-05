# EV Charging Infrastructure in Europe

A data engineering project on Databricks that explores whether Europe's EV
charging network keeps up with its electric vehicle fleet, region by region.

## Question

Which European regions have many electric cars but few charging points, and
which have the opposite? The project combines geospatial data (charger
locations and regional boundaries) with regional vehicle statistics to compare
charging infrastructure against EV adoption at NUTS2 level.

## Data sources

| Source | Content | Format |
|---|---|---|
| [Open Charge Map](https://openchargemap.org) | EV charging station locations and attributes | JSON (API) |
| [Eurostat GISCO](https://ec.europa.eu/eurostat/web/gisco) | NUTS region boundaries | GeoJSON |
| [Eurostat](https://ec.europa.eu/eurostat) | Vehicle stock and electric cars by region (`tran_r_vehst`, `tran_r_elvehst`) | TSV/CSV |

Charging data: © Open Charge Map contributors. Licensing is set per charging
location; see the Open Charge Map documentation for details.

## Architecture

Medallion architecture on Unity Catalog (catalog: `ev_charging`):

landing (raw files in a Volume) → bronze (raw Delta tables) →
silver (cleaned data, spatial join of chargers to regions) →
gold (regional metrics and under-served regions)

## Repository structure

- `setup/` catalog, schemas and volume creation
- `src/landing/` scripts that bring raw files into the Volume
- `src/bronze/` raw files to Delta tables
- `src/silver/` cleaning, typing and spatial joins
- `src/gold/` analysis-ready metrics
- `docs/` notes and architecture details

## Environment

Built on Databricks Free Edition (serverless compute, quota-limited), so the
project is deliberately scoped to small and medium-sized datasets.

## Status

Work in progress. Data downloaded: *(date to be added)*.