from flask import Flask, render_template, request, session
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = b'helloworld'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/auth/login", methods=["POST"])
def auth_login():
    if request.method == "POST":
        print(request.form["username"])
    return "Hello world"

app.run(debug=True)