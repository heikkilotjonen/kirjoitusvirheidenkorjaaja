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
        self.trie.insert('testattavuus')
        self.trie.insert('sana')
        self.trie.insert('kissa')
        self.trie.insert('koira')
        self.assertTrue(self.trie.search('testi'))
        self.assertTrue(self.trie.search('testattavuus'))
        self.assertTrue(self.trie.search('sana'))
        self.assertFalse(self.trie.search('sanat'))
        self.assertFalse(self.trie.search('tseti'))
