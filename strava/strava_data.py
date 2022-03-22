import requests
import json
import pathlib
import asyncio
from strava_service import client, check_for_token_refresh


def getting_activity(client=client, refresh_check=check_for_token_refresh()):
    refresh_check
    return [activity for activity in client.get_activities()]
