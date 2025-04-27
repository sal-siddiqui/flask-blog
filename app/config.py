from pathlib import Path


class Config:
    # -- Forms
    SECRET_KEY = "you-will-never-guess"

    # -- SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(Path.cwd() / "app/utils/temp.sqlite")
