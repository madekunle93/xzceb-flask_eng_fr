"""
This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        english_text (str): The English text to translate.

    Returns:
        str: The French translation of the input text.
    """
    translator = MyMemoryTranslator(source="en", target="fr")
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        french_text (str): The French text to translate.

    Returns:
        str: The English translation of the input text.
    """
    translator = MyMemoryTranslator(source="fr", target="en")
    return translator.translate(french_text)