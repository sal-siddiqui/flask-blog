from flask import Flask

from app.config import Config
from app.extensions import bcrypt, db, login_manager, mail
from app.routes.authentication import bp_authentication_web
from app.routes.default import bp_default_web
from app.routes.error import bp_error_web
from app.routes.post import bp_post_web
from app.routes.user import bp_user_web


def create_app():
    # initalize the app
    app = Flask(__name__)

    # configure the application
    app.config.from_object(Config)

    # initalize the extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # register blueprints
    app.register_blueprint(bp_default_web)
    app.register_blueprint(bp_authentication_web)
    app.register_blueprint(bp_user_web)
    app.register_blueprint(bp_post_web)
    app.register_blueprint(bp_error_web)

    return app
