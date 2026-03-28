import unittest
from spellcheck import SpellChecker

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.spell_checker = SpellChecker()
        self.spell_checker.load_dictionary(['testi', 'sana', 'kissa', 'koira'])

    def test_is_correct(self):
        self.assertTrue(self.spell_checker.is_correct('testi'))
        self.assertFalse(self.spell_checker.is_correct('tseti'))

    def test_suggest(self):
        suggestions = self.spell_checker.suggest('tseti')
        self.assertIn('testi', suggestions)
        self.assertNotIn('sana', suggestions)
