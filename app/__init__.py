import logging
import sys

from flask import Flask, render_template

from app import auth, commands, main
from app.extensions import bcrypt, csrf_protect, db, login_manager, migrate
from app.settings import settings


def create_app():
    """Qupiya app factory."""
    app = Flask(__name__)
    app.config.from_object(settings[app.config["ENV"]])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
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


def register_blueprints(app):
    """Register Qupiya blueprints."""
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    return None


def register_commands(app):
    """Register Qupiya commands."""
    app.cli.add_command(commands.lint)


def register_errorhandlers(app):
    """Register error handlers."""
    messages = {
        404: "Not Found",
        500: "Server Error",
    }

    def render_error(error):
        """Render error template.

        If an HTTPException, pull the `code` attribute; defaults to 500
        """
        error_code = getattr(error, "code", 500)
        return render_template("error.html", error, messages[error]), error_code

    for errcode in (404, 500):
        app.errorhandler(errcode)(render_error)
    return None


def configure_logger(app):
    """Configure Qupiya logger."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
