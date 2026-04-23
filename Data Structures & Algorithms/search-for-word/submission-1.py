class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Backtracking DFS from any cell that matches the
        # starting letter of the word
        visited = set()

        def dfs(cell: (int, int), index: int) -> bool:

            visited.add(cell)

            # print("Current Cell: ", cell)
            # print("visited: ", visited)

            for d in dirs:

                r = cell[0] + d[0]
                c = cell[1] + d[1]

                if min(r, c) >= 0 and r < ROWS and c < COLS: # Valid cell

                    new_cell = (r, c)

                    if board[r][c] == word[index] and new_cell not in visited:

                        # print("Matching Letter: ", board[r][c])
                        # print("of word index: ", index)

                        if index + 1 == len(word):

                            return True

                        if dfs(new_cell, index + 1):

                            return True

            visited.remove(cell)
            return False

        for i in range(ROWS):

            for j in range(COLS):

                if board[i][j] == word[0]:

                    if len(word) == 1: return True

                    cell = (i, j)
                    #print("Starting DFS from ", cell)
                    if dfs(cell, 1):

                        return True

        return False