class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        costs = defaultdict(list)

        for src, dst, cost in times:

            costs[src].append((dst, cost))

        min_heap = [(0, k)]
        required_time = float("-inf")
        visited = set()

        while min_heap:

            if len(visited) == n:

                break

            cost, dst = heapq.heappop(min_heap)

            if dst in visited:

                continue

            visited.add(dst)
            required_time = max(required_time, cost)

            if dst in costs:

                for neighbor in costs[dst]:

                    if neighbor[0] not in visited:

                        heapq.heappush(min_heap, (neighbor[1] + cost, neighbor[0]))

        if len(visited) < n:

            return -1

        return required_time