# project/test_book_page.py
# reference from: https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
 
import unittest
from models import Book
from book_details import get_book_details

  
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self):
        pass

    # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
  
    # executed after each test
    def tearDown(self):
        pass
 
 
    ###############
    #### tests ####
    ###############

    def test_valid_isbn_book_details(self):
        book = get_book_details("1416949658")
        self.assertEqual(book.title, "The Dark Is Rising")

    def test_valid_isbn_book_details(self):
        book = get_book_details("080213825X")
        self.assertEqual(book.title, "Four Blondes")
    
    def test_invalid_isbn_book_details(self):
        book = get_book_details()
        self.assertEqual(book, None)


if __name__ == "__main__":
    unittest.main()
