import requests
import sys
# import json
# import jsonpath
from config import *
from conftest import *

base_url = f"{DEV_BASE_URL}{SHOPPING_URL}{API_TAG}"

def test_get_invoice(auth_token):
    url = f"{base_url}/invoices/4738"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url=url, headers=headers)
    print(response)
    api_response_conditions(response)