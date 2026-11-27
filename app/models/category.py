
from datetime import datetime, timezone

from app import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(80),
        nullable=False
    )

    color = db.Column(
        db.String(7),
        nullable=False,
        default="#64748b"
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    owner = db.relationship(
        "User",
        back_populates="categories"
    )

    tasks = db.relationship(
        "Task",
        back_populates="category"
    )

    def __repr__(self):
        return f"<Category {self.name}>"
