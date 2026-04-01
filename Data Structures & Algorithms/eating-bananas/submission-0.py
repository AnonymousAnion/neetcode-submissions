import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = max(piles)
        required_rate = max_pile

        if h == len(piles):

            return required_rate

        l = 1
        r = max_pile

        while l <= r:

            k = l + (r -l) // 2

            total_hours = 0

            for pile in piles:

                total_hours += math.ceil(pile / k)

            #print("Required hours for eating rate of {0}: {1}".format(k, total_hours))

            if total_hours > h:

                l = k + 1

            else:

                r = k - 1
                required_rate = min(required_rate, k)
            
        return required_rate

