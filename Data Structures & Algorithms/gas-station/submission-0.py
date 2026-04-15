class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if not gas or not cost:

            return -1

        tank = []

        for i in range(len(gas)):

            tank.append(gas[i] - cost[i])

        if sum(tank) < 0:

            return -1

        print("Tank: ", tank)
        print("sum: ", sum(tank))

        max_index = len(tank) - 1
        max_tank = 0
        current_tank = 0

        for i in range(len(tank) - 1, -1, -1):

            current_tank = max(tank[i], tank[i] + current_tank)
            #print("Current Tank: ", current_tank)

            if current_tank > max_tank:

                max_tank = current_tank
                max_index = i

        for i in range(len(tank) - 1, -1, -1):

            current_tank = max(tank[i], tank[i] + current_tank)
            #print("Current Tank: ", current_tank)

            if current_tank > max_tank:

                max_tank = current_tank
                max_index = i

        return max_index