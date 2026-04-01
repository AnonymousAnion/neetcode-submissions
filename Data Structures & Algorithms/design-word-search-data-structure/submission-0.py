class TrieNode:

    def __init__(self):

        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        
        self.head = TrieNode()

    def addWord(self, word: str) -> None:

        current = self.head

        for char in word:

            if char not in current.children:

                current.children.update({char: TrieNode()})

            current = current.children[char]

        current.is_word = True

    def search(self, word: str, current: TrieNode = None) -> bool:

        if not current:

            current = self.head

        for i, char in enumerate(word):

            # print("Searching for: ", char)
            # print("Searching on: ", current)
            # print(type(current))
            # print(current.children)

            if char == ".":
        
                # BFS search whenever there's a wildcard "." character
                queue = deque()

                for child in current.children:

                    queue.append(current.children[child])

                while queue:

                    child: TrieNode = queue.pop()

                    if self.search(word[i + 1:], child):

                        return True

                return False

            else:

                if char in current.children:

                    current = current.children[char]

                else:

                    return False

        return current.is_word
