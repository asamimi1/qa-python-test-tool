import requests
import sys
import json
# import jsonpath
from config import *
# from fixtures import *

def test_login_step1():
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_KEY}"
    data = {"email" : EMAIL, "password" : PASSWORD, "returnSecureToken" : "true" }
    response = requests.post(url=url, data=data)
    responseJson = json.loads(response.text)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200

def test_login_step2():
    url = f"{DEV_BASE_URL}{MEMBERSHIP_URL}/api/auth-token?authenticatorPin=888087"
    headers = {"Authorization": f"Bearer {auth_token}" }
    response = requests.get(url=url, headers=headers)
    responseJson = json.loads(response.text)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200

def test_login_step3():
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={FIREBASE_KEY}"
    data = { {auth_token} : f"Bearer {auth_token}", "returnSecureToken" : "true" }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, headers=headers, data=data)
    responseJson = json.loads(response.text)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200

