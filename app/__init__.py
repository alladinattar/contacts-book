from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = b'helloworld'
app.config["SECRET_KEY"] = "fsdfa"

from app import routes