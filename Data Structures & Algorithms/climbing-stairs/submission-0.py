class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:

            return 1

        stairs = [0 for _ in range(n)]
        stairs[-1] = 1
        stairs[-2] = 2

        for i in range(n - 3, -1, -1):

            stairs[i] = stairs[i + 1] + stairs[i + 2]

        return stairs[0]


        