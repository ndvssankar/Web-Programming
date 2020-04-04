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
        flag = get_user_details("vamsi", "vamsi_1234")
        self.assertTrue(flag)

    def test_invalid_user_login_1(self):
        flag = get_user_details("vamsi1234", "vamsi_1234")
        self.assertFalse(flag)

    def test_invalid_user_login_2(self):
        flag = get_user_details("vamsi")
        self.assertFalse(flag)

    def test_invalid_user_login_3(self):
        flag = get_user_details("", "vamsi_1234")
        self.assertFalse(flag)

    def test_invalid_user_login_4(self):
        flag = get_user_details()
        self.assertFalse(flag)


if __name__ == "__main__":
    unittest.main()
