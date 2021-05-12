from typing import List

from rich import box
from rich.panel import Panel
from rich.table import Table

from vaccibot.models import AppointmentMatch

# ----- Data ----- #

COLUMNS_SETTINGS = {
    "CENTER": dict(
        justify="left",
        header_style="bold",
        style="bold",
    ),  # no_wrap=True),
    "CITY": dict(justify="center", header_style="magenta", style="magenta", no_wrap=True),
    "DISTANCE (KM)": dict(
        justify="center", header_style="medium_turquoise", style="medium_turquoise", no_wrap=True
    ),
    "NEXT APPOINTMENT": dict(justify="right", header_style="bold green3", style="bold green3", no_wrap=True),
    "AVAILABLE VACCINES": dict(
        justify="right", header_style="bold dark_orange3", style="bold dark_orange3", no_wrap=True
    ),
    "URL": dict(
        justify="right", header_style="bold cornflower_blue", style="bold cornflower_blue", no_wrap=True
    ),
}


# ----- Helpers ----- #


def _default_table() -> Table:
    """Create the default structure for the Tasks Table, hard coded columns and no rows added."""
    table = Table(box=box.SIMPLE_HEAVY)
    for header, header_col_settings in COLUMNS_SETTINGS.items():
        table.add_column(header, **header_col_settings)
    return table


def make_department_table(appointments: List[AppointmentMatch]) -> Table:
    table = _default_table()
    for appointment in appointments:
        table.add_row(
            appointment.center_name,
            appointment.center_city,
            str(appointment.distance_km),
            appointment.next_appointment_time,
            ",".join(v for v in appointment.vaccines),
            str(appointment.url),
        )
    return table
