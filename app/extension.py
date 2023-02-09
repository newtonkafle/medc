from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
csrf = CSRFProtect()
login_manager = LoginManager()
bootstrap = Bootstrap5()
db = SQLAlchemy()
