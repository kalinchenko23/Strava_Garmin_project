from datetime import datetime
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
    start_date: datetime = None

    @validator('start_date', check_fields=False)
    def date_format(cls, date):
        return date.strftime("%m/%d/%y %H:%M")

    @validator('distance', check_fields=False)
    def distance_convertion(cls, dist):
        if dist != None:
            return round(dist / 1609.34,3)

    @validator('moving_time', 'elapsed_time', check_fields=False)
    def moving_time_convertion(cls, time):
        return round(time / 60,3)
