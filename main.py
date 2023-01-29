import datetime
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from model import db
from model import Product
from forms import SearchBar, Login, Register


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.secret_key = "kjf9q4oirjfqoawcj4"
bootstrap = Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def product():
    products = Product.query.all()
    search_form = SearchBar()
    return render_template('product.html', form=search_form, products=products)


# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # calculating year for footer
    login_form = Login()
    return render_template("login.html", form=login_form, year=calc_year())


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = Register()
    return render_template("sign_up.html", form=register_form, year=calc_year())


def calc_year():
    return datetime.date.today().year


if __name__ == '__main__':
    app.run(debug=True)
