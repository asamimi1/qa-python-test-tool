import requests
import sys
# import json
# import jsonpath
from config import *
from fixtures import *

def test_unsigned_agreements(auth_token):
    url = f"{DEV_BASE_URL}{MEMBERSHIP_URL}{API_TAG}/member-agreements?contextTypeId=2"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url=url, headers=headers)
    # responseJson = json.loads(response.text)
    assert response.status_code == 200
    # assert type(jsonpath.jsonpath(responseJson)[0]) == str
