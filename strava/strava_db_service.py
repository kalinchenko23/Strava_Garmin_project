from sqlalchemy_utils import database_exists, create_database
from strava_sensitive_info_service import sensitive_info_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from strava_service import logger
sensitive_info_file = '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/sensitive_info.json'
username, password = sensitive_info_db(sensitive_info_file)

engine=create_engine()

def create_db(db_name: str, username=username, password=password):
    db_string = f'postgresql://{username}:{password}@127.0.0.1:5432/{db_name}'
    if not database_exists(db_string):
        logger.info(create_database(db_string))
    else:
        logger.info(f"Data Base with name {db_name} already exists!")
