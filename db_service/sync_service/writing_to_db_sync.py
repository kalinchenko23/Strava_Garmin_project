import sys
import datetime

from db_service.table_creation_functionality import Activity

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_data import getting_activity
from strava_db_service_sync import session_sync, engine_sync
from db_service.pydantic_service import ActivityPydantic
from strava.strava_service import strava_logger

# new 2.0 style of quering using select
from sqlalchemy import select


# adding initial data to db

def add_to_db(session=session_sync):
    with session.begin() as sess:
        most_recent_date = sess.execute(select(Activity))
        print(type(most_recent_date))
        records_to_add = getting_activity()
        for record in records_to_add:
            result = sess.execute(select(Activity.id).where(Activity.id == record['id']))
            if result.first() is None:
                sess.add(Activity(**ActivityPydantic(**record).dict()))
                strava_logger.info(f"New record {record['name']} with id{record['id']} was added to the db")


add_to_db()
