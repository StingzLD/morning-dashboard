import requests
import os
from datetime import datetime


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


if __name__ == '__main__':
    menu = [{
        'date': '2023-09-10',
        'dayOfWeek': 'Monday',
        'main': 'Peanut Butter & Jelly',
        'side1': 'Berry Medley',
        'side2': 'Yogurt',
        'snack': 'Goldfish',
        'id': 2
    }]
    # menu = get_menu("schoolLunch")
    # print(data)

    raw_date = datetime.today()
    day_of_week = raw_date.strftime("%A")
    date = raw_date.strftime("%Y-%m-%d")
    print(day_of_week, date)

    lunch_today = get_meal(menu, date)
    print(lunch_today)
