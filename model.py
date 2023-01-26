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
