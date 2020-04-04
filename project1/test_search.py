import unittest
from models import Book
from search import get_books

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

      def test_valid_isbn_book(self):
         book = get_books("1416949658")
         self.assertEqual(book.title, "The Dark Is Rising")

      def test_valid_title_book(self):
         book = get_books("080213825X")
         self.assertEqual(book.title, "Four Blondes")

      def test_valid_author(self):
         book=get_books("Raymond E. Fetist")
         self.assertEqual(book.title, "Krondor: The Betrayal")




     


 if __name__ == "__main__":
    unittest.main()