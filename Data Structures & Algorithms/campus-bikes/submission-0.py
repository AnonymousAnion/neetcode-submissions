class Solution:

    def manhattan_dist(self, x1: int, y1: int, x2: int, y2: int) -> int:

        return abs(x2 - x1) + abs(y2 - y1)

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        triplets = []

        for worker, worker_loc in enumerate(workers):

            wx, wy = worker_loc

            for bike, bike_loc in enumerate(bikes):

                bx, by = bike_loc

                distance = self.manhattan_dist(wx, wy, bx, by)
                triplets.append((distance, worker, bike))

        triplets.sort()

        bike_status = [False] * len(bikes)

        worker_status = [-1] * len(workers)

        pair_count = 0

        for distance, worker, bike in triplets:

            if worker_status[worker] == -1 and not bike_status[bike]:

                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1

                if pair_count == len(workers):

                    return worker_status

        return worker_status