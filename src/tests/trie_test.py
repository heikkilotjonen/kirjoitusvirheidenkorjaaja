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

    def test_find_similar_words(self):
        self.trie.insert('testi')
        self.trie.insert('testit')
        self.trie.insert('testattavuus')
        self.trie.insert('sana')
        self.trie.insert('sanat')
        self.trie.insert('sanoja')
        self.trie.insert('moi')

        similar_to_test = self.trie.find_similar_words('test', max_distance=2)
        similar_to_san = self.trie.find_similar_words('san', max_distance=2)
        similar_to_moido = self.trie.find_similar_words(
            'moido ', max_distance=2)

        self.assertCountEqual(
            similar_to_test,
            [('testi', 1), ('testit', 2)],
        )
        self.assertCountEqual(
            similar_to_san,
            [('sana', 1), ('sanat', 2)],
        )
        self.assertCountEqual(
            similar_to_moido,
            [('moi', 2)],
        )


class TestTrieStructure(unittest.TestCase):
    def test_insert_single_word_structure(self):
        trie = Trie()
        trie.insert("cat")

        root = trie.root
        assert "c" in root.children
        c = root.children["c"]

        assert "a" in c.children
        a = c.children["a"]

        assert "t" in a.children
        t = a.children["t"]

        assert t.is_word is True

    def test_insert_creates_branches(self):
        trie = Trie()
        trie.insert("car")
        trie.insert("cat")

        root = trie.root
        c = root.children["c"]
        a = c.children["a"]

        assert "r" in a.children
        assert "t" in a.children

        assert a.children["r"].is_word is True
        assert a.children["t"].is_word is True

    def test_insert_overlapping_words(self):
        trie = Trie()
        trie.insert("car")
        trie.insert("cart")

        root = trie.root
        c = root.children["c"]
        a = c.children["a"]
        r = a.children["r"]

        assert r.is_word is True
        assert "t" in r.children
        assert r.children["t"].is_word is True

    def test_is_word_only_at_final_node(self):
        trie = Trie()
        trie.insert("to")

        root = trie.root
        t = root.children["t"]
        o = t.children["o"]

        assert t.is_word is False
        assert o.is_word is True
