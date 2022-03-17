import mongoengine
import sys
sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from db_service.pydantic_service import ActivityPydantic
from strava.strava_data import getting_activity

db= mongoengine.connect("strava_project")

class Specks(mongoengine.EmbeddedDocument):
    distance = mongoengine.FloatField()
    average_speed = mongoengine.FloatField()
    max_speed = mongoengine.FloatField()
    moving_time = mongoengine.FloatField()
    elapsed_time = mongoengine.FloatField()
    total_elevation_gain = mongoengine.FloatField()
    average_heartrate = mongoengine.FloatField()
    max_heartrate = mongoengine.FloatField()
    average_cadence = mongoengine.FloatField()
    meta={'strict':False}
class Activity(mongoengine.Document):
    strava_id=mongoengine.IntField()
    type=mongoengine.StringField()
    name=mongoengine.StringField()
    start_date=mongoengine.DateTimeField()
    specks=mongoengine.EmbeddedDocumentField(Specks)
    meta = {'strict': False,
          'indexes':["#id"],
          'ordering': ['-start_date'],
          }

def add_activity_mongo():
    a=Activity()
    for activity in getting_activity():
        specs=Specks().from_json(ActivityPydantic(**activity).json().replace('id','strava_id'))
        new_record=Activity().from_json(ActivityPydantic(**activity).json().replace('id','strava_id'))
        new_record.specks=specs
        # new_record.save()
add_activity_mongo()