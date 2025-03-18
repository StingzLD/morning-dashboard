from flask import Flask, render_template
from date import get_date
from menu import get_meal, get_menu

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/menu')
def menu():
    date, day_of_week = get_date()
    menu_data = get_menu("schoolLunch")
    main, side1, side2, snack = get_meal(menu_data, date)
    return render_template('menu.html',
                           dayOfWeek=day_of_week,
                           main=main,
                           side1=side1,
                           side2=side2,
                           snack=snack)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
