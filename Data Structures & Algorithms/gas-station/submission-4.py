class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if not gas or not cost or sum(gas) < sum(cost):

            return -1

        total = 0
        earliest_net_contributor = 0

        # Leveraging the fact that we know there's a solution,
        # we search for the earliest net contributor
        for i in range(len(gas)):

            total += (gas[i] - cost[i])

            if total < 0:

                total = 0
                earliest_net_contributor = i + 1

        return earliest_net_contributor