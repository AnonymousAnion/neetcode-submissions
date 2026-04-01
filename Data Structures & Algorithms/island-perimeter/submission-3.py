from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid:

            return 0

        perimeter = 0  
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        def bfs():

            nonlocal queue
            nonlocal visited
            nonlocal directions
            nonlocal perimeter
            nonlocal ROWS
            nonlocal COLS

            while queue:

                current_tile = queue.popleft()
                row, col = current_tile

                if grid[row][col] == 1:

                    for direction in directions:

                        r = direction[0] + row
                        c = direction[1] + col

                        if min(r, c) < 0 or r >= ROWS or c >= COLS:

                            perimeter += 1

                        elif grid[r][c] == 0:

                            perimeter += 1

                        else:

                            coords = (r,c)

                            if coords not in visited:

                                queue.append(coords)
                                visited.add(coords)

        for i in range(ROWS):

            for j in range(COLS):

                coordinates = (i, j)

                if coordinates not in visited and grid[i][j] == 1:

                    queue.append(coordinates)
                    visited.add(coordinates)
                    bfs()
                    break

        return perimeter