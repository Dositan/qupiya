import logging
import sys
from flask import Flask

from app.settings import settings
from app.extensions import bcrypt, db, migrate, csrf_protect, login_manager

def create_app():
    """Qupiya app factory."""
    app = Flask(__name__)
    app.config.from_object(settings[app.config["ENV"]])
    register_extensions(app)
    configure_logger(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    return None

def configure_logger(app):
    """Configure app logger."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)