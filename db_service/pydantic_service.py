from datetime import datetime

import pytz
from pydantic import BaseModel, validator


class ActivityPydantic(BaseModel):
    id: int = None
    type: str = None
    name: str = None
    distance: float = None
    average_speed: float = None
    max_speed: float = None
    moving_time: float = None
    elapsed_time: float = None
    total_elevation_gain: float = None  # in meters
    average_heartrate: float = None
    max_heartrate: float = None
    average_cadence: float = None  # steps per minute
    start_date: datetime

    # this validator makes datetime oject timezone unaware, we have to do this in order to fix
    # an error form writing_to_db.py
    @validator('start_date', check_fields=False)
    def date_format(cls, date):
        return date.replace(tzinfo=None)

    @validator('distance', check_fields=False)
    def distance_convertion(cls, dist):
        if dist != None:
            return round(dist / 1609.34,3)

    @validator('moving_time', 'elapsed_time', check_fields=False)
    def moving_time_convertion(cls, time):
        return round(time / 60,3)