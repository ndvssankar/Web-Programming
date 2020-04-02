# project/test_book_page.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

import unittest
from init_app import initialize_testing_app

class BaseTest(unittest.TestCase): 

    def setUp(self):
        initialize_testing_app()

    # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
  
    # executed after each test
    def tearDown(self):
        pass
 

if __name__ == "__main__":
    unittest.main()
