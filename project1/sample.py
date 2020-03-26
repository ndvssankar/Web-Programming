import os
from flask import Flask, request, render_template
from models import *
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    # user = User(username="Siva", password="sankar", user_created_on=datetime.now())
    # db.session.add(user)
    # print("user created successfully")
    # db.session.commit()
    
    users = User.query.all()
    print (len(users))
    for user in users:
        print(f"{user.username} and password is {user.password} and created on {user.user_created_on}")

if __name__ == "__main__":
    with app.app_context():
        print("Calling main...")
        main()



