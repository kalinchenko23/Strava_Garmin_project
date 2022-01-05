import sys
sys.path.insert(1, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_data import getting_activity
from strava_db_service import session
from pydantic_service import ActivityPydantic
from strava_db_service import Activity

#adding initial data to db

def add_to_db(session=session):
    with session as sess:
        records_to_add=getting_activity()
        for record in records_to_add:
            sess.add(Activity(**ActivityPydantic(**record).dict()))
        sess.commit()
