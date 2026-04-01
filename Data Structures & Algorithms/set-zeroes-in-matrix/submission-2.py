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

        print(matrix)

        for i in range(1, len(matrix)):

            for j in range(len(matrix[i]) - 1, -1, -1):

                if 0 == matrix[0][j] or 0 == matrix[i][0]:

                    matrix[i][j] = 0

        print(matrix)

        if first_row_zeros:

            for i in range(len(matrix[0])):

                matrix[0][i] = 0