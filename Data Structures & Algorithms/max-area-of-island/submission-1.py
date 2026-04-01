class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()

        def dfs(i: int, j: int) -> int:

            nonlocal visited
            nonlocal grid

            if min(i, j) < 0 or i >= len(grid) or j >= len(grid[i]):

                return 0

            coords = (i, j)

            if coords in visited:

                return 0

            visited.add(coords)

            if grid[i][j] == 1:

                area = 1

                area += dfs(i - 1, j)
                area += dfs(i, j - 1)
                area += dfs(i + 1, j)
                area += dfs(i, j + 1)

                return area

            else:

                return 0

        largest_island = 0

        for i in range(len(grid)):

            for j in range(len(grid[i])):

                largest_island = max(largest_island, dfs(i, j))

        return largest_island 