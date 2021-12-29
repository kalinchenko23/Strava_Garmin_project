import logging
import logging.config
import json
import pathlib
from pathlib import Path

from strava_sensitive_info_service import sensitive_info_api
from stravalib.client import Client
import time

sensitive_info_file: Path = pathlib.Path.cwd().parent / 'sensitive_info.json'

logging.config.fileConfig("/Users/maximkalinchenko/Desktop/Garmin_Strava_project/logging_file_config.conf")
logger=logging.getLogger("stravalogger")

# client info
client = Client()
client.access_token = sensitive_info_api(sensitive_info_file)[3]
client.refresh_token = sensitive_info_api(sensitive_info_file)[0]
client.expires_at = sensitive_info_api(sensitive_info_file)[4]


# getting an original access token
def original_token_retrival(code: str, client_id=sensitive_info_api(sensitive_info_file)[1],
                            client_secret=sensitive_info_api(sensitive_info_file)[2]):
    logger.info(client.exchange_code_for_token(client_id, client_secret, code))


# refreshing access token
def refresh_access_token(refresh_token=sensitive_info_api(sensitive_info_file)[0],
                         client_id=sensitive_info_api(sensitive_info_file)[1],
                         client_secret=sensitive_info_api(sensitive_info_file)[2]):
    try:
        result = client.refresh_access_token(client_id=client_id, client_secret=client_secret,
                                             refresh_token=refresh_token)
        access_token, refresh_token, expires_at = result['access_token'], result['refresh_token'], result['expires_at']
        with open(pathlib.Path('/Users/maximkalinchenko/Desktop/Garmin_Strava_project/sensitive_info.json'),
                  'r+') as file:
            data = json.load(file)
            data["strava"]["refresh_token"] = refresh_token
            data["strava"]["access_token"] = access_token
            data["strava"]["expires_at"] = expires_at
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            logger.info(f"New access and refresh tokens is are generated")
    except Exception as e:
        logger.info("Exception occurred", exc_info=True)


# check for refresh
def check_for_token_refresh(expiration: time.time() = sensitive_info_api(sensitive_info_file)[4]):
    if expiration < time.time():
        logger.info('Token needs to be refreshed!')
        refresh_access_token()
    else:
        logger.info('Token is still valid!')

