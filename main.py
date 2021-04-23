from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('podborka.html', title='Всё что нужно - любые товары самых разных категорий.')


@app.route('/personal_cabinet')
def personal_cabinet():
    return render_template('personal_cabinet.html', title='Личный кабинет')


@app.route('/shopping_cart')
def basket():
    return render_template('shopping_cart.html', title='Корзина')


@app.route('/delivery')
def delivery():
    return render_template('delivery.html', title='Доставка')


@app.route('/pick-up_service')
def pick_up_service():
    return render_template('pick-up_service.html', title='Самовывоз')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')


@app.route('/phones')
def smartphones():
    return render_template('phones.html', title='Смартфоны')


@app.route('/laptops')
def laptops():
    return render_template('laptops.html', title='Ноутбуки')


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
