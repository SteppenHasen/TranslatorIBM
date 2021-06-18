import unittest

from translator import english_to_french, english_to_german

class Testenglish_to_french(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french("Hello world"), "Bonjour le monde")
        self.assertEqual(english_to_french(""), "Nothing to translate")

class TestTestenglish_to_german(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_german("Hello world"), "Hallo Welt")
        self.assertEqual(english_to_german(""), "Nothing to translate")

if __name__ == '__main__':
    unittest.main()