import requests
import sys
from config import *
from conftest import *

def test_unsigned_agreements(auth_token):
    url = f"{DEV_BASE_URL}{MEMBERSHIP_URL}{API_TAG}/member-agreements?contextTypeId=2"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url=url, headers=headers)
    print(response)
    api_response_conditions(response)