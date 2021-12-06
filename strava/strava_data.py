import requests
import json
import pathlib
from strava_service import client , check_for_token_refresh

def getting_activity(client=client,refresh_check=check_for_token_refresh()):
    pass