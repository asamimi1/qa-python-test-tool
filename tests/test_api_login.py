import requests
import sys
import json
# import jsonpath
from config import *
from conftest import *

base_url = f"{DEV_BASE_URL}{MEMBERSHIP_URL}{API_TAG}"

def test_login_step1():
    global token
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_KEY}"
    data = {"email" : EMAIL, "password" : PASSWORD, "returnSecureToken" : "true" }
    response = requests.post(url=url, json=data)
    token = response.json()["idToken"]
    api_response_conditions(response)

def test_login_step2():
    global token
    url = f"{base_url}/auth-token?authenticatorPin=888087"
    headers = {"Authorization": f"Bearer {token}" }
    response = requests.get(url=url, headers=headers)
    token = response.json()["token"]
    api_response_conditions(response)

def test_login_step3():
    global token
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={FIREBASE_KEY}"
    data = {"token" : token, "returnSecureToken" : "true" }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    api_response_conditions(response)
