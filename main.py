from datetime import datetime
from menu import get_meal, get_menu
from weather import get_weather_today

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
