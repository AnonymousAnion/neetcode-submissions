class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        transposition = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix[0])):

            for j in range(len(matrix)):

                transposition[i][j] = matrix[j][i]

        return transposition