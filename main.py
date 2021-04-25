from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('podborka.html', title='Всё что нужно - любые товары самых разных категорий.')


@app.route('/shopping_cart')
def basket():
    return render_template('shopping_cart.html', title='Корзина')


@app.route('/category/<string:category>')
def product_category(category):
    return render_template('phones.html', title='')


@app.route('/register_user')
def register_user():
    return render_template('register_user.html', title="Registration")


@app.route('/register_admin')
def register_admin():
    return render_template('register_admin.html', title='Registration')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Catalog')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
