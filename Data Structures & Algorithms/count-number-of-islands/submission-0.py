class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
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

            if grid[i][j] == "1": # Island

                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i, j + 1)

                return 1
            
            else:

                return 0

        num_islands = 0

        for i in range(len(grid)):

            for j in range(len(grid[i])):

                num_islands += dfs(i, j)

        return num_islands