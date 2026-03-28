import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert('testi')
        self.assertTrue(self.trie.search('testi'))

    def test_search(self):
        self.trie.insert('testi')
        self.assertTrue(self.trie.search('testi'))
        self.assertFalse(self.trie.search('tseti'))

    def test_get_all_words(self):
        self.trie.insert('testi')
        self.trie.insert('sana')
        self.trie.insert('kissa')
        self.trie.insert('koira')
        words = self.trie.get_all_words()
        self.assertIn('testi', words)
        self.assertIn('sana', words)
        self.assertIn('kissa', words)
        self.assertIn('koira', words)

    def test_get_all_words_with_nonexistent_prefix(self):
        self.trie.insert('testi')
        self.trie.insert('sana')
        words = self.trie.get_all_words('xyz') 
        self.assertEqual(words, [])

    def test_get_all_words_with_valid_prefix(self):
        self.trie.insert('kissa')
        self.trie.insert('koira')
        self.trie.insert('keke')
        words = self.trie.get_all_words('ki')
        self.assertIn('kissa', words)
        self.assertEqual(len(words), 1)
