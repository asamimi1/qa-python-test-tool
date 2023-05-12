import pytest
import requests
import sys
import json
from config import *

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{DEV_BASE_URL}{MEMBERSHIP_URL}{API_TAG}/auth/signin", json={"username": EMAIL, "password": PASSWORD})
    token = response.json()["idToken"]
    return token