import requests
import sys
# import json
# import jsonpath
from config import *
from fixtures import *

def test_get_wallet_eth(auth_token):
    url = f"{DEV_BASE_URL}{WALLET_URL}/api/wallets/ETH"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200