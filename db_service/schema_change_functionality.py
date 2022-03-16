
# making changes to a column type as necessary
import sqlalchemy
from alembic.operations import Operations
from alembic.runtime.migration import MigrationContext

from db_service.sync_service.strava_db_service_sync import engine_sync

ctx = MigrationContext.configure(engine_sync.connect())
op = Operations(ctx)


def alter_column_type(table_name: str, column_name: str, new_column_type: sqlalchemy.sql.visitors.TraversibleType):
    op.alter_column(table_name=table_name, column_name=column_name, nullable=False, type_=new_column_type)