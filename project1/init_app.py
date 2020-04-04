import os
from flask import Flask, request, render_template, redirect
from flask import url_for, session, flash
from models import *

def initialize_production_app():
    app = Flask(__name__)
    app.secret_key = 'anyrandomstring'
    # Check for environment variable
    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

def initialize_testing_app():
    app = Flask(__name__)
    db = SQLAlchemy()
    
    # Check for environment variable
    if not os.getenv("TEST_DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("TEST_DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.app_context().push()
    return app

