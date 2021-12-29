import requests
import json
import pathlib
from strava_service import client, check_for_token_refresh


def getting_activity(client=client, refresh_check=check_for_token_refresh()):
    refresh_check
    for activity in [activity for activity in client.get_activities()]:
        if activity.type == "Run":
            return json.dumps(activity.to_dict(),indent=4)


print(getting_activity())
