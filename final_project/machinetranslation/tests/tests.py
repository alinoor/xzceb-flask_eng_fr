import unittest
from machinetranslation import translator
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french('En2Fr'))
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english('Fr2En'))
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
