class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1
        majority_element = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num == majority_element:

                count += 1

            else:

                if 0 == count:

                    count = 1
                    majority_element = num

                else:

                    count -= 1

        return majority_element