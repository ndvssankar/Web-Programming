# test_user.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from user import register_user
from BaseTest import BaseTest

class TestRegisterUser(BaseTest):

    ###############
    #### tests ####
    ###############

    def test_valid_register_user(self):
        flag = register_user("sai123", "sai_12345")
        self.assertTrue(flag)

    def test_invalid_register_user(self):
        flag = register_user("vamsi", "vamsi_1234")
        self.assertFalse(flag)

    def test_invalid_isbn_book_details(self):
        flag = register_user("siva", "siva_1234")
        self.assertFalse(flag)

    def test_invalid_isbn_book_details(self):
        flag = register_user("abcdef")
        self.assertFalse(flag)

    def test_invalid_isbn_book_details(self):
        flag = register_user()
        self.assertFalse(flag)

if __name__ == "__main__":
    unittest.main()
