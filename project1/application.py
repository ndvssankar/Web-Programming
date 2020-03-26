import os
from flask import request
from flask import render_template
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# meta = MetaData()

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Creating a database table USERS
def create_register_table():
    meta = MetaData()
    USERS = Table(
    'USERS', meta, 
    Column('username', Integer, primary_key = True), 
    Column('password', String))
    meta.create_all(engine)
    print("Database table created successfully")


# Set up database
engine = create_engine("postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2", echo = True)
db = scoped_session(sessionmaker(bind=engine))
create_register_table()


@app.route("/")
def index():
    return "Project 1: TODO"

def show_registration_page():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return show_registration_page()
    else:
        for key, value in request.form.items():
            if (key != "submit"):
                print("key: {0}, value: {1}".format(key, value))
        return show_registration_page()