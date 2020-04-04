from models import *
from sqlalchemy import and_

def get_user_details(username = None, password = None):
    if username is None or password is None:
        return False
    else:
        users = User.query.filter(and_(User.username==username, User.password==password)).all()
        if (len(users) == 1):
            return True
        else:
            return False


def register_user(username = None, password = None):
    try:
        db.session.rollback()
        db.session.commit()
        if username == None or password == None:
            return False
        newUser = User(username=username, password=password)
        db.session.add(newUser)
        db.session.commit()
        return True
    except Exception as e:
        return False
