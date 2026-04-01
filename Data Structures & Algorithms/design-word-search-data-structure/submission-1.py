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

        def bfs(j: int, root: TrieNode):

            for i in range(j, len(word)):
            
                char = word[i]

                if char == ".":
            
                    # BFS search whenever there's a wildcard "." character
                    queue = deque()

                    for child in root.children:

                        queue.append(root.children[child])

                    while queue:

                        child: TrieNode = queue.pop()

                        if bfs(i + 1, child):

                            return True

                    return False

                else:

                    if char in root.children:

                        root = root.children[char]

                    else:

                        return False

            return root.is_word

        return bfs(0, self.head)
