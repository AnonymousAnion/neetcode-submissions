class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1:

            return 0

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]

        for c in range(COLS - 2, -1, -1):

            if obstacleGrid[ROWS - 1][c] == 0:

                grid[ROWS - 1][c] = grid[ROWS - 1][c + 1]
            
            else:

                grid[ROWS - 1][c] = 0

        for r in range(ROWS - 2, -1, -1):

            if obstacleGrid[r][-1] == 0:

                grid[r][-1] = grid[r + 1][-1]

            else:

                grid[r][-1] = 0

        for r in range(ROWS - 2, -1, -1):

            for c in range(COLS - 2, -1, -1):

                if obstacleGrid[r][c] == 0:

                    grid[r][c] = grid[r + 1][c] + grid[r][c + 1]

                else:

                    grid[r][c] = 0

        return grid[0][0]