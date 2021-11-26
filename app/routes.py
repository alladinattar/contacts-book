from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import User
from app.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        print("Authenticated")
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        print('Hello world')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid password or login")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return redirect(url_for('login'))

    return render_template("register.html", form=form)
