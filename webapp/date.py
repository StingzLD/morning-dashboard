from datetime import datetime

def get_date():
    raw_date = datetime.today()
    day_of_week = raw_date.strftime("%A")
    date = raw_date.strftime("%Y-%m-%d")

    return date, day_of_week
