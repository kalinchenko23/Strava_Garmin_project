import sys
import asyncio

from db_service.async_service.strava_db_service_async import session_async
from db_service.table_creation_functionality import Activity
from strava.strava_data import getting_activity

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_service import client, check_for_token_refresh
from db_service.pydantic_service import ActivityPydantic

from strava.strava_service import strava_logger

# new 2.0 style of quering using select
from sqlalchemy import select, desc


# adding new data to db
async def add_to_db():
    async with session_async() as sess:
        async with sess.begin():
            last_activity_date = await sess.execute(select(Activity).order_by(desc(Activity.start_date)))
            records_to_add = [record for record in getting_activity() if
                              record.start_date.replace(tzinfo=None) > last_activity_date.scalars().first().start_date]
            for record in records_to_add:
                    sess.add(Activity(**ActivityPydantic(**record.to_dict()).dict()))
                    strava_logger.info(f"New record {record.name} with id{record.id} was added to the db")


asyncio.run(add_to_db())
