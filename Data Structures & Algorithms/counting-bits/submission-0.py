class Solution:
    def countBits(self, n: int) -> List[int]:
        
        bit_count = [0 for _ in range(n + 1)]
        two_pow = 1

        # print("Initial Bit Count: ")
        # print(bit_count)

        for i in range(1, n + 1):

            #print("i: ", i)

            if i == two_pow:

                bit_count[i] = 1
                two_pow *= 2

            else:

                #print("Non-power-of-two index: ", str(i^(two_pow//2)))
                bit_count[i] = bit_count[i^(two_pow//2)] + 1

            #print(bit_count)

        return bit_count
