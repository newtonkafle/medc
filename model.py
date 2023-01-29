import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), unique=True)
    selling_price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    category = db.Column(db.String(20), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Columns(db.DateTime, nullable=False))
    email = db.Column(db.Column(db.String(120), unique=True, nullable=False))


class Cart(db.Model):
    pass


class Review(db.Model):
    pass
