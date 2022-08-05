import unittest
from translator import french_to_english, english_to_french



class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("Bonjour"),
                         'Hello', "Bonjour translates to Hello")
        with self.assertRaises(TypeError):
            french_to_english()


class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour",
                         "Hello translates to Bonjour")
        with self.assertRaises(TypeError):
            english_to_french()


unittest.main()
