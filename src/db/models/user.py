from sqlalchemy import Integer, String
from sqlalchemy_utils import EmailType
from flask_sqlalchemy import SQLAlchemy

from src.db.database import db

class User(db.Model):
    """
    This is a base user Model
    """
    __tablename__ = 'users.user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(17), unique=True, nullable=False)
    otp_token = db.Column(db.String(254), nullable=True)
    face_image_url = db.Column(db.String(254), nullable=True)

    def __init__(self, email, mobile):
        self.email = email
        self.mobile = mobile

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)
