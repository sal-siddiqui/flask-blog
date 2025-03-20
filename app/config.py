import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # forms
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # sqlachelmy
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///" + os.path.join(APP_DIR, "app.db")

    # email
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.gmail.com"
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 465)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "salmansiddiqui172002@gmail.com"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "xrdr sghe ilpr lojf "
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or False
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL") or True
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
