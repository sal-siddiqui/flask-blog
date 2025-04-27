from app.extensions import db
from datetime import datetime, timezone


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(title={self.title}, date_posted={self.date_posted})"
