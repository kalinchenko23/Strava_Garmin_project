import mongoengine
import sys

from db_service.pydantic_service import ActivityPydantic
from db_service.table_creation_functionality import Mongo_Activity, Specks
from strava.strava_data import getting_activity

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')


def add_activity_mongo():
    a = Mongo_Activity()
    last_activity_date=Mongo_Activity.objects().first().start_date
    records_to_add =[record.to_dict() for record in  getting_activity() if record.start_date.replace(tzinfo=None) > last_activity_date]
    for activity in records_to_add:
        specs = Specks().from_json(ActivityPydantic(**activity).json().replace('id', 'strava_id'))
        new_record = Mongo_Activity().from_json(
            ActivityPydantic(**activity).json().replace('id', 'strava_id'))
        new_record.specks = specs
        #new_record.save()


add_activity_mongo()
