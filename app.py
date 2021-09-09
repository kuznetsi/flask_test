import random

import flask

app = flask.Flask(__name__)


# @app.route('/')
# def index():
#     night = random.random()  # Генератор случайных чисел от 0 до 1
#     return flask.render_template('index.html', night=night)


@app.route('/')
def index():
    return flask.render_template('main.html')


@app.route('/about')
def about_index():
    return flask.render_template('about.html')


@app.route('/students')
def students_view():
    students = [
        "Смирнов Хольгер Филиппович",
        "Демидович Налина Кирилловна",
        "Рыбакова Хитер Валерьевна",
        "Жуков Орион Святославович"
    ]
    return flask.render_template('students.html', students=students)


# Передача словаря в шалон
@app.route('/roses')
def roses_view():
    # Ключ - Red
    # Списоок - ["Freedom", "Forever young", "Explorer"]
    roses = {
        "Red": ["Freedom", "Forever young", "Explorer"],
        "White": ["Polar star", "Mondial", "Vendella"],
        "other": ["Engagement", "Topaz", "Miss Piggy"]
    }
    return flask.render_template('roses.html', roses=roses)

# Фильтры
@app.route('/galaxies')
def galaxies_view():
    nearby_galaxies = {
        1: {"galaxy": "Карликовая галактика в Большом Псе",
            "distance_trillionkm": 241248.627051,
            "distance_ly": 25500,
            "description": "Галактика Местной группы, находящаяся в созвездии Большого Пса..."},
        2: {"galaxy": "Большое Магелланово Облако",
            "distance_trillionkm": 1542099.06703,
            "distance_ly": 163000,
            "description": "Спутник Млечного Пути, расположенная на расстоянии около 163 тыс. св. лет..."},
        3: {"galaxy": "Карликовая эллиптическая галактика в Стрельце",
            "distance_trillionkm": 662251.133081,
            "distance_ly": 70000,
            "description": "Эллиптическая галактика-спутник Млечного Пути. Проме обычного..."}
    }
    return flask.render_template('galaxies.html', nearby_galaxies=nearby_galaxies)

if __name__ == '__main__':
    app.run(debug=True)
