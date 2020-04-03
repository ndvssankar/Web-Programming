from models import *
from sqlalchemy import and_

def get_user_details(username = None, password = None):

    if username is None or password is None:
        return None
    else:
        users = User.query.filter(and_(User.username==username, User.password==password)).all()
        if (len(users) == 0):
            return None
        else:
            return users[0]