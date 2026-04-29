#Define a Trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    # create a root node
    def __init__(self):
        self.root = TrieNode()

    # insert () adds a word to the trie
    def insert(self, word):
        # start from the root node
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True

    def search(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end
    
    def starts_with(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True
    
# create na trie object
trie = Trie()

# insert some words
trie.insert("hello")
trie.insert("world")
trie.insert("hi")

# search for words
print("Search 'hello':", trie.search("hello"))  # True
print("Search 'world':", trie.search("world"))  # True

# search for prefixes
print("Starts with 'he':", trie.starts_with("he"))  # True
print("Starts with 'wo':", trie.starts_with("wo"))  # True
