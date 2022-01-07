import sys

sys.path.insert(1, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_data import getting_activity
from strava_db_service_sync import session
from pydantic_service import ActivityPydantic
from strava_db_service_sync import Activity
from strava.strava_service import logger


# adding initial data to db

def add_to_db(session=session):
    with session as sess:
        sess.begin()
        records_to_add = getting_activity()
        for record in records_to_add:
            if session.query(Activity).filter(Activity.id == record['id']).count() != 1:
                sess.add(Activity(**ActivityPydantic(**record).dict()))
                logger.info(f"New record {record['name']} with id{record['id']} was added to the db")
            else:
                pass



add_to_db()
