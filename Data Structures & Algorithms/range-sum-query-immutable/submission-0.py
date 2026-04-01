class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix_sums = []
        current_sum = 0

        for i in range(0, len(nums)):

            current_sum += nums[i]
            self.prefix_sums.append(current_sum)
        

    def sumRange(self, left: int, right: int) -> int:

        left_prefix_sum = 0

        if left > 0:

            left_prefix_sum = self.prefix_sums[left - 1]
        
        return self.prefix_sums[right] - left_prefix_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)