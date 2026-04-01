class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_data = sorted(zip(position, speed))

        #print(sorted_data)

        expected_arrivals = []
        
        for pos, vel in sorted_data:

            expected_arrivals.append((target - pos) / vel)

        # print("Expected Arrivals: ")
        # print(expected_arrivals)

        fastest_arrival: int = 0
        car_fleets: int = 0

        for i in range(len(expected_arrivals) - 1, -1, -1):

            eta = expected_arrivals[i]

            if eta > fastest_arrival:

                car_fleets += 1
                fastest_arrival = eta

        return car_fleets