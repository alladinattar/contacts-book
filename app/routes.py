from flask import render_template, request, redirect, url_for
from app import app
from app.forms import LoginForm, SignUpForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "POST"
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return redirect(url_for('login'))


    return render_template("register.html", form=form)

