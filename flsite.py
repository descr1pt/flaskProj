from flask import Flask, render_template, url_for

app = Flask(__name__)


menu = ["Главная", "Первая страница", "Поддержка"]


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
    return f'Пользователь: {username}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username="descr1pt"))


# if __name__ == "__main__":
#     app.run(debug=True)
