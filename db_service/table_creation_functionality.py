# creating a table from the above class
import mongoengine

from db_service.sync_service.strava_db_service_sync import engine_sync
from strava.strava_service import strava_logger

# In this section we are creating tables for our database
from sqlalchemy import Column, Float, DateTime, BigInteger, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Activity(Base):
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

    def __str__(self):
        return f'Activity {self.id}'


async def create_activity_table(base=Base, db=engine_sync):
    try:
        async with db.begin() as conn:
            await conn.run_sync(base.metadata.create_all)
            strava_logger.info(f"Table {Activity.__tablename__} was created successfully")
    except Exception:
        strava_logger.info(f"{Exception}")


# ///////////////////////////////////////////////////////

# MongoDB portion is below

class Specks(mongoengine.EmbeddedDocument):
    distance = mongoengine.FloatField()
    average_speed = mongoengine.FloatField()
    max_speed = mongoengine.FloatField()
    moving_time = mongoengine.FloatField()
    elapsed_time = mongoengine.FloatField()
    total_elevation_gain = mongoengine.FloatField()
    average_heartrate = mongoengine.FloatField()
    max_heartrate = mongoengine.FloatField()
    average_cadence = mongoengine.FloatField()
    meta = {'strict': False}


class Mongo_Activity(mongoengine.Document):
    strava_id = mongoengine.IntField()
    type = mongoengine.StringField()
    name = mongoengine.StringField()
    start_date = mongoengine.DateTimeField()
    specks = mongoengine.EmbeddedDocumentField(Specks)
    meta = {'collection':"activity",
            'strict': False,
            'indexes': ["#id"],
            'ordering': ['-start_date'],
            }
