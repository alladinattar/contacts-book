from app import db
from hashlib import md5
from flask_login import UserMixin
from app import login
import json


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    contacts = db.relationship('Contact', backref='owner', lazy='dynamic')

    def set_password(self, password: str):
        self.password_hash = md5(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        if md5(password.encode()).hexdigest() == self.password_hash:
            return True
        return False


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(200), index=True)
    phone = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            'name': self.name,
            'phone': self.phone
        }