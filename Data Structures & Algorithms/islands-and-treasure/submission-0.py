class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        LAND = 2147483647
        WATER = -1
        TREASURE = 0

        # Multi-Source BFS from treasure chests
        queue = deque()
        visited = set()

        for i in range(ROWS):

            for j in range(COLS):

                if TREASURE == grid[i][j]:

                    visited.add((i, j))
                    queue.append((i, j, 0))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:

            i, j, dist = queue.popleft()

            for d in dirs:

                r = i + d[0]
                c = j + d[1]

                if min(r, c) >= 0 and r < ROWS and c < COLS:

                    if LAND == grid[r][c] and (r, c) not in visited:

                        visited.add((r, c))
                        new_dist = dist + 1
                        queue.append((r, c, new_dist))
                        grid[r][c] = new_dist