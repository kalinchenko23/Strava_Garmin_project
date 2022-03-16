import sys
import asyncio

from db_service.async_service.strava_db_service_async import session_async
from db_service.table_creation_functionality import Activity

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from strava.strava_service import client, check_for_token_refresh
from db_service.pydantic_service import ActivityPydantic

from strava.strava_service import strava_logger

# new 2.0 style of quering using select
from sqlalchemy import select


# adding new data to db
async def getting_records():
    async with session_async as sess:
        async with sess.begin():
            most_recent_date = await sess.execute(select(Activity))
            print(most_recent_date.fetchone())
            for record in client.get_activities():
                result = await sess.execute(select(Activity).where(Activity.id == record.id))
                if result.scalar() is None:
                    sess.add(Activity(**ActivityPydantic(**record.to_dict()).dict()))
                    strava_logger.info(f"New record {record.name} with id{record.id} was added to the db")


asyncio.run(getting_records())
