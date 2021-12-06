from sqlalchemy_utils import database_exists, create_database
from strava_sensitive_info_service import sensitive_info_db

sensitive_info_file = '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/sensitive_info.json'
username, password = sensitive_info_db(sensitive_info_file)


def create_db(db_name: str, username=username, password=password):
    db_string = f'postgresql://{username}:{password}@127.0.0.1:5432/{db_name}'
    if not database_exists(db_string):
        return create_database(db_string)
    else:
        return f"Data Base with name {db_name} already exists!"
