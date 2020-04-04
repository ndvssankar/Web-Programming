import unittest
import os
from flask import Flask, session, request, render_template, redirect, url_for
from application import app




class TestStringMethods(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        
        self.app = app.test_client()
        self.app.testing = True 
        self.assertEqual(app.debug, False)

     # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 

     # executed after each test
    def tearDown(self):
        pass

    def test_app(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.app.get("/admin")
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
