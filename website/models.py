# file to manage sql table models
from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
