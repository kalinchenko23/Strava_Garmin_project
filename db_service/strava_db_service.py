import sys

sys.path.insert(1, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from sqlalchemy_utils import database_exists, create_database
import pathlib
from strava.strava_sensitive_info_service import sensitive_info_db
from strava.strava_service import logger
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#Here we are creating engine,Session, and other important sqlalchemy components
sensitive_info_file = pathlib.Path.cwd().parent / 'sensitive_info.json'
username, password, db_name = sensitive_info_db(sensitive_info_file)
db_string = f'postgresql://{username}:{password}@127.0.0.1:5432/{db_name}'
engine=create_engine(db_string, echo=True)
Session = sessionmaker(engine)
session = Session()

# In this section we are checking if database exists
def create_db():
    if not database_exists(db_string):
        logger.info(create_database(db_string))
    else:
        logger.info(f"Data Base with name {db_name} already exists!")


# In this section we are creating tables for our database
base = declarative_base()

def create_activity_table(base=base,db=engine):
    class Activity(base):
        __tablename__ = 'activities'
        id = Column(Integer, primary_key=True)
        type = Column(String, index=True)
        name = Column(String, index=True)
        distance = Column(Float)
        average_speed = Column(Float)
        max_speed = Column(Float)
        moving_time = Column(Float)
        elapsed_time = Column(Float)
        total_elevation_gain = Column(Float)
        average_heartrate = Column(Float)
        max_heartrate = Column(Float)
        average_cadence = Column(Float)
        start_date = Column(DateTime)
    try:
        base.metadata.create_all(db)
        logger.info(f"Table {Activity.__tablename__} was created successfully")
    except Exception:
        logger.info(f"{Exception}")
