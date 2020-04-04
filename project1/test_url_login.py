# project/test_url_login.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from BaseTest import BaseTestURLs

class TestLoginURL(BaseTestURLs):

    def test_login_success(self):
        response = self.app.post("/auth", data=dict(username="vamsi", password="vamsi_1234"), follow_redirects=True)
        self.assertIn("Signed in as vamsi", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_login_failure_1(self):
        response = self.app.post("/auth", data=dict(username="", password="vamsi_1234"), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_login_failure_2(self):
        response = self.app.post("/auth", data=dict(username="vamsi", password=""), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_login_failure_3(self):
        response = self.app.post("/auth", data=dict(username="", password=""), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_login_failure_4(self):
        response = self.app.post("/auth", data=dict(username="vamsi", password="vamsi"), follow_redirects=True)
        self.assertIn("Please provide valid username or password", response.data.decode())
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
