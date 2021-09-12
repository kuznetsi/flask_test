import flask
import json
import flask_wtf
import wtforms


# Класс для создания подписки
class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Имя')
    email = wtforms.StringField('Почта')
    submit = wtforms.SubmitField('Отправить')


# Класс для формы заказа мороженного
class IceCreamForm(flask_wtf.FlaskForm):
    # Вкус (селекторы)
    # - черничный
    # - земляничный
    # - лакричный
    tastes = wtforms.SelectField('Вкус')
    # Топпинги (чекбоксы)
    # - Шоколадная крошка
    # - Карамель
    # - Петрушка
    toppings = wtforms.SelectMultipleField('Топпинги')
    # Размер стаканчика (радиокнопки)
    # - Маленький
    # - Большой
    # - Средний
    cup_size = wtforms.RadioField('Размер стаканчика')
    submit = wtforms.SubmitField('Отправить')


# Класс для формы регистрации
class Registrationform(flask_wtf.FlaskForm):
    email = wtforms.StringField('Почта')
    password = wtforms.PasswordField('Пароль')
    submit = wtforms.SubmitField('Отправить')


# Функци для проверки длины поля
def is_luggage_weight_valid(form, field):
    if field.data > 30:
        raise wtforms.validators.ValidationError('Вес багажа слишком велик')


# Класс для формы валидации
class LuggageForm(flask_wtf.FlaskForm):
    # validators = [wtforms.validators.input_required] - обязательно для заполнения
    surname = wtforms.StringField('Фамилия', validators=[wtforms.validators.input_required()])
    name = wtforms.PasswordField('Имя', validators=[wtforms.validators.input_required()])
    pass_id = wtforms.PasswordField('Номер паспорта', validators=[wtforms.validators.input_required()])  # Только цифры
    luggage_weight = wtforms.IntegerField(
        'Вес багажа',
        validators=[
            wtforms.validators.input_required(),
            is_luggage_weight_valid]
    )  # Вес багажа
    submit = wtforms.SubmitField('Отправить')


# with open('7_wonders.json') as f: # Открыть и прочесть файл
#     wonders = json.load(f)
# # print(data)
# # Так как это обычный писок, пройдемся по нему
# for wonder in wonders:
#     print(wonder['what'])
#
# # Добавление в список
# wonders.append({'where': 'None', 'what': 'Nothing'})
# # Проверка добавления введенных данных
# for wonder in wonders:
#     print(wonder['what'])
#
# # Добавление в список json-файл
# with open('7_wonders.json', 'w') as f: # Открываем файл на запись
#     json.dump(wonders, f, indent=4, ensure_ascii=False )
#     # (Что?, Куда хотим записывать?, Отступ (структурой будет выводиться), Нужен ли acsii?)

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'lkfjbslkjlkjblkjdbkjsdkl'


@app.route('/search')
def search_view():
    return flask.render_template('search.html')  # Будет просто возвращаться шаблон


@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe_view():
    form = SubscriptionForm()
    if flask.request.method == 'GET':
        return flask.render_template('subscribe.html', form=form)  # Будет просто возвращаться шаблон
    return form.name.data


@app.route('/luggage/', methods=['GET', 'POST'])
def luggage_view():
    form = LuggageForm()
    if flask.request.method == 'GET':
        return flask.render_template('luggage.html', form=form)  # Будет просто возвращаться шаблон
    # Метод для валидации формы
    if form.validate_on_submit():
        return 'Ok'
    else:
        return f'{form.errors}'  # Словарь ошибок


@app.route('/register/', methods=['GET', 'POST'])
def register_view():
    form = Registrationform()
    if flask.request.method == 'GET':
        return flask.render_template('register.html', form=form)  # Будет просто возвращаться шаблон
    return form.email.data


@app.route('/ice/', methods=['GET', 'POST'])
def ice_view():
    form = IceCreamForm()
    # Список из кортежей, а также можно получать из базы данных
    form.tastes.choices = [('черничный', 'черничный'), ('земляничный', 'земляничный'), ('лакричный', 'лакричный')]
    form.toppings.choices = [('Шоколадная крошка', 'Шоколадная крошка'), ('Карамель', 'Карамель'),
                             ('Петрушка', 'Петрушка')]
    form.cup_size.choices = ['Маленький', 'Большой', 'Средний']
    if flask.request.method == 'GET':
        return flask.render_template('ice.html', form=form)  # Будет просто возвращаться шаблон
    return form.tastes.data


@app.route('/getsearch/', methods=['GET'])
def get_search_view():
    # Во flask есть объект request, в котором есть атрибут args
    # args - это словарь перепараметров запроса
    # перепараметры - это значения, которые передаются в строке запроса
    mail = flask.request.args.get('mail')
    return f'Это страница поиска, параметр передан через get. Выполняется поиск по "{mail}"'


@app.route('/postsearch/', methods=['POST'])
def post_search_view():
    # Во flask есть объект request, в котором есть атрибут form
    # args - это словарь перепараметров запроса
    # перепараметры - это значения, которые передаются в строке запроса
    mail = flask.request.form.get('mail')
    return f'Это страница поиска, параметр передан через post. Выполняется поиск по "{mail}"'


if __name__ == '__main__':
    app.run(debug=True)
