class Solution:

    def arrangeCoins(self, n: int) -> int:
        
        l = 1
        r = n
        maximum_levels = 0

        while l <= r:

            m = (l + r) // 2
            total = int((m/2) * (m + 1))

            if total > n: # Requires more coins than we have

                r = m - 1

            else: # We have sufficient coins

                l = m + 1
                maximum_levels = max(maximum_levels, m)

        return maximum_levels