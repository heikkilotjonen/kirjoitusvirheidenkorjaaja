import time
from spellcheck import SpellChecker


def performance_test(test_word):
    spell_checker = SpellChecker()
    start_time = time.time()
    spell_checker.load_dictionary_from_file('sanakirja/kaikkisanat.txt')
    suggestions = spell_checker.suggest(test_word)
    end_time = time.time()
    print(
        f"Saatiin {len(suggestions)} ehdotusta sanalle '{test_word}' {end_time - start_time:.4f} sekunnissa.")


if __name__ == "__main__":
    performance_test("kammioves")
    performance_test("koir")
    performance_test("oikes")
