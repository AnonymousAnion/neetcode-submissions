class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freqs = Counter(nums)
        frequent_nums = []

        for val, freq in freqs.items():

            if freq > len(nums) // 3:

                frequent_nums.append(val)

        return frequent_nums