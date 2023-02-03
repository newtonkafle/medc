import datetime
import os
from flask import Flask
from .extension import db, bootstrap
from .auth import auth_bp
from .product import product_bp


def create_app(test_config=None):
    # creating the application factory
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config , if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load he test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    bootstrap.init_app(app)
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()

    return app
