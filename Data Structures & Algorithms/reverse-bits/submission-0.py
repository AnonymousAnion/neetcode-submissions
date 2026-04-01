class Solution:
    def reverseBits(self, n: int) -> int:
        
        num = 1
        power = 31
        new_num = 0

        while num <= n:

            if num & n == num:

                new_num += 2**power

            num <<= 1
            power -= 1

        return new_num