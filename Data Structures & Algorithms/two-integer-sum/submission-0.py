class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum_components = dict() # Store {k - num: index}

        for j in range(len(nums)):

            num = nums[j]

            if num in sum_components:

                i = sum_components[num]

                return [i,j]
            
            else:

                sum_components.update({target-num: j})

        return None