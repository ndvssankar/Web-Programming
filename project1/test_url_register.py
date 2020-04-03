# project/test_url_register.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from BaseTest import BaseTestURLs

class TestRegisterURL(BaseTestURLs):

    def test_default_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_default_page(self):
        response = self.app.get("/register", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_failure_page_1(self):
        response = self.app.post('/register', data=dict(username="vamsi", password="vamsi_1234"), follow_redirects=True)
        self.assertIn("User already registered...", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_register_failure_page_2(self):
        response = self.app.post('/register', data=dict(username="vamsi", password=""), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_register_failure_page_3(self):
        response = self.app.post('/register', data=dict(username="", password="vamsi_1234"), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_register_failure_page_4(self):
        response = self.app.post('/register', data=dict(username="", password=""), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
