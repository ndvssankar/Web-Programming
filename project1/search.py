import os
from flask import request
from flask import render_template
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, String
from models import *
from datetime import datetime
from sqlalchemy import or_


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def get_books(searchWord):
        # print("Srch---"+searchWord)
        books = Book.query.filter(or_(Book.title==searchWord, Book.author==searchWord, Book.year==searchWord,Book.isbn==searchWord)).all()
        # print(len(books))
        if(len(books)==0):
            return [0,]
        else:
            return books

def main():
    text = "Aztec"
    get_books(text)

if __name__ == "__main__":
    with app.app_context():
        main()