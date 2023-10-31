from flask_login import current_user, login_required
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Home Page

@views.route('/')
@login_required
def home():
    return render_template('home.html')

# Error Page
@views.app_errorhandler(404)
def error_page(e):
    print(e.code)
    return render_template("404.html")