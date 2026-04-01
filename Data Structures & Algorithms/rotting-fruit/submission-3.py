from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:

            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        
        # BFS initialized with all rotten fruits at start
        queue = deque()
        fresh_count = 0
        minutes = 0

        for i in range(len(grid)):

            for j in range(len(grid[i])):

                if grid[i][j] == 2:

                    queue.append((i, j))

                elif grid[i][j] == 1:

                    fresh_count += 1

        # Row Major Directions
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        while queue and fresh_count > 0:

            for i in range(len(queue)):

                coords = queue.popleft()

                # Rot neighboring fresh oranges!
                for dr, dc in directions:

                    row = coords[0] + dr
                    col = coords[1] + dc

                    # Check if neighbor coordinates are valid
                    if min(row, col) < 0 or row >= ROWS or col >= COLS:

                        continue
                        
                    # Unvisited, valid, neighboring, fresh orange to rot
                    if grid[row][col] == 1:

                        neighbor_coords = (row, col)
                        grid[row][col] = 2
                        queue.append(neighbor_coords)
                        fresh_count -= 1

            minutes += 1

        return minutes if fresh_count == 0 else -1