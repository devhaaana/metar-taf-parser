# METAR-TAF-Parser

Parse `METAR` and `TAF` data provided by [Iowa State University](https://mesonet.agron.iastate.edu/request/download.phtml).

```console
METAR-TAF-Parser
├─ README.md
├─ data
│  ├─ METAR
│  │  ├─ RKSI_METAR_20241026.csv
│  │  └─ RKSS_METAR_20241026.csv
│  └─ TAF
├─ data_loader
│  ├─ IEM_data_load.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ IEM_data_load.cpython-39.pyc
│     └─ __init__.cpython-39.pyc
├─ main.py
├─ settings
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-39.pyc
│  │  └─ config_params.cpython-39.pyc
│  └─ config_params.py
└─ utils
   ├─ __init__.py
   ├─ __pycache__
   │  ├─ __init__.cpython-39.pyc
   │  ├─ change.cpython-39.pyc
   │  ├─ csv_manager.cpython-39.pyc
   │  ├─ load_airport_code.cpython-39.pyc
   │  └─ secrets_manager.cpython-39.pyc
   ├─ change.py
   ├─ csv_manager.py
   └─ save.py
```

## Technologies

- `Python` : 3.9

# Getting Started

## Installation

- You can install it **locally:**
  ```console
  $ git clone https://github.com/devhaaana/metar-taf-parser.git
  $ cd metar-taf-parser
  ```

## Parameters

* `station` : ICAO Code
  * default: `RKSI`
* `data` : Select From Available Data
  * default: `all`
* `startDate` : Start Date `YYYY-MM-DD`
  * default: `2023-01-01`
* `endDate` : End Date `YYYY-MM-DD`
  * default: `2023-12-31`
* `format` : Data Format
  * default: `onlycomma`
* `latlon` : Include Latitude, Longitude
  * default: `no`
* `elev` : Include Elevation
  * default: `no`
* `missing` : Represent Missing Data
  * default: `empty`
* `trace` : Represent Trace Reports
  * default: `empty`
* `direct` : Direct
  * default: `no`
* `save` : Save Excel File
  * default: `True`

## Usage

```console
python main.py --station=RKSI --data=all --startDate=2023-01-01 --endDate=2023-12-31 --format=onlycomma --latlon=no --elev=no --missing=empty --trace=empty --direct=no --save=True
```

## Reference

[Iowa State University](https://mesonet.agron.iastate.edu/request/download.phtml)
