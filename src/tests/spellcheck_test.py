import unittest
import hypothesis.strategies as st
from hypothesis import given, settings, example
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
    
    def test_load_dictionary_from_file(self):
        # Oletetaan, että sanalista on tallennettu tiedostoon 'test_sanalista.txt'
        with open('test_sanalista.txt', 'w', encoding='utf-8') as file:
            file.write('testi\nsana\nkissa\nkoira\n')
        
        self.spell_checker.load_dictionary_from_file('test_sanalista.txt')
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

    @given(st.text(min_size=1, max_size=5))
    @settings(max_examples=100)
    def test_suggest_random_words(self, random_word):
        self.spell_checker.load_dictionary(['testi', 'sana', 'kissa', 'koira'])
        suggestions = self.spell_checker.suggest(random_word)
        for suggestion in suggestions:
            self.assertTrue(self.spell_checker.is_correct(suggestion))
