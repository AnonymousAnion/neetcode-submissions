class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        pq = [(grid[0][0], (0, 0))]

        while pq:

            swim_time, cell = heapq.heappop(pq)

            if cell in visited:

                continue

            visited.add(cell)

            # print("Swim Time: ", swim_time)
            # print("Cell: ", cell)

            if cell == (ROWS - 1, COLS - 1):

                return swim_time

            # Add unvisited neighbors to Priority Queue
            for r, c in dirs:

                row = cell[0] + r
                col = cell[1] + c

                if min(row, col) >= 0 and row < ROWS and col < COLS:

                    neighbor = (row, col)

                    if neighbor not in visited:

                        cost = max(grid[row][col], swim_time)
                        heapq.heappush(pq, (cost, neighbor))

        return -1 # This should not occur