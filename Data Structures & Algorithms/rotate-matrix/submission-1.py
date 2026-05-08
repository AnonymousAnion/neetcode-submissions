class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        ROWS = COLS = len(matrix) - 1

        def quartet_swap(r: int, c: int) -> None:

            nonlocal matrix

            temp = matrix[r][c]
            matrix[r][c] = matrix[ROWS - c][r]
            matrix[ROWS - c][r] = matrix[ROWS - r][COLS - c]
            matrix[ROWS - r][COLS - c] = matrix[c][ROWS - r]
            matrix[c][ROWS - r] = temp

        for i in range((ROWS + 2) // 2):

            for j in range(i, COLS - i):

                quartet_swap(i, j)