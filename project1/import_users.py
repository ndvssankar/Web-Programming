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
    users = []
    c = 0

    for username, password in reader:
        c += 1
        app.logger.info('%d %s %s', c, username, password)
        users.append(User(username=username, password=password))
        try:
            if len(users) == 10:
                db.session.add_all(users)
                db.session.flush()
                db.session.commit()
                users = []
        except Exception as e:
            error = str(e.__dict__['orig'])
            app.logger.error("%s", error)

def main():
    store_in_db(load_data_from_csv("users.csv"))

if __name__ == "__main__":
    with app.app_context():
        main()