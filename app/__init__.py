from flask import Flask
app = Flask(__name__)
app.secret_key = b'helloworld'


from app import routes