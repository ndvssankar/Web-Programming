from models import *

def get_book_details(isbn_number = None):

    if isbn_number is None:
        return None
    else:
        books = Book.query.filter_by(isbn=isbn_number).all()
        return books[0]