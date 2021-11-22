from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
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
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200), index=True)
    phone = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))