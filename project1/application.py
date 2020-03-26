import os
from flask import Flask, request, render_template
from models import *
from datetime import datetime
from models import User

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return "Project 1: TODO"

def register_user(request):
    req = request.form
    cnt_users = User.query.filter_by(username = req.get("username")).count()
    if cnt_users == 1:
        return False
    else:
        newUser = User(req.get("username"), req.get("password"))
        db.session.add(newUser)
        db.session.commit()
        return True

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