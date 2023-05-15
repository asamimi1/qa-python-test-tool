import requests
import sys
import json
from config import *

def test_login_step1():
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_KEY}"
    data = {"email" : EMAIL, "password" : PASSWORD, "returnSecureToken" : "true" }
    response = requests.post(url=url, json=data)
    auth_token = response.json()["idToken"]
    assert response.status_code == 200