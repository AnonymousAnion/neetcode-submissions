class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.prefix_sums = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)]

        for i in range(1, len(self.prefix_sums)):

            prefix_sum = 0

            for j in range(1, len(self.prefix_sums[i])):

                prefix_sum += matrix[i-1][j-1]
                self.prefix_sums[i][j] = prefix_sum + self.prefix_sums[i - 1][j]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        upper_left = self.prefix_sums[row1][col1]
        col_band = self.prefix_sums[row2 + 1][col1]
        row_band = self.prefix_sums[row1][col2 + 1]
        grid_total = self.prefix_sums[row2 + 1][col2 + 1]

        return grid_total - row_band - col_band + upper_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)