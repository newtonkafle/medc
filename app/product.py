from flask import (
    Blueprint, redirect, render_template, url_for, request
)
from .forms import SearchBar
from .models import Product, db
from flask_login import login_required

product_bp = Blueprint('product', __name__, url_prefix='/products')


@product_bp.route("/")
@login_required
def products():
    products = Product.query.all()
    search_form = SearchBar()
    return render_template('product/product.html', form=search_form, products=products)
