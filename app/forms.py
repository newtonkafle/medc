from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, Label
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchBar(FlaskForm):
    search_text = StringField('search', validators=[
                              DataRequired(), Length(max=50)])
    search_btn = SubmitField('Search')


class Login(FlaskForm):
    email = EmailField('Email address', validators=[
                       DataRequired(), Length(max=100), Email()], render_kw={'placeholder': 'Enter email here...'})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'placeholder': 'Enter password here..'})
    forgot_password = Label(text='Forgot password?',
                            field_id='forgot_password')
    login = SubmitField("Login")
    google_login = SubmitField("Sign In using Google Account")


class Register(FlaskForm):
    first_name = StringField('First Name', validators=[
                             DataRequired(), Length(max=50)],
                             render_kw={'placeholder': 'Firstname..'})
    last_name = StringField('Last Name', validators=[
                            DataRequired(), Length(max=50)],
                            render_kw={'placeholder': 'Lastname..'})
    middle_name = StringField('Middle Name', validators=[Length(max=50)],
                              render_kw={'placeholder': 'Middlename..'})
    email = EmailField('Email address', validators=[
                       DataRequired(), Length(max=100), Email()],
                       render_kw={'placeholder': 'Enter email here..'})
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=6, max=15),
                                                     EqualTo('password_confirm',
                                                             message='Password must match with confirm password')],
                             render_kw={'placeholder': 'Enter password here..'})

    password_confirm = PasswordField("Confirm password", validators=[
                                     DataRequired(), Length(min=6, max=10)],
                                     render_kw={'placeholder': 'Confirm the password..'})
    submit = SubmitField("Submit")
    google_login = SubmitField("Sign In using Google Account")


class FindAccount(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=50)],
                        render_kw={'placeholder': 'Email..'})
    gen_label = Label(text='Please enter your valid email address',
                      field_id='label')
    search = SubmitField('Find Account')


class VerifyAccount(FlaskForm):
    code_field = StringField('Verification Code', validators=[DataRequired(), Length(max=10)],
                             render_kw={'placeholder': 'Code..'})
    submit = SubmitField("Verify")
    resend = SubmitField("Resend")
