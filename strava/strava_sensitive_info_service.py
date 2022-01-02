import json
import pathlib


def sensitive_info_api(path: str):
    with open(pathlib.Path(path), 'r') as file:
        data = json.load(file)
        return data['strava']['refresh_token'], data['strava']['client_id'], data['strava']['client_secret'], \
               data['strava']['access_token'], data['strava']['expires_at']


def sensitive_info_db(path: str):
    with open(pathlib.Path(path), 'r') as file:
        data = json.load(file)
        return data['data_base']['db_username'], data['data_base']['db_password'], data['data_base']['db_name']
