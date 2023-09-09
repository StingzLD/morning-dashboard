import requests
import os

SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']

project_url = f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/menus"
headers = {
            "Authentication": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }

response = requests.get(
    url=f"{project_url}/lunch",
    headers=headers
)
response.raise_for_status()
print(response.text)
