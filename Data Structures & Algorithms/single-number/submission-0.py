class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        current_num = 0
        
        for num in nums:

            current_num ^= num

        return current_num