class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def num_missing(length: int, maximum: int, minimum: int) -> int:

            return maximum - minimum - length + 1

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2
            left_len = m + 1
            right_len = r - m + 1
            left_missing = num_missing(left_len, nums[m], nums[0])
            right_missing = num_missing(right_len, nums[r], nums[m])

            print("l: ", l)
            print("r: ", r)
            print("m: ", m)
            print("left len: ", left_len)
            print("right len: ", right_len)
            print("left missing: ", left_missing)
            print("right missing: ", right_missing)

            if left_missing < k:

                l = m + 1

            else:

                r = m - 1
    
        num_missing = num_missing(r + 1, nums[r], nums[0])
        print("Before Missing: ", num_missing)

        return nums[r] + (k - num_missing)