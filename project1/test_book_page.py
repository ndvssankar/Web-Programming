# project/test_book_page.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
 
import os
import unittest
from sqlalchemy import *
from flask import Flask, request, render_template
from models import *
from application import *
import log

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        # app = Flask(__name__)
        app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['DEBUG'] = False
        # if not os.getenv("DATABASE_URL"):
        #     raise RuntimeError("DATABASE_URL is not set")

        self.app = app.test_client()
 
        # Disable sending emails during unit testing
        # mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
    ###############
    #### tests ####
    ###############

    def test_default_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_register_default_page(self):
        response = self.app.get("/register", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_failure_page(self):
        response = self.app.get('/register', data=dict(username="sivasankar", password="Sankar@1234"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_book_page_success(self):
        response = self.app.get('/book_page', data=dict(isbn_number="1857231082"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # def test_book_page_failure(self):
    #     response = self.app.get('/book_page', data=dict(isbn_number=""), follow_redirects=True)
    #     self.assertIn("Invalid ISBN Number", response.data.decode())
    #     self.assertEqual(response.status_code, 200)
    
    # def test_valid_login(self):
    #     response = self.app.post("/auth", data=dict(username="vamsi", password="vamsi_1234", follow_redirects=True))
    #     # self.assertIn("User home page under construction", response.data.decode())
    #     self.assertEqual(response.status_code, 200)

    # def test_invalid_login(self):
    #     response = self.app.post("/auth", data=dict(username="vamsi", password="vamsi_123455", follow_redirects=True))
    #     # self.assertIn("User home page under construction", response.data.decode())
    #     self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
