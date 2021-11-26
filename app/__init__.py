from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = b'helloworld'
app.config["SECRET_KEY"] = "fsdfa"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:123@localhost/contacts"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)

from app import routes