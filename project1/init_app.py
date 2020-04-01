import os
from flask import Flask, request, render_template, redirect
from flask import url_for, session, flash
from models import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'anyrandomstring'
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
return app