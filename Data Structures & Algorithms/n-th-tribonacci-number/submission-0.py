class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:

            return 0

        elif n < 3:

            return 1
        
        t = [0 for _ in range(n + 1)]

        t[1] = 1
        t[2] = 1

        for i in range(3, n + 1):

            t[i] = t[i - 3] + t[i - 2] + t[i - 1]

        return t[-1]