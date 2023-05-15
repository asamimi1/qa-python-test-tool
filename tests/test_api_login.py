import requests
import sys
import json
# import jsonpath
from config import *
# from fixtures import *

def test_login_step1():
    global auth_token
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_KEY}"
    data = {"email" : EMAIL, "password" : PASSWORD, "returnSecureToken" : "true" }
    response = requests.post(url=url, json=data)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200

def test_login_step2():
    global auth_token
    url = f"{DEV_BASE_URL}{MEMBERSHIP_URL}/api/auth-token?authenticatorPin=888087"
    headers = {"Authorization": f"Bearer {auth_token}" }
    response = requests.get(url=url, headers=headers)
    auth_token = response.json()["token"]
    assert response.status_code == 200

def test_login_step3():
    global auth_token
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={FIREBASE_KEY}"
    data = {"token" : auth_token, "returnSecureToken" : "true" }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200

