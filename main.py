from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)


@app.route('/')
def home():
    db.create_all()
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug=True)
