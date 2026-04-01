class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = 0
        current_max_sum = 0
        global_max = nums[0]
        current_min_sum = 0
        global_min = nums[0]

        for num in nums:

            current_max_sum = max(0, current_max_sum)
            current_min_sum = min(0, current_min_sum)

            current_max_sum += num
            current_min_sum += num

            # print("Max Sum: ", current_max_sum)
            # print("Min Sum: ", current_min_sum)

            total += num

            global_max = max(global_max, current_max_sum)
            global_min = min(global_min, current_min_sum)

            # print("Global Max Sum: ", global_max)
            # print("Global Min Sum: ", global_min)

        global_min = min(global_min, 0)

        # print("Total: ", total)
        # print("Total Minus Global Min: ", total - global_min)

        if global_max < 0:

            return global_max

        return max(total - global_min, global_max)