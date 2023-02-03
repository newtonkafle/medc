from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, Label
from wtforms.validators import DataRequired, Length, Email


class SearchBar(FlaskForm):
    search_text = StringField('search', validators=[
                              DataRequired(), Length(max=50)])
    search_btn = SubmitField('Search')


class Login(FlaskForm):
    email = EmailField('Email address', validators=[
                       DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'placeholder': 'Enter password here..'})
    forgot_password = Label(text='Forgot password?',
                            field_id='forgot_password')
    login = SubmitField("Login")
    google_login = SubmitField("Sign In using Google Account")


class Register(FlaskForm):
    first_name = StringField('First Name', validators=[
                             DataRequired(), Length(max=50)], render_kw={'placeholder': 'Firstname..'})
    last_name = StringField('Last Name', validators=[
                            DataRequired(), Length(max=50)], render_kw={'placeholder': 'Lastname..'})
    middle_name = StringField('Middle Name', validators=[
                              DataRequired(), Length(max=50)], render_kw={'placeholder': 'Middlename..'})
    email = EmailField('Email address', validators=[
                       DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'placeholder': 'Enter password here..'})

    submit = SubmitField("Submit")
    google_login = SubmitField("Sign In using Google Account")
