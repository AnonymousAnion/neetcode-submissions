class Solution:
    def countBits(self, n: int) -> List[int]:
        
        bit_count = [0 for _ in range(n + 1)]
        two_pow = 1

        for i in range(1, n + 1):

            if i == two_pow:

                bit_count[i] = 1
                two_pow *= 2

            else:

                bit_count[i] = bit_count[i^(two_pow//2)] + 1

        return bit_count
