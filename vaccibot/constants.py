SECONDS_IN_DAY = 60 * 60 * 24

ST_GENIS_LOCATION = (46.2440083, 6.0253162)
PING_INTERVAL_MINUTES = 30
MAX_DISTANCE_KM = 50
DEFAULT_DEPARTMENTS = ["01", "38", "73", "74", "39", "71", "69"]

VACCINES = {"P": "Pfizer-BioNTech", "M": "Moderna", "AZ": "AstraZeneca", "J": "Janssen", "mRNA": "ARNm"}
SELECTED_VACCINES = list(VACCINES.values())

LOGURU_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)
