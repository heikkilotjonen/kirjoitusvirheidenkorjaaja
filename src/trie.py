from distance import dl_distance


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):                         # Lisää sana trie:hen
        node = self.root
        for char in word.lower():                   # Käy läpi sanan merkit
            if char not in node.children:           # Jos merkki ei ole lapsissa, luodaan uusi solmu
                node.children[char] = TrieNode()
            # Siirrytään seuraavaan solmuun
            node = node.children[char]
        node.is_word = True

    def search(self, word):                         # Tarkistaa, onko trie:ssä sana
        node = self.root
        for char in word.lower():                   # Käy läpi sanan merkit
            if char not in node.children:           # Jos merkki ei ole lapsissa, palautetaan False
                return False
            # Siirrytään seuraavaan solmuun
            node = node.children[char]
        return node.is_word

    # Etsi sanoja, joiden edit distance on enintään max_distance
    def find_similar_words(self, word, max_distance=2):
        word_lower = word.lower()
        results = []
        # Syvyyssuuntainen haku, joka arvioi etäisyyttä ja kerää ehdotuksia
        self._dfs_similar(self.root, "", word_lower, max_distance, results)
        return results

    def _dfs_similar(self, node, prefix, target_word, max_distance, results):
        # Arvioi etäisyys nykyisestä prefixistä kohdesanaan apufunktiolla
        estimated_dist = self._estimate_distance(target_word, prefix)

        # Jos arvioitu etäisyys on suurempi kuin max_distance, polkua ei tutkita pidemmälle
        if estimated_dist > max_distance:
            return

        # Jos tämä on validi sana, laske tarkka etäisyys
        if node.is_word:
            actual_dist = dl_distance(target_word, prefix)
            if actual_dist <= max_distance:
                results.append((prefix, actual_dist))

        # Jatka syvyyssuuntaista hakua lapsisolmuihin
        for char, child in node.children.items():
            self._dfs_similar(child, prefix + char,
                              target_word, max_distance, results)

    def _estimate_distance(self, target, prefix):
        if not prefix:
            return 0

        # Vertailtava pituus, verrataan niin kauan kuin molemmissa on merkkejä
        min_len = min(len(prefix), len(target))

        # Sanojen merkkiero
        char_diff = sum(1 for i in range(min_len) if prefix[i] != target[i])

        # Jos prefix on pidempi kuin target, ylimääräiset merkit lasketaan virheiksi
        if len(prefix) > len(target):
            length_diff = len(prefix) - len(target)
            return char_diff + length_diff
        else:
            return char_diff
