import sys
import sqlalchemy

sys.path.insert(1, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from sqlalchemy_utils import database_exists, create_database
import pathlib
from strava.strava_sensitive_info_service import sensitive_info_db
from strava.strava_service import logger
from sqlalchemy import Column, String, Integer, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from alembic.migration import MigrationContext
from alembic.operations import Operations

# Here we are creating engine,Session, and other important sqlalchemy components
sensitive_info_file = pathlib.Path.cwd().parent / 'sensitive_info.json'
username, password, db_name = sensitive_info_db(sensitive_info_file)
db_string = f'postgresql://{username}:{password}@127.0.0.1:5432/{db_name}'
#here future=True indicates that we are going to use sqlalchemy2.0 type of quering
engine = create_engine(db_string, echo=True, future=True)
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


class Activity(base):
    __tablename__ = 'activities'
    id = Column(BigInteger, primary_key=True)
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


# creating a table from the above class

def create_activity_table(base=base, db=engine):
    try:
        base.metadata.create_all(db)
        logger.info(f"Table {Activity.__tablename__} was created successfully")
    except Exception:
        logger.info(f"{Exception}")


# making changes to a column type as necessary
ctx = MigrationContext.configure(engine.connect())
op = Operations(ctx)


def alter_column_type(table_name: str, column_name: str, new_column_type: sqlalchemy.sql.visitors.TraversibleType):
    op.alter_column(table_name=table_name, column_name=column_name, nullable=False, type_=new_column_type)
