import os
import search
from flask import Flask, request, render_template, redirect
from flask import url_for, session, flash, jsonify
from models import *
from datetime import datetime
from sqlalchemy import and_
from book_details import get_book_details
from init_app import initialize_production_app
from sqlalchemy import or_



try:
    app = initialize_production_app()
except Exception as e:
    print("Error: Check for Database url with respect to configurations...")

@app.route("/")
def index():
    return "Project 1: TODO"

def register_user(request):
    req = request.form
    try:
        newUser = User(req.get("username"), req.get("password"))
        db.session.add(newUser)
        db.session.commit()
        return True
    except:
        return False

@app.route('/logout', methods=["GET"])
def logout():
    session["USERNAME"] = None
    flash("User successfully logout")
    return redirect(url_for("register"))

@app.route('/user_home', methods=["GET"])
def user_home():
    if not session["USERNAME"] is None:
        username = session["USERNAME"]
        return render_template("/user_home.html", username=username)
    else:
        flash("Your session is closed.. Please login again")
        return redirect(url_for("register"))

@app.route('/book_page', methods=["GET"])
def book_page():
    # isbn_number = request.form["isbn_number"]
    isbn_number = "1416949658"
    # username = request.session["USERNAME"]
    username = "vamsi"
    if not username:
        flash("Your session is closed.. Please login again")
        return redirect(url_for("register"))
    else:
        book = get_book_details(isbn_number)
        if book is None:
            flash("Invalid ISBN Number")
            return render_template("book_page.html", book=None)
        else:
            return render_template("book_page.html", book=book)

@app.route('/auth', methods=["POST"])
def login():
    req = request.form
    username = req.get("username")
    password = req.get("password")
    users = User.query.filter(and_(User.username==username, User.password==password)).all()
    if len(users) == 1:
        session["USERNAME"] = req.get("username")
        return redirect(url_for("user_profile"))
    else:
        flash("Invalid username or password")
        return redirect(url_for("register"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        flag = register_user(request)
        if flag:
            return render_template("register_success.html")
        else:
            return render_template("register_failure.html")

@app.route("/admin", methods=["GET"])
def list_users():
    users = User.query.order_by(User.user_created_on.desc())
    return render_template("list_users.html", users=users)


@app.route("/search", methods=["POST"])
def search():
    if request.method == 'POST':
        req = request.form
        searchWord = req.get('searchword')
        # print("Srch---"+searchWord)
        # books = Book.query.filter(or_(Book.title==searchWord, Book.author==searchWord, Book.year==searchWord,Book.isbn==searchWord)).all()
        books = search.get_books(searchWord)
        if(len(books)==0):
            return render_template("user_profile.html", message="no results found")
        else:
            return render_template("user_profile.html", result = books)



@app.route('/api/search/', methods=["POST"])
def api_books():
    content= request.get_json()
    if 'type' in content and 'query' in content:
        search_query= content['type'].strip()
        books= search.get_books(search_query)
        if(len(books)==0):
            return jsonify({"Error":"No Match Found"}), 422
        else:
            l=[]
            books_json={}
            for each in books:
                d={}
                d["isbn"]=each.isbn
                l.append(d)
            books_json['books']=l
            return jsonify(books_json)
    else:
        return jsonify({"Error":"invalid search query"}), 422

@app.route("/api/book/<isbn_number>")
def book_details_web_api(isbn_number):
    print("here...... ndv ... isbn:", isbn_number)
    book = get_book_details(isbn_number)
    if book is None:
        return jsonify({"Error":"Invalid ISBN number"}), 422
    elif book:
        return jsonify({"ISBN" : book.isbn,
            "Title": book.title,
            "Author" : book.author,
            "year" : int(book.year)}), 200
    else:
        return jsonify({"Error" : "Server not ready to serve api requestss"}), 500