from flask import Flask

from app.config import Config
from app.routes import bp_default_web


def create_app():
    # initalize the app
    app = Flask(__name__)

    # configure the application
    app.config.from_object(Config)

    # initalize the extensions
    # ...

    # register blueprints
    app.register_blueprint(bp_default_web)

    return app
