class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])
        
        watershed_overlap = []

        atlantic_watershed = set()
        pacific_watershed = set()

        # Multisource BFS for each Ocean starting from the land that borders them.
        # Each land bordering spreads to land that is higher than it.
        # This set of land represents the respective ocean's watershed.
        def multi_bfs(queue, watershed) -> None:

            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:

                row, col = queue.popleft()

                for d in dirs:

                    r = row + d[0]
                    c = col + d[1]

                    if min(r, c) >= 0 and r < ROWS and c < COLS: # valid cell

                        cell = (r, c)

                        if heights[row][col] <= heights[r][c] and cell not in watershed:

                            queue.append(cell)
                            watershed.add(cell)
                
        # Atlantic watershed
        queue = deque()

        for j in range(COLS):

            cell = (ROWS - 1, j)
            atlantic_watershed.add(cell)
            queue.append(cell)

        for i in range(ROWS):

            cell = (i, COLS - 1)
            atlantic_watershed.add(cell)
            queue.append(cell)

        multi_bfs(queue, atlantic_watershed)

        # print(atlantic_watershed)
        # print(len(atlantic_watershed))

        # Pacific Watershed
        queue = deque()

        for j in range(COLS):

            cell = (0, j)
            pacific_watershed.add(cell)
            queue.append(cell)

        for i in range(ROWS):

            cell = (i, 0)
            pacific_watershed.add(cell)
            queue.append(cell)

        multi_bfs(queue, pacific_watershed)

        # print(pacific_watershed)
        # print(len(pacific_watershed))

        for r in range(ROWS):

            for c in range(COLS):

                cell = (r, c)

                if cell in atlantic_watershed and cell in pacific_watershed:

                    watershed_overlap.append([r,c])

        return watershed_overlap