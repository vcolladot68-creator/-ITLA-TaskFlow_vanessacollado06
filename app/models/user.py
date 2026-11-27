
from datetime import datetime, timezone

from flask_login import UserMixin
from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column

from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    projects = db.relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    categories = db.relationship(
        "Category",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    tasks = db.relationship(
        "Task",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"
