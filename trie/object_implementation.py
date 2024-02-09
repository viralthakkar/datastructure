class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def load_data(self, words):
        for word in words:
            self.insert_word(word)

    def search_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.end

    def dfs(self, prefix, node):
        words = []

        if node.end:
            words.append(prefix)

        for char, child in node.children.items():
            words.extend(self.dfs(prefix + char, child))

        return words

    def prefix_search(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self.dfs(prefix, node)


if __name__ == '__main__':
    words = ["leet", "code", "apple", "and", "ball", "banana", "bowl"]

    t = Trie()
    t.load_data(words)
    print(t.root)
    print(t.search_word('le'))
    print(t.search_word('leet'))
    print(t.search_word('let'))
    print(t.search_word('and'))
    print(t.search_word('bo'))
    print(t.prefix_search('b'))
