from flask import render_template, request, session, redirect, url_for
from app import app
from domain.auth import check_user


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("register.html")


@app.route("/auth/login", methods=["POST"])
def auth_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in session:
            return redirect(url_for('/{}'.format(username)))
        if check_user(username, password):
            session['authorized'] = 'true'
            return url_for('/{}'.format(username))



    return "Hello world"

