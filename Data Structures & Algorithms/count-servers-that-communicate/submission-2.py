class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        row_counts = [0] * ROWS
        col_counts = [0] * COLS
        count = 0

        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c]:

                    row_counts[r] += 1
                    col_counts[c] += 1

        for r in range(ROWS):

            for c in range(COLS):

                if grid[r][c] and max(row_counts[r], col_counts[c]) > 1:

                        count += 1

        return count