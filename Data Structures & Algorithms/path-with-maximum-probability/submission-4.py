class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        probabilities: Dict[int, List[Tuple[int, float]]] = dict()
        visited = set()

        for i in range(len(edges)):

            edge = edges[i]
            prob = succProb[i]

            if edge[0] not in probabilities:

                probabilities.update({edge[0]: [(edge[1], prob)]})

            else:

                probabilities[edge[0]].append((edge[1], prob))

            if edge[1] not in probabilities:

                probabilities.update({edge[1]: [(edge[0], prob)]})

            else:

                probabilities[edge[1]].append((edge[0], prob))

        priority_queue = [(1.0, start_node)]

        while priority_queue:

            probability, node = heapq.heappop_max(priority_queue)

            if node in visited:

                continue

            visited.add(node)

            if node == end_node:

                return probability

            if node in probabilities:

                for neighbor in probabilities[node]:

                    if neighbor not in visited:

                        heapq.heappush_max(priority_queue, (probability * neighbor[1], neighbor[0]))
        
        return 0
        