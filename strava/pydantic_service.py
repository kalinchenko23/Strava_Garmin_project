from datetime import datetime
from pydantic import BaseModel, validator

class Activity(BaseModel):
    id:'int'
    type='str'
    name='str'
    distance='float'
    average_speed='float'
    max_speed='float'
    moving_time='float'
    elapsed_time='float'
    total_elevation_gain='float'# in meters
    average_heartrate='float'
    max_heartrate='float'
    average_cadence='float' # steps per minute
    start_date=datetime = None
    @validator('start_date')
    def date_format(date):
        return date.strftime("%m/%d/%y %H:%M")
    @validator('distance')
    def distance_convertion(dist):
        return dist/1609.34
    @validator('moving_time','elapsed_time')
    def moving_time_convertion(time):
        return time / 60
