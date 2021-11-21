from flask import render_template, request, session, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/signup")
def signup():
    return render_template("register.html")

@app.route('/auth/signup', methods=["POST"])
def auth_signup():
    username = request.form["username"]
    password = request.form["password"]
    cofirm = request.form['confirm']


@app.route("/auth/login", methods=["POST"])
def auth_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in session:
            return redirect(url_for('/'))
        if check_user(username, password):
            session['authorized'] = 'true'
            return url_for('/')


    return redirect('/')

