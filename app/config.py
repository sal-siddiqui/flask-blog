from pathlib import Path


class Config:
    # -- Forms
    SECRET_KEY = "you-will-never-guess"

    # -- SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(Path.cwd() / "app/utils/temp.sqlite")

    # -- Mail
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_DEFAULT_SENDER = "salmansiddiqui172002@gmail.com"
    MAIL_PASSWORD = "oovw shct mpsc sgag"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
