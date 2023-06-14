import unittest
from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    """
    Test cases for the translator module.
    """

    def test_english_to_french_translation(self):
        """
        Test the translation of English to French.
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("goodbye"), "au revoir")

    def test_french_to_english_translation(self):
        """
        Test the translation of French to English.
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("au revoir"), "goodbye")
        
if __name__ == '__main__':
    unittest.main()