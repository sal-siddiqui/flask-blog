from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedSerializer as Serializer

from app.extensions import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).one()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship("Post", back_populates="author", lazy="select")

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

    def get_reset_token(self):
        serializer = Serializer(current_app.config["SECRET_KEY"])
        return serializer.dumps({"user_id": self.id})

    @staticmethod
    def verify_reset_token(token, max_age=1800):
        serializer = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = serializer.loads(token, max_age=max_age)["user_id"]
        except Exception:
            return None
        else:
            return User.query.filter_by(id=user_id).first()
