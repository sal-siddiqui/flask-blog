from datetime import datetime, timezone

from app.extensions import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)

    author = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.id}>"
