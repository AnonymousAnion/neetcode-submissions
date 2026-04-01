class Solution:
    def mySqrt(self, x: int) -> int:
        

        l = 0
        r = x

        while l <= r:

            m = l + (r - l) // 2

            if x > m * m:

                l = m + 1

            elif x < m * m:

                r = m - 1

            else:

                return m

        return l-1