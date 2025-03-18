from datetime import datetime
from webapp.menu import get_meal, get_menu

raw_date = datetime.today()
day_of_week = raw_date.strftime("%A")
date = raw_date.strftime("%Y-%m-%d")

# menu = [{
#     'date': '2023-09-10',
#     'dayOfWeek': 'Monday',
#     'main': 'Peanut Butter & Jelly',
#     'side1': 'Berry Medley',
#     'side2': 'Yogurt',
#     'snack': 'Goldfish',
#     'id': 2
# }]
menu = get_menu("schoolLunch")
print(menu)
main, side1, side2, snack = get_meal(menu, date)
print(main, side1, side2, snack)
