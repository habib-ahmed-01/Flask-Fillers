from flask import Blueprint, render_template, redirect

auth = Blueprint('auth', __name__)

# Sign Up
@auth.route("/sign-up")
def sign_up():
    return render_template('signup.html')

# Login
@auth.route("/login")
def login():
    return render_template('login.html')

# Logout
@auth.route("/logout")
def logout():
    return redirect('/login')

