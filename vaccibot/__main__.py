import sys

from loguru import logger
from rich.console import Console, RenderGroup
from rich.panel import Panel

from vaccibot.process import retrieve_all_suitable_appointments
from vaccibot.render import make_department_table

logger.remove()
logger.add(sys.stdout, level="INFO")


@logger.catch()
def main() -> None:
    """Parses arguments from the commandline, fetches data and renders it in the terminal."""
    console = Console()
    panels = []
    suitable_appointments: dict = retrieve_all_suitable_appointments()
    for department, appointments in suitable_appointments.items():
        if appointments:  # do not make a panel and table if no appointments found
            panels.append(
                Panel(
                    make_department_table(appointments),
                    title=department,
                    expand=True,
                    border_style="scope.border",
                )
            )
    console.print(*panels)


if __name__ == "__main__":
    main()
