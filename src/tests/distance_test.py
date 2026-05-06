import unittest
from distance import dl_distance


class TestDistance(unittest.TestCase):
    def test_insertion_length_one(self):
        word_1 = "tesi"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 1)
        self.assertEqual(dl_distance(word_2, word_1), 1)

    def test_insertion_length_two(self):
        word_1 = "tes"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 2)
        self.assertEqual(dl_distance(word_2, word_1), 2)

    def test_deletion_length_one(self):
        word_1 = "testti"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 1)
        self.assertEqual(dl_distance(word_2, word_1), 1)

    def test_deletion_length_two(self):
        word_1 = "testtti"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 2)
        self.assertEqual(dl_distance(word_2, word_1), 2)

    def test_substitution_length_one(self):
        word_1 = "terti"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 1)
        self.assertEqual(dl_distance(word_2, word_1), 1)

    def test_substitution_length_two(self):
        word_1 = "twrti"
        word_2 = "testi"
        self.assertEqual(dl_distance(word_1, word_2), 2)
        self.assertEqual(dl_distance(word_2, word_1), 2)

    def test_transposition_length_one(self):
        word_1 = "testi"
        word_2 = "tseti"
        self.assertEqual(dl_distance(word_1, word_2), 1)
        self.assertEqual(dl_distance(word_2, word_1), 1)

    def test_transposition_length_two(self):
        word_1 = "testi"
        word_2 = "tseit"
        self.assertEqual(dl_distance(word_1, word_2), 2)
        self.assertEqual(dl_distance(word_2, word_1), 2)
