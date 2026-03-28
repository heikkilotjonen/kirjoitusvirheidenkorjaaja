import unittest
from spellcheck import SpellChecker

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.spell_checker = SpellChecker()
    
    def test_load_dictionary(self):
        self.spell_checker.load_dictionary(['testi', 'sana', 'kissa', 'koira'])
        self.assertTrue(self.spell_checker.is_correct('testi'))
        self.assertTrue(self.spell_checker.is_correct('sana'))
        self.assertTrue(self.spell_checker.is_correct('kissa'))
        self.assertTrue(self.spell_checker.is_correct('koira'))

    def test_is_correct(self):
        self.spell_checker.load_dictionary(['testi'])
        self.assertTrue(self.spell_checker.is_correct('testi'))
        self.assertFalse(self.spell_checker.is_correct('tseti'))

    def test_suggest(self):
        self.spell_checker.load_dictionary(['testi', 'sana'])
        suggestions = self.spell_checker.suggest('tseti')
        self.assertIn('testi', suggestions)
        self.assertNotIn('sana', suggestions)
