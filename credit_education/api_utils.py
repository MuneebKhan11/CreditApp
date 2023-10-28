import os
import requests

API_TOKEN = os.environ.get('CAPITAL_ONE_API_TOKEN')
BASE_URL = "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    "version": "1.0"
}


def create_random_account(quantity=1, num_transactions=0, live_balance=True):
    endpoint = "/accounts/create"
    payload = {
        "quantity": quantity,
        "numTransactions": num_transactions,
        "liveBalance": live_balance
    }
    response = requests.post(f"{BASE_URL}{endpoint}", headers=HEADERS, json=payload)
    return response.json()


def get_all_accounts(state=None, balance_lte=None, balance_gt=None):
    endpoint = "/accounts"
    params = {}
    if state:
        params["state"] = f"eq:{state}"
    if balance_lte:
        params["balance"] = f"lte:{balance_lte}"
    if balance_gt:
        params["balance"] = f"gt:{balance_gt}"
    response = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS, params=params)
    return response.json()
