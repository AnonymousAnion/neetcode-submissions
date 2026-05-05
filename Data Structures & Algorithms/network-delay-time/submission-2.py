class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        costs = defaultdict(list)

        for time in times:

            src, dst, cost = time

            costs[src].append((dst, cost))

        #print(costs)

        min_heap = [(0, k)]

        min_costs = dict()

        while min_heap:

            if len(min_costs) == n:

                break

            cost, dst = heapq.heappop(min_heap)

            if dst in min_costs:

                continue

            # print("Current Node: ", dst)
            # print("Cost: ", cost)

            if dst not in min_costs:

                min_costs.update({dst: cost})

            if dst in costs:

                for neighbor in costs[dst]:

                    #print(neighbor)
                    if neighbor[0] not in min_costs:

                        heapq.heappush(min_heap, (neighbor[1] + cost, neighbor[0]))

            #print("Updated min heap: ", min_heap)

        # print("Min Costs: ")
        # print(min_costs)

        if len(min_costs) < n:

            return -1

        required_time = float("-inf")

        for key in min_costs:

            #print(key)
            required_time = max(min_costs[key], required_time)

        return required_time