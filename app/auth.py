import datetime
import functools
from cryptography.fernet import Fernet

from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .forms import Register, Login
from .models import User, db

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
                        email=encrypt_item(form.email.data),
                        password=generate_password_hash(form.password.data)
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template("auth/sign_up.html", form=form, year=calc_year())


@auth_bp.route("/login", methods=('GET', 'POST'))
def login():
    form = Login()
    return render_template('auth/login.html', form=form, year=calc_year())


def encrypt_item(item):
    item = item.encode()
    key = Fernet.generate_key()
    d_key = Fernet(key)
    item = d_key.encrypt(item)
    return item
