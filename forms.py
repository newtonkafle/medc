from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email


class SearchBar(FlaskForm):
    search_text = StringField('search', validators=[
                              DataRequired(), Length(max=50)])
    search_btn = SubmitField('Search')


class Login(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Length(
        max=100), Email(message='Type correct email address')], render_kw={'placeholder': 'Enter email here'})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'placeholder': 'Enter password here'})
    login = SubmitField("Login")
    google_login = SubmitField("Sign In using Google Account")
