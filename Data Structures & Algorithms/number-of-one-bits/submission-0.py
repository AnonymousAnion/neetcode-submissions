class Solution:
    def hammingWeight(self, n: int) -> int:
        
        num = 1
        ones = 0

        while num <= n:

            if num & n == num:

                ones += 1

            num <<= 1

        return ones