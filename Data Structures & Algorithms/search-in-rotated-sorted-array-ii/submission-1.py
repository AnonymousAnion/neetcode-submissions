class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2

            if nums[m] == nums[l] == nums[r] and nums[m] != target:

                l += 1
                r -= 1
                continue

            if nums[m] < target:

                if nums[m] >= nums[l]: # Ascending from l to m

                    l = m + 1 

                else: # Ascending from m to r

                    if nums[r] < target:

                        r = m - 1
                    
                    else:

                        l = m + 1

            elif nums[m] > target:

                if nums[m] >= nums[l]: # Ascending from l to m

                    if target < nums[l]:

                        l = m + 1

                    else:

                        r = m - 1

                else: # Ascending from m to r

                    r = m - 1

            else:

                return True

        return False