import requests
import os


SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']

project_url = f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/menus"
headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
    "Content-Type": "application/json"
}


def get_menu(menu):
    response = requests.get(
        url=f"{project_url}/{menu}",
        headers=headers
    )

    if response.status_code == 402:
        print("Monthly quota exceeded. Payment Required.")
        return 402
    else:
        return response.json()[f'{menu}']


def get_meal(menu, date):
    for meal in menu:
        if date == meal['date']:
            main = meal['main']
            side1 = meal['side1']
            side2 = meal['side2']
            snack = meal['snack']
            return main, side1, side2, snack
