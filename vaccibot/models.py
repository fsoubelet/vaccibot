from typing import List

from pydantic import BaseModel, HttpUrl


class AppointmentMatch(BaseModel):
    center_name: str
    center_city: str
    distance_km: float
    next_appointment_time: str
    vaccines: List[str]
    url: HttpUrl
