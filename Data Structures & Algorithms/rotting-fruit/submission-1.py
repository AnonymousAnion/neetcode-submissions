from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:

            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        
        # BFS initialized with all rotten fruits at start
        visited = set()
        queue = deque()
        fresh_count = 0

        for i in range(len(grid)):

            for j in range(len(grid[i])):

                if grid[i][j] == 2:

                    queue.append(((i, j), 0))

                elif grid[i][j] == 1:

                    fresh_count += 1

        if fresh_count == 0:

            return 0

        # Row Major Directions
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        while queue:

            coords, minute = queue.popleft()

            if grid[coords[0]][coords[1]] == 1:

                fresh_count -= 1

            if fresh_count <= 0:

                return minute

            for direction in directions:

                row = coords[0] + direction[0]
                col = coords[1] + direction[1]

                # Check if the neighbor is valid
                if min(row, col) < 0 or row >= ROWS or col >= COLS:

                    continue

                neighbor_coords = (row, col)

                # Unvisited fresh orange to rot
                if neighbor_coords not in visited and grid[row][col] == 1:

                    queue.append((neighbor_coords, minute + 1))
                    visited.add(neighbor_coords)

        # Queue Empty
        # Fresh fruits remain
        return -1