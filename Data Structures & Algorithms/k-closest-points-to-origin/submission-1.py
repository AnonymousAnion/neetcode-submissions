import heapq

class Solution:

    def euclidean_distance(self, x1: float, y1: float, x2: float = 0.0, y2: float = 0.0) -> float:

        return (x1 - x2)**2 + (y1 - y2)**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Min heap organized by distance
        min_heap = []

        for point in points:

            heapq.heappush(min_heap, (self.euclidean_distance(point[0], point[1]), point))

        k_closest = []

        for val in heapq.nsmallest(k, min_heap):

            k_closest.append(val[1])

        return k_closest