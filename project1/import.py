import os
import csv
from flask import Flask, request, render_template
from models import *
import log

app = Flask(__name__)

# Configuring the file for logging.
# fileConfig('logging.cfg')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def load_data_from_csv(file_name):
    f = open(file_name)
    return csv.reader(f)

def store_in_db(reader):
    books = []
    c = 0

    for isbn, title, author, year in reader:
        c += 1
        app.logger.info('%d %s %s %s %s', c, isbn, title, author, year)
        books.append(Book(isbn=isbn, title=title, author=author,year=int(year)))
        try:
            if len(books) == 100:
                db.session.add_all(books)
                db.session.flush()
                db.session.commit()
                books = []
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            app.logger.error("%s", error)

def main():
    store_in_db(load_data_from_csv("books.csv"))
    
if __name__ == "__main__":
    with app.app_context():
        main()