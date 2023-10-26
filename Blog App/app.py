from flask import Flask, render_template

app = Flask(__name__)

# 404 Page
@app.errorhandler(404)
def error_page(e):
    return render_template("404.html", title="404")

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# Login Page
@app.route("/login")
def login_page():
    return render_template("login.html", title="Login")