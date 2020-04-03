# project/test_book_page.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from init_app import *
from flask import Flask, request, render_template
from application import *

class BaseTest(unittest.TestCase): 

    def setUp(self):
        self.app = initialize_testing_app()

    # executed after each test
    def tearDown(self):
        pass

class BaseTestURLs(unittest.TestCase):
 
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