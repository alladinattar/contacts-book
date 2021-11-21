from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = b'helloworld'


from app import routes