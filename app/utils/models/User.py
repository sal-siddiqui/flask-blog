from app.extensions import db, login_manager
from flask_login import UserMixin


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
