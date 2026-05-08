class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        min_col = 0
        max_col = len(matrix[0]) - 1
        min_row = 0
        max_row = len(matrix) - 1

        spiral = []

        while max_col >= min_col and max_row >= min_row:

            # Top Row
            for i in range(min_col, max_col + 1):

                spiral.append(matrix[min_row][i])

            min_row += 1

            if max_col < min_col or max_row < min_row:

                break
                
            # Right Column
            for i in range(min_row, max_row + 1):

                spiral.append(matrix[i][max_col])

            max_col -= 1

            if max_col < min_col or max_row < min_row:

                break

            # Bottom Row
            for i in range(max_col, min_col - 1, -1):

                spiral.append(matrix[max_row][i])

            max_row -= 1

            if max_col < min_col or max_row < min_row:

                break

            # Left Column
            for i in range(max_row, min_row - 1, -1):

                spiral.append(matrix[i][min_col])

            min_col += 1

            if max_col < min_col or max_row < min_row:

                break

        return spiral