class Solution:

    def manhattan_dist(self, p1: List[int], p2: List[int]) -> int:

        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()
        distances = defaultdict(list)
        
        for i in range(len(points)):

            p1 = points[i]

            for j in range(i + 1, len(points)):

                p2 = points[j]
                distances[(p1[0], p1[1])].append((self.manhattan_dist(p1, p2), (p2[0], p2[1])))
                distances[(p2[0], p2[1])].append((self.manhattan_dist(p1, p2), (p1[0], p1[1])))

        cost = 0
        src = (points[0][0], points[0][1])
        pq = [(0, src)]
        
        while pq:

            if len(visited) == len(points):

                break

            dist, src = heapq.heappop(pq)

            if src in visited:

                continue

            cost += dist
            visited.add(src)

            for dist, dst in distances[src]:

                if dst not in visited:

                    heapq.heappush(pq, (dist, dst))

        return cost