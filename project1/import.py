import os
import csv
import time
from models import *
import log
from init_app import initialize_testing_app

app = initialize_testing_app()
db.create_all()

def load_data_from_csv(file_name):
    f = open(file_name)
    return csv.reader(f)

def store_in_db(reader):
    books = []
    c = 0

    for isbn, title, author, year in reader:
        c += 1
        app.logger.info('%d %s %s %s %s', c, isbn, title, author, year)
        books.append(Book(isbn=isbn, title=title, author=author,year=year))

        try:
            if len(books) == 100:
                db.session.add_all(books)
                db.session.flush()
                db.session.commit()
                books = []
        except Exception as e:
            error = str(e.__dict__['orig'])
            app.logger.error("%s", error)

def main():
    store_in_db(load_data_from_csv("books.csv"))
    
if __name__ == "__main__":
    with app.app_context():
        # Book.__table__.drop()
        # User.__table__.drop()
        # db.drop_all()
        # db.session.flush()
        # db.session.commit()
        main()