from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    pin = db.Column(
        db.String(4),
        nullable=False
    )

    balance = db.Column(
        db.Integer,
        default=0
    )
