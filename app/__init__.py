from flask import Flask

from app.config import Config


def create_app():
    # initalize the app
    app = Flask(__name__)

    # configure the application
    app.config.from_object(Config)

    # initalize the extensions
    ...

    # register blueprints
    ...

    return app
