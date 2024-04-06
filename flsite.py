from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fgfgrgrgfrgrg34gfgfgf6676'

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Установка', 'url': 'install-flask'},
    {'name': 'Первое приложение', 'url': 'first-app'},
    {'name': 'Поддержка', 'url': 'contact'},
    {'name': 'Авторизоваться', 'url': 'login'},
]


@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f'Пользователь: {username}'


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template('contact.html', title='Поддержка', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'descr1pt' and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] != 'descr1pt' and request.form['psw'] != "123":
        flash('Неверный логин или пароль')

    return render_template('login.html', title='Авторизация', menu=menu)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="descr1pt"))


if __name__ == "__main__":
    app.run(debug=True)
