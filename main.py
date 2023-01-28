from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from model import db
from forms import SearchBar
from model import Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.secret_key = "kjf9q4oirjfqoawcj4"
bootstrap = Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    products = Product.query.all()
    form = SearchBar()
    return render_template('product.html', form=form, products=products)


if __name__ == '__main__':
    app.run(debug=True)
