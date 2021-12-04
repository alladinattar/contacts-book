from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import User, Contact
from app.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app import db

import json


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
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid password or login")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are registered")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route("/api/get_contacts")
@login_required
def get_contacts():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    contacts_for_api = [contact.serialize() for contact in contacts]
    return json.dumps(contacts_for_api)
