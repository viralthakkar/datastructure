class Trie:
    def __init__(self):
        self.root = {}

    def insert_word(self, word):
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node['end'] = True

    def load_data(self, words):
        for word in words:
            self.insert_word(word)

    def search_word(self, word):
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        return 'end' in node

    def dfs(self, node, prefix):
        words = []
        for char, child in node.items():
            if 'end' in char:
                words.append(prefix)
            else:
                words.extend(self.dfs(child, prefix + char))
        return words

    def prefix_search(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        return self.dfs(node, prefix)


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
