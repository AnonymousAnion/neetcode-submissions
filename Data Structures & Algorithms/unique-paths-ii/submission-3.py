class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1:

            return 0

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        prev_row = [1] * COLS

        for c in range(COLS - 2, -1, -1):

            if obstacleGrid[ROWS - 1][c] == 0:

                prev_row[c] = prev_row[c + 1]
            
            else:

                prev_row[c] = 0

        for r in range(ROWS - 2, -1, -1):

            row = [1] * COLS

            if obstacleGrid[r][-1] == 1:

                row[-1] = 0

            else:

                row[-1] = prev_row[-1]

            for c in range(COLS - 2, -1, -1):

                if obstacleGrid[r][c] == 0:

                    row[c] = prev_row[c] + row[c + 1]

                else:

                    row[c] = 0

            prev_row = row

        return prev_row[0]