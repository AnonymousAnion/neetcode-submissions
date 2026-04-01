class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums) # original array length
        nums.extend(nums)
    
        #print(nums)

        max_sum = nums[0]
        current_sum = 0
        max_l = 0
        max_r = 0
        l = 0

        for i, num in enumerate(nums):

            r = i

            #print("OG L and R: [{0}, {1}]".format(l, r))

            if current_sum < 0:

                l = i
                current_sum = 0

            if r - l >= n:

                current_sum -= nums[l]
                l += 1

                while nums[l] < 0:

                    current_sum -= nums[l]
                    l += 1

            current_sum += num

            #print("[{0}, {1}]: {2}".format(l, r, current_sum))

            if current_sum > max_sum:

                max_sum = current_sum
                max_l = l
                max_r = r

        # print("Max Sum: ", max_sum)
        # print("Max L: ", max_l)
        # print("Max R: ", max_r)

        return max_sum