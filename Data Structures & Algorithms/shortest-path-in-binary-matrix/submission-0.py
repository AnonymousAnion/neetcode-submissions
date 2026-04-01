from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid:

            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        if grid[0][0] == 0:

            queue.append(((0, 0), 1))

        # Row-Major Directions
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        visited = set() # tracks visited coordinates

        while queue:

            coords, dist = queue.popleft()

            if coords == (ROWS - 1, COLS - 1):

                return dist

            else:

                for direction in directions:

                    row = coords[0] + direction[0]
                    col = coords[1] + direction[1]

                    if min(row, col) < 0 or row >= ROWS or col >= COLS:

                        continue

                    neighbor_coords = (row, col)

                    if neighbor_coords not in visited and grid[row][col] == 0:

                        queue.append((neighbor_coords, dist + 1))
                        visited.add(neighbor_coords)

        return -1