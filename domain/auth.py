import hashlib
from .models import User, Session


def check_user(username: str, password: str) -> bool:
    password_hash = hashlib.md5(password.encode())
    s = Session()
    user = s.query(User).filter(User.username == username).first()
    if user is not None:
        if user.password == password_hash:
            return True
        return False

    return False