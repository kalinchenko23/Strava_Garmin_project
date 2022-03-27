import pytest
import sys

from strava.strava_service import refresh_access_token

sys.path.insert(0, '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/strava')

from strava.strava_sensitive_info_service import sensitive_info_api, sensitive_info_db


class TestSensitiveInfo:
    @pytest.fixture
    def path_for_sensitive_info(self):
        return '/Users/maximkalinchenko/Desktop/Garmin_Strava_project/sensitive_info.json'

    def test_sensitive_info_api(self,path_for_sensitive_info):
        assert len(sensitive_info_api(path_for_sensitive_info)) == 5

    def test_sensitive_info_db(self,path_for_sensitive_info):
        assert len(sensitive_info_db(path_for_sensitive_info)) == 3

class TestToken():
    def test_token_refresh(self):
        assert refresh_access_token()==None