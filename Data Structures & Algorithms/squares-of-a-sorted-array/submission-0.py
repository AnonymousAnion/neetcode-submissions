class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squares = [0 for _ in range(len(nums))]

        l = 0
        r = len(nums) - 1
        c = len(nums) - 1

        while l <= r and c >= 0:

            square_l = nums[l]**2
            square_r = nums[r]**2

            if square_l >= square_r:

                squares[c] = square_l
                l += 1

            else:

                squares[c] = square_r
                r -= 1

            c -= 1

        return squares