from flask import render_template, url_for, request
from main import app
from forms import SearchBar
from model import Product


# User registeration route


@app.route('/register', methods=['GET', 'POST'])
def registration():
    if request == "POST":
        pass
    pass


# home route -- need to desing the homepage for the website


def home():
    pass

# product view route


@app.route('/product/<product_id>')
def product(product_id):
    pass

# cart route


def cart():
    pass


# product search route
@app.route('/product/search/<name>')
def search(name):
    pass

# payment route
