import pytest
import requests
import sys
import json
from config import *

@pytest.fixture(scope="session")
def auth_token():
    headers = {"x-api-key": "a09e57cc-f2ca-4d74-b627-0df941f67daf"}
    response = requests.post(f"{DEV_BASE_URL}{MEMBERSHIP_URL}{API_TAG}/auth/signin", headers=headers, json={"username": EMAIL, "password": PASSWORD})
    token = response.json()["idToken"]
    return token

def api_response_conditions(response):
    allowed_status_codes = [200, 201, 203, 204]
    assert response.status_code in allowed_status_codes, f"API response status code: {response.status_code}"
