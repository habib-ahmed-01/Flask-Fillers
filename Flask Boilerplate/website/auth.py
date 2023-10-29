from flask import Blueprint, render_template, redirect, request
from flask_wtf import Form, StringField, Required, Email

auth = Blueprint('auth', __name__)

class ContactForm(Form):
    username = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = StringField('password', validators=[Required()])

# Sign Up
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

    print(email, username, password)

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

