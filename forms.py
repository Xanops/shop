from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Login/email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('repeat_password', 'Passwords must match')])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired()])
    is_seller = BooleanField('Are you seller?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class ProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    categories = StringField('Categories', validators=[DataRequired()])
    submit = SubmitField('Submit')
