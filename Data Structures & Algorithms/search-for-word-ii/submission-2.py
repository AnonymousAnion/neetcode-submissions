class TrieNode:

    def __init__(self, char: str = "/", word: str = "", children: Dict = None) -> None:

        self.char = char
        self.children = {}
        self.word = word

class Trie:

    def __init__(self) -> None:

        self.head = TrieNode()

    def add_word(self, word: str) -> None:

        current = self.head

        for i, char in enumerate(word):

            if char not in current.children:

                current.children.update({char: TrieNode(char)})

            current = current.children[char]

            if i == len(word) - 1:

                current.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # CONTNIUE HERE WITH A FULL TRACE THROUGH EVERY PART OF THE PROGRAM

        ROWS = len(board)
        COLS = len(board[0])

        present_words = set()
        
        # Form a Trie from words
        trie = Trie()

        for word in words:

            trie.add_word(word)

        visited = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(node: TrieNode, cell: (int, int)) -> None:

            nonlocal visited

            visited.add((cell[0], cell[1]))

            nonlocal board
            nonlocal present_words

            row = cell[0]
            col = cell[1]

            char = board[row][col]

            if char in node.children:

                next_node = node.children[char]

                if next_node.word:

                    present_words.add(next_node.word)

                for d in dirs:

                    r = row + d[0]
                    c = col + d[1]

                    if min(r, c) >= 0 and r < ROWS and c < COLS: # valid Node

                        new_cell = (r, c)

                        if new_cell not in visited:
                        
                            dfs(next_node, new_cell)

            visited.remove((cell[0], cell[1]))



        # Loop through each cell and attempt
        # to form words out of neighbors in a DFS manner
        # at each one.
        for i in range(ROWS):

            for j in range(COLS):

                cell = (i, j)

                dfs(trie.head, cell)

        return list(present_words)