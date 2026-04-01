class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # O(nlog(n))
        triplets: List[List[int]] = []

        prev_a = -10**6

        for i, a in enumerate(nums):

            if a == prev_a:

                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:

                    r -= 1

                elif three_sum == 0:

                    triplets.append([a, nums[l], nums[r]])

                    r -= 1
                    l += 1

                    while l < len(nums) and nums[l] == nums[l - 1]:

                        l += 1

                    while r >= 0 and nums[r] == nums[r + 1]:

                        r -= 1

                else:

                    l += 1

            prev_a = a

        return triplets