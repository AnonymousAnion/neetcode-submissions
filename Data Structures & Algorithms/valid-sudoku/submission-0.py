class Solution:

    def isValidSudokuNumber(self, s: str) -> bool:

        if s.isdigit() and 1 <= int(s) <= 9:

            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #print("Check Rows!")
        # Check Rows
        for i in range(0, len(board)):

            row = set()

            for j in range(0, len(board[i])):

                if not self.isValidSudokuNumber(board[i][j]):

                    continue

                val = int(board[i][j])

                #print("({0},{1}): {2})".format(i, j, val))

                if val in row:

                    return False

                else:

                    row.add(val)

        #print("Check Columns!")

        # Check Columns
        for j in range(0, len(board[0])):

            col = set()

            for i in range(0, len(board)):

                if not self.isValidSudokuNumber(board[i][j]):

                    continue

                val = board[i][j]

                #print("({0},{1}): {2})".format(i, j, val))

                if val in col:

                    return False

                else:

                    col.add(val)

        #print("Check Boxes!")

        # Check Sub-Boxes
        SUDOKU_BOX_SIZE = 3
        for i in range(0, len(board), SUDOKU_BOX_SIZE):

            for j in range(0, len(board[i]), SUDOKU_BOX_SIZE):

                sub_box = set()

                # Sub-Box Start
                for row in range(0, SUDOKU_BOX_SIZE):

                    for col in range(0, SUDOKU_BOX_SIZE):

                        if not self.isValidSudokuNumber(board[i + row][j + col]):

                            continue

                        val = board[i + row][j + col]

                        #print("({0},{1}): {2})".format(i, j, val))

                        if val in sub_box:

                            return False

                        else:

                            sub_box.add(val)

        return True




