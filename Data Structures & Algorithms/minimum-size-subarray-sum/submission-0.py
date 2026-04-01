class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:

            return 0

        l = 0
        min_length = len(nums)
        current_sum = 0

        for r in range(0, len(nums)):

            #print("R: ", r)

            current_sum += nums[r]

            #print("Current Sum: ", current_sum)

            while current_sum >= target:

                min_length = min(min_length, (r - l) + 1)
                current_sum -= nums[l]
                l += 1

                # print("Min Length: ", min_length)
                # print("L: ", l)
                # print("[{0}, {1}] Current Sum: {2}".format(l, r, current_sum))

        return min_length