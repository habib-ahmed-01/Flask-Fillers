from flask import Blueprint, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

auth = Blueprint('auth', __name__)

# Sign Up
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        pass

    return render_template('signup.html')

# Login
@auth.route("/login", methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

# Logout
@auth.route("/logout")
def logout():
    return redirect('auth/login')

