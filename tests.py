import unittest
from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishtofrench("Hello world"), "Bonjour le monde")
        self.assertEqual(englishtofrench(""), "Please enter some words.")
        self.assertEqual(englishtofrench(None), "There is nothing to translate.")

class TestTestEnglishToGerman(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishtogerman("Hello world"), "Hallo Welt")
        self.assertEqual(englishtogerman(""), "Please enter some words.")
        self.assertEqual(englishtogerman(None), "There is nothing to translate.")

unittest.main()