import os
from flask import Flask, request, render_template, redirect
from flask import url_for, session, flash
from models import *
from datetime import datetime
from sqlalchemy import *



# app = Flask(__name__)
# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# # app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

def get_book_details(isbn_number = None):
    db = SQLAlchemy()

    def create_app():
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.init_app(app)
        return app

    app = create_app()
    app.app_context().push()

    if isbn_number is None:
        return None
    else:
        book = Book.query.filter_by(isbn=isbn_number).all()
        return book[0]
