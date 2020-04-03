# test_user.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from BaseTest import BaseTest
from user import get_user_details

class Test_User(BaseTest):

    ###############
    #### tests ####
    ###############

    def test_valid_user_login(self):
        user = get_user_details("vamsi", "vamsi_1234")
        self.assertEqual(user.username, "vamsi")

    def test_invalid_user_login(self):
        user = get_user_details("vamsi1234", "vamsi_1234")
        self.assertEqual(user, None)

    def test_invalid_isbn_book_details(self):
        book = get_user_details()
        self.assertEqual(book, None)


if __name__ == "__main__":
    unittest.main()
