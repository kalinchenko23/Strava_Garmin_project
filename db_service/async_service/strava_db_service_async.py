import sys

from db_service.db_settings import db_string

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

# here future=True indicates that we are going to use sqlalchemy2.0 type of quering
engine_async = create_async_engine(db_string, echo=False, future=True)
# expire_on_commit=False will prevent attributes from being expired
# after commit. class_=AsyncSession specifies that we are using async mode for this session.
Session_async = sessionmaker(engine_async, expire_on_commit=False, class_=AsyncSession)
session_async = Session_async

