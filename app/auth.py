import datetime
from cryptography.fernet import Fernet

from flask import (
    Blueprint, redirect, render_template, request, session, url_for, flash,
)
from werkzeug.security import check_password_hash, generate_password_hash
from .forms import Register, Login, FindAccount, VerifyAccount, ChangePassword
from .models import User, db
from .extension import login_manager
from flask_login import login_user, current_user
from .twf_auth import send_code
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def calc_year():
    """returns date to use for the footer of the page"""
    return datetime.date.today().year


@auth_bp.route("/register", methods=('GET', 'POST'))
def register():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(first_name=encrypt_item(form.first_name.data),
                        middle_name=encrypt_item(form.middle_name.data),
                        last_name=encrypt_item(form.last_name.data),
                        email=form.email.data,
                        password=generate_password_hash(form.password.data)
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template("auth/sign_up.html", form=form, year=calc_year())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_bp.route("/login", methods=('GET', 'POST'))
def login():
    form = Login()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('Cannot validate the user data')
        user = db.one_or_404(
            db.select(User).filter_by(email=form.email.data))
        if user is None:
            flash("User doesn't exists in the database")
            return
        if check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('product.products'))
    return render_template('auth/login.html', form=form, year=calc_year())


def logout():
    pass


@auth_bp.route('/change_password')
def change_password():
    form = ChangePassword()
    return render_template('auth/change_password.html', form=form)
    # first ask user for the username or the email
    # check if the email exists in the database
    # send the random number generated to the user email
    # comapare the random number inputed by user with the number generated
    # if true let user change the password
    # process must be completed with a minute, after a minute user must send request again for the random number
    pass


@auth_bp.route('/find_account', methods=('GET', 'POST'))
def find_account():
    form = FindAccount()
    if request.method == 'POST':
        user = db.select(User).filter_by(email=form.email.data)
        if user is not None:
            send_code(form.email.data)
            # need to send the email with the code for the verificaion purpose
            return redirect(url_for('auth.verification'))
    return render_template('auth/find_account.html', form=form)


@auth_bp.route('/verification', methods=('GET', 'POST'))
def verification():
    form = VerifyAccount()
    if request.method == "POST":
        if form.validate_on_submit():

            # get the verification code
            # compare with the code generated
            # if success procced to the change password route
            # if not return to page where user will ask for try again
            pass

    return render_template('auth/verify.html', form=form)


def encrypt_item(item):
    item = item.encode()
    key = Fernet.generate_key()
    d_key = Fernet(key)
    item = d_key.encrypt(item)
    return item
