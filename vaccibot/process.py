from typing import Dict, List, Tuple

import pendulum
import requests
from geopy.distance import distance
from loguru import logger

from vaccibot.constants import *
from vaccibot.models import AppointmentMatch
from vaccibot.parsing import ARGS

CLIENT = requests.Session()
USER_LOCATION: Tuple[float, float] = ARGS.location
MAX_DISTANCE: float = ARGS.max_distance
SELECTED_VACCINES: List[str] = [VACCINES[v] for v in ARGS.vaccines]
DEPARTMENTS: List[str] = ARGS.depts


# ----- Utilities ----- #


def _get_department_numbers_and_names() -> Dict[str, str]:
    """Fetch a dict of all departments and their numbers."""
    response = CLIENT.get("https://vitemadose.gitlab.io/vitemadose/departements.json")
    response.raise_for_status()
    return {dep["code_departement"]: dep["nom_departement"] for dep in response.json()}


DEPARTMENTS_TABLE = _get_department_numbers_and_names()


# ----- Main Functionality ----- #


def find_centers_for_department(department: str) -> List[AppointmentMatch]:
    """
    Fetches all appropriate appointments from online data, returned as a list of data-validated objects.

    Args:
        department (str): the department number as a two-digit string (for instance 1 is 01). Exceptions
            made for the département Corse which has '2A' and '2B'.

    Returns:
        A list of AppointmentMatch objects, one for each suitable appointment.
    """
    logger.info(f"Looking for centers in '{DEPARTMENTS_TABLE[department]}'")
    suitable_appointments = []
    now_datetime = pendulum.now()

    response = CLIENT.get(f"https://vitemadose.gitlab.io/vitemadose/{department}.json")
    response.raise_for_status()
    department_info = response.json()

    for center in department_info["centres_disponibles"]:
        logger.debug(f"Checking if center '{center['nom']}' has an appointment in the next 24h")
        next_appointment_time = pendulum.parse(center["prochain_rdv"])

        if next_appointment_time.diff(now_datetime).in_hours() <= 24:
            logger.debug(f"'{center['nom']}' has an appointment, checking vaccines availability and location")
            vaccine_types = center["vaccine_type"]
            location = (center["location"]["latitude"], center["location"]["longitude"])
            distance_km = round(distance(location, USER_LOCATION).km)

            if (distance_km <= MAX_DISTANCE_KM) and any(
                vaccine in SELECTED_VACCINES for vaccine in vaccine_types
            ):
                suitable_appointments.append(
                    AppointmentMatch(
                        center_name=center["nom"],
                        center_city=center["location"]["city"],
                        distance_km=distance_km,
                        next_appointment_time=next_appointment_time.to_day_datetime_string(),
                        vaccines=vaccine_types,
                        url=center["url"],
                    )
                )
    return suitable_appointments


def retrieve_all_suitable_appointments() -> Dict[str, List[AppointmentMatch]]:
    """
    Retrieve appointments for all queried departments.

    Returns:
        A dictionary with a list of suitable AppointmentMatch objects for each department.
    """
    all_appointments = {}
    for department in DEPARTMENTS:
        entry = f"{DEPARTMENTS_TABLE[department]} ({department})"
        all_appointments[entry] = find_centers_for_department(department)
    return all_appointments
