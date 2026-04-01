class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # since our algo will have runtime greater than
        # O(nlog(n)), this will simplify ignoring duplicate
        # values.
        nums.sort()
        res, k_group = [], []

        def kSum(k, start, target) -> None:

            if k > 2:

                for i in range(start, len(nums) - k + 1):

                    # Ignore duplicate values
                    if i > start and nums[i] == nums[i - 1]:

                        continue

                    k_group.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])

                    # Remove the previous k_group search
                    # when starting a new one
                    k_group.pop()

            elif 2 == k:

                # Two Sum II
                l = start
                r = len(nums) - 1

                while l < r:

                    if nums[l] + nums[r] > target:

                        r -= 1

                    elif nums[l] + nums[r] < target:

                        l += 1

                    else:

                        res.append(k_group + [nums[l], nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l - 1]:

                            l += 1
            elif 1 == k:

                for i, num in enumerate(nums):

                    if i > 0 and nums[i] == nums[i - 1]:

                        continue

                    if num == target:

                        res.append(num)

            else:

                raise ValueError("Invalid k sum value: {0}".format(k))

        kSum(4, 0, target)

        return res

            