<h1 align="center">
  <b>vaccibot</b>
</h1>

A simple script to find vaccination appointments around you in France in the next 24h, filtered by department and vaccine availability.

## Install

### Prerequisites

This code is compatible with `Python 3.7+`, but is not deployed to `PyPI`.
You will find a source distribution and wheels in the repository's releases tab.
One can install from the wheel with
```bash
pip install vaccibot-0.1.0-py3-none-any.whl
```

Otherwise, you can clone this repository and install with Poetry through:
```bash
git clone https://github.com/fsoubelet/vaccibot
cd vaccibot
poetry install
```

## Usage

With this package is installed in the activated enrivonment, it can be called through `python -m vaccibot`.

Detailed usage goes as follows:
```bash
usage: __main__.py [-h] [--location LAT LONG] [--max-distance MAX_DISTANCE] [--vaccines [VACCINES [VACCINES ...]]] [--depts [DEPTS [DEPTS ...]]] [--logs LOGS]

Fetch ViteMaDose data and find appointments within 24h around you.

optional arguments:
  -h, --help            show this help message and exit
  --location LAT LONG   Latitude and longitude of your location. Default: St. Genis Pouilly.
  --max-distance MAX_DISTANCE
                        Maximum radius of search from your position in km. Default: 50 km
  --vaccines [VACCINES [VACCINES ...]]
                        Vaccines to look for. P=Pfizer-BioNTech; M=Moderna; AZ=AstraZeneca; J=Janssen. Default: all.
  --depts [DEPTS [DEPTS ...]]
                        Numbers of departments to look for vaccines in (add 0 before single-digit depts. e.g. 01 instead of 1). Default: 01 (Ain) + neighbouring departments.
  --logs LOGS           The level of logging messages, either capitalized or not. Can be 'INFO', 'DEBUG' or 'TRACE'. Defaults to 'INFO'.
```

An example use would then be:
```bash
python -m vaccibot --location 46.2440083 6.0253162 --max-distance 35 --vaccines P M AZ --depts 01 38 73
```

The script will fetch the latest Vitemadose data and output the suitable appointments in formatted tables in the terminal.
If no appointments match your criteria, no results table will be shown.
For additional information during the search, you can move the logging level to `DEBUG` or even `TRACE` through the `--logs` flag.

## License

Copyright &copy; 2021 Felix Soubelet. [MIT License](LICENSE)