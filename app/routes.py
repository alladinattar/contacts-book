from flask import render_template, request, redirect, url_for, flash, make_response
from app import app
from app.models import User, Contact
from app.forms import LoginForm, SignUpForm, SearchForm, NewContactForm
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
def api_get_contacts():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    contacts_for_api = [contact.serialize() for contact in contacts]
    resp = make_response(json.dumps(contacts_for_api))
    resp.headers["content-type"] = "text/json"
    return resp


@app.route('/get_contacts', methods=["GET", "POST"])
@login_required
def get_contacts():
    form = SearchForm()
    form
    if form.validate_on_submit():
        contacts = Contact.query.filter_by(user_id=current_user.id).filter_by(name=form.search.data).all()
        return render_template('all_contacts.html', contacts=contacts, form=form)

    form = SearchForm()
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    return render_template('all_contacts.html', contacts=contacts, form=form)


@app.route('/add_contact', methods=["GET", 'POST'])
@login_required
def add_contact():
    form = NewContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, user_id=current_user.id, phone=form.phone.data)
        contact_checked = Contact.query.filter_by(phone=form.phone.data).first()
        if contact_checked is not None:
            return "Contact already exists"
        db.session.add(contact)
        db.session.commit()
        flash("User successfully added!!!")
        return redirect(url_for('add_contact'))

    return render_template('new_contact.html', form=form)
