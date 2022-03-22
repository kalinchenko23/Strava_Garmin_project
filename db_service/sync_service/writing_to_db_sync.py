import sys
import datetime

from dateutil.parser import parser

from db_service.table_creation_functionality import Activity

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_data import getting_activity
from strava_db_service_sync import session_sync, engine_sync
from db_service.pydantic_service import ActivityPydantic
from strava.strava_service import strava_logger

# new 2.0 style of quering using select
from sqlalchemy import select, desc


# adding initial data to db
def add_to_db(session=session_sync):
    with session.begin() as sess:
        last_activity_date = sess.execute(select(Activity).order_by(desc(Activity.start_date))).scalars().first().start_date
        records_to_add =[record.to_dict() for record in  getting_activity() if record.start_date.replace(tzinfo=None) > last_activity_date]
        for record in records_to_add:
             sess.add(Activity(**ActivityPydantic(**record).dict()))
             strava_logger.info(f"New record {record['name']} with id{record['id']} was added to the db")
add_to_db()
