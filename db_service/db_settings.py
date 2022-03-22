import pathlib

from sqlalchemy_utils import database_exists, create_database
from strava.strava_sensitive_info_service import sensitive_info_db
from strava.strava_service import sensitive_info_file, strava_logger
import mongoengine

mongo_db = mongoengine.connect("strava_project")
# Here we are creating engine,Session, and other important sqlalchemy components
username, password, db_name = sensitive_info_db(sensitive_info_file)
db_string_sync = f'postgresql://{username}:{password}@127.0.0.1:5432/{db_name}'
db_string_async = f'postgresql+asyncpg://{username}:{password}@127.0.0.1:5432/{db_name}'


# In this section we are checking if database exists
def create_db():
    if not database_exists(db_string_sync):
        strava_logger.info(create_database(db_string_sync))
    else:
        strava_logger.info(f"Data Base with name {db_name} already exists!")
