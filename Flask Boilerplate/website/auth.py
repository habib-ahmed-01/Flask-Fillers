from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from .models import User
from . import db



auth = Blueprint('auth', __name__)

# Sign Up
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    '''The is sign-up it saves user information and saves in DB. Also it does not have extras like checking in email exists or form validations in place. Just a basic implementation of flask form, and redirects you to homepage'''
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        create_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(create_user)
        db.session.commit()
        print("Account Created")
        login_user(create_user, remember=True)
        return redirect(url_for('views.home'))

    return render_template('signup.html')

# Login
@auth.route("/login", methods=['GET','POST'])
def login():
    '''The is login it checks login info against data in DB and logs in. Just a basic implementation of flask form, and redirects you to homepage'''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print("Logged In")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template('login.html')

# Logout
@auth.route("/logout")
@login_required
def logout():
    '''The logs you out'''
    logout_user()
    return redirect(url_for('auth.login'))

