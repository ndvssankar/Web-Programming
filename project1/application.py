import os
from flask import Flask, request, render_template, redirect
from flask import url_for, session, flash
from models import *
from datetime import datetime
from sqlalchemy import and_
from models import User

app = Flask(__name__)
app.secret_key = 'anyrandomstring'
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return "Project 1: TODO"

def register_user(request):
    req = request.form
    try:
        newUser = User(req.get("username"), req.get("password"))
        db.session.add(newUser)
        db.session.commit()
        return True
    except:
        return False

@app.route('/logout', methods=["GET"])
def logout():
    session["USERNAME"] = None
    return redirect(url_for("register"))

@app.route('/user_profile', methods=["GET"])
def user_profile():
    if not session["USERNAME"] is None:
        username = session["USERNAME"]
        return render_template("/user_profile.html", username=username)
    else:
        flash("Your session is closed.. Please login again")
        return redirect(url_for("register"))

@app.route('/auth', methods=["POST"])
def login():
    req = request.form
    username = req.get("username")
    password = req.get("password")
    users = User.query.filter(and_(User.username==username, User.password==password)).all()
    if len(users) == 1:
        session["USERNAME"] = req.get("username")
        return redirect(url_for("user_profile"))
    else:
        flash("Invalid username or password")
        return redirect(url_for("register"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        flag = register_user(request)
        if flag:
            return render_template("register_success.html")
        else:
            return render_template("register_failure.html")

@app.route("/admin", methods=["GET"])
def list_users():
    users = User.query.order_by(User.user_created_on.desc())
    return render_template("list_users.html", users=users)