from main import db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    selling_price = db.Column(db.Integer, nullabe=False)
    discount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullabe=False)
    brand = db.Column(db.String(100), nullabe=False)
    image = db.Column(db.String(200))
    category = db.Column(db.String(20), nullable=False)
