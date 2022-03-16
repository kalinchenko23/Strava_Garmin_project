import sys

from db_service.db_settings import db_string

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from alembic.migration import MigrationContext
from alembic.operations import Operations

# here future=True indicates that we are going to use sqlalchemy2.0 type of quering
engine_sync = create_engine(db_string, echo=False, future=True)
Session_sync = sessionmaker(engine_sync)
session_sync = Session_sync

ctx_sync = MigrationContext.configure(engine_sync.connect())
op_sync = Operations(ctx_sync)
