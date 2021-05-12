import argparse

from vaccibot.constants import (
    DEFAULT_DEPARTMENTS,
    MAX_DISTANCE_KM,
    PING_INTERVAL_MINUTES,
    SELECTED_VACCINES,
    ST_GENIS_LOCATION,
    VACCINES,
)

VACCIBOT_PARSER = argparse.ArgumentParser(
    description="Fetch ViteMaDose data and find appointments within 24h around you."
)
VACCIBOT_PARSER.add_argument(
    "--location",
    type=float,
    metavar=("LAT", "LONG"),
    nargs=2,
    help="Latitude and longitude of your location. Default: St. Genis Pouilly.",
    default=ST_GENIS_LOCATION,
)
VACCIBOT_PARSER.add_argument(
    "--max-distance",
    type=int,
    help=f"Maximum radius of search from your position in km. Default: {MAX_DISTANCE_KM} km",
    default=MAX_DISTANCE_KM,
)
VACCIBOT_PARSER.add_argument(
    "--vaccines",
    type=str,
    nargs="*",
    help="Vaccines to look for. P=Pfizer-BioNTech;  M=Moderna; AZ=AstraZeneca; J=Janssen. Default: all.",
    default=list(VACCINES.keys()),
)
VACCIBOT_PARSER.add_argument(
    "--depts",
    type=str,
    nargs="*",
    help="Numbers of departments to look for vaccines in (add 0 before single-digit depts. e.g. 01 "
         "instead of 1). Default: 01 (Ain) + neighbouring departments.",
    default=DEFAULT_DEPARTMENTS,
)
ARGS = VACCIBOT_PARSER.parse_args()
