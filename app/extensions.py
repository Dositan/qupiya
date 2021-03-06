"""Extensions module. Each defined ext gets initialized at `__init__.py`"""
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
bcrypt = Bcrypt()
