# project/test_book_page.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from BaseTest import BaseTestURLs

class BasicTests(BaseTestURLs):

    ###############
    #### tests ####
    ###############

    def test_book_page_success_1(self):
        response = self.app.get('/book_page', data=dict(isbn_number="1857231082"), follow_redirects=True)
        self.assertIn("The Black Unicorn", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_book_page_success_2(self):
        response = self.app.get('/book_page', data=dict(isbn_number="080213825X"), follow_redirects=True)
        self.assertIn("Four Blondes", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_book_page_failure_1(self):
        response = self.app.get('/book_page', data=dict(isbn_number="123456789A"), follow_redirects=True)
        self.assertIn("Invalid ISBN Number", response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_book_page_failure_2(self):
        response = self.app.get('/book_page', data=dict(isbn_number=""), follow_redirects=True)
        self.assertIn("Invalid ISBN Number", response.data.decode())
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
