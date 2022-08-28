import unittest

from machinetranslation import translator

class TestTranslation(unittest.TestCase):

    def test_f2e_translates(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

    def test_f2e_empty_text(self):
        self.assertEqual(translator.french_to_english(''), '')

    def test_e2f_translates(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_e2f_empty_text(self):
        self.assertEqual(translator.english_to_french(''), '')

if __name__ == '__main__':
    unittest.main()