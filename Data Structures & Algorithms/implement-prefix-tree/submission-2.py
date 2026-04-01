class TrieNode:

    def __init__(self):

        self.children = {}
        self.word: bool = False

class PrefixTree:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word: str) -> None:

        current = self.root

        for char in word:

            if char not in current.children:

                # Create new TrieNode
                current.children.update({char: TrieNode()})
            
            current = current.children[char]

        current.word = True

    def search(self, word: str) -> bool:
        
        current = self.root

        for char in word:

            if char not in current.children:

                return False

            current = current.children[char]

        return current.word

    def startsWith(self, prefix: str) -> bool:

        current = self.root

        for char in prefix:

            if char not in current.children:

                return False

            current = current.children[char]

        return True
        
        