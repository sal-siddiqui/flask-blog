from flask import Flask

from app.config import Config

from app.extensions import db, migrate, bcrypt, login

from app.routes.core import bp_core_web
from app.routes.authentication import bp_authentication_web
from app.routes.users import bp_users_web
from app.routes.errors import bp_errors_web


def create_app():
    # initalize the app
    app = Flask(__name__)

    # configure the application
    app.config.from_object(Config)

    # initalize the extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login.init_app(app)

    # register blueprints
    app.register_blueprint(bp_core_web)
    app.register_blueprint(bp_authentication_web)
    app.register_blueprint(bp_users_web)
    app.register_blueprint(bp_errors_web)

    return app
