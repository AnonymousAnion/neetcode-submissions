class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # O(nlog(n))

        # Remove Duplicates
        # l = 1
        # prev_num = nums[0]

        # for i, num in enumerate(nums, start = 1)

        #     if num != prev_num:

        #         nums[l] = num
        #         l += 1

        #     prev_num = num

        triplets = []

        #print("Sorted Array: ")
        #print(nums)

        def find_pair_sum(target_index: int = 0, l: int = 0, r: int = len(nums) - 1):

            if 0 == l:

                l = target_index + 1

            target = -nums[target_index]

            #print("Searching for {0} in range [{1}, {2}]".format(target, l, r))

            while l < r:

                #print("{0}, {1} with values {2} and {3}".format(l, r, nums[l], nums[r]))
                if nums[l] + nums[r] == target:

                    #print("Matching pair found!")

                    triplets.append([nums[target_index], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while 0 <= l < len(nums) and nums[l] == nums[l - 1]:

                        l += 1

                    while 0 <= r < len(nums) and nums[r] == nums[r + 1]:

                        r -= 1

                elif nums[l] + nums[r] < target:

                    #print("Less")

                    l += 1

                elif nums[l] + nums[r] > target:

                    #print("More")

                    r -= 1

        prev_num = -10**6

        for i in range(len(nums)):

            if nums[i] == prev_num:

                continue

            if nums[i] <= 0:

                find_pair_sum(i)

            prev_num = nums[i]

        return triplets

