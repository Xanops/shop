import flask_login
from data import db_session
from data.products import Product
from data.users import User
from data.categories import Category
from flask import Flask, render_template, redirect, abort
from forms import *

app = Flask(__name__, template_folder='templates')
login_manager = flask_login.LoginManager()


@app.route('/')
def index():
    session = db_session.create_session()
    data = session.query(Product).all()
    return render_template('podborka.html', title='Всё что нужно - любые товары самых разных категорий.',
        current_user=flask_login.current_user, data=data)


@app.route('/category/<string:category>')
def product_category(category):
    return render_template('phones.html', title='')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Catalog')


@app.route('/shopping_cart')
def basket():
    return render_template('shopping_cart.html', title='Корзина')


@app.route('/register_user', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        # noinspection PyArgumentList
        user = User(username=form.username.data, email=form.email.data,
                    is_seller=form.is_seller.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        flask_login.login_user(user)
        return redirect('/')
    return render_template('register.html', title='Registration',
                           current_user=flask_login.current_user, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            flask_login.login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', title='Authorization',
                               form=form, current_user=flask_login.current_user,
                               message="Incorrect login or password")
    return render_template('login.html', title='Login', form=form, current_user=flask_login.current_user)


@flask_login.login_required
@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    session = db_session.create_session()
    product = session.query(Product).get(product_id)
    if flask_login.current_user.is_seller and product:
        session.delete(product)
        session.commit()
        return redirect('/')
    else:
        return abort(404)


@flask_login.login_required
@app.route('/change_product/<int:product_id>', methods=['GET', 'POST'])
def change_product(product_id):
    session = db_session.create_session()
    form = ProductForm()
    product = session.query(Product).get(product_id)
    if form.validate_on_submit():
        product.title = form.title.data
        product.description = form.description.data
        product.price = form.price.data
        for category_title in form.categories.data.split(', '):
            category = session.query(Category).filter(Category.title == category_title).first()
            if category:
                product.categories.append(category)
            else:
                # noinspection PyArgumentList
                category = Category(title=category_title)
                session.add(category)
                product.categories.append(category)
        session.commit()
        return redirect('/')
    if flask_login.current_user.is_seller and product:
        form.title.data = product.title
        form.description.data = product.description
        form.price.data = product.price
        form.categories.data = ', '.join(map(str, product.categories))
        return render_template('form.html', title='Change Product', form=form,
                               current_user=flask_login.current_user)
    return redirect('/')


@flask_login.login_required
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    session = db_session.create_session()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        product = Product(title=form.title.data, description=form.title.description, price=form.price.data)
        for category_title in form.categories.data.split(', '):
            category = session.query(Category).filter(Category.title == category_title).first()
            if category:
                product.categories.append(category)
            else:
                # noinspection PyArgumentList
                category = Category(title=category_title)
                session.add(category)
                product.categories.append(category)
        session.add(product)
        session.commit()
        return redirect('/')
    if flask_login.current_user.is_seller:
        return render_template('form.html', title='Add Job', form=form,
                               current_user=flask_login.current_user)
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['JSON_AS_ASCII'] = False
    db_session.global_init("db/mission.db")
    login_manager.init_app(app)
    app.run(port=8080, host='127.0.0.1')
