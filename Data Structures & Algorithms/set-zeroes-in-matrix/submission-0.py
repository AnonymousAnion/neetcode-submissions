class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row_zeros = False

        for i in range(len(matrix[0])):

            if 0 == matrix[0][i]:

                first_row_zeros = True
                break
        
        for i in range(1, len(matrix)):

            for j in range(len(matrix[i])):

                if 0 == matrix[i][j]:

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):

            if 0 == matrix[i][0]:

                for j in range(len(matrix[i])):

                    matrix[i][j] = 0

        for j in range(0, len(matrix[0])):

            if 0 == matrix[0][j]:

                for i in range(1, len(matrix)):

                    matrix[i][j] = 0

        if first_row_zeros:

            for i in range(len(matrix[0])):

                matrix[0][i] = 0