class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        sliding_window = set()

        # Initialize the sliding window
        for i in range(0, min(k + 1, len(nums))):

            num = nums[i]

            if num in sliding_window:

                return True

            sliding_window.add(num)
            #print(sliding_window)
            
        for i in range(k + 1, len(nums)):

            num = nums[i]
            old_num = nums[i - (k + 1)]
            # print("i: ", i)
            # print("Old Num: ", old_num)
            sliding_window.remove(old_num)

            if num in sliding_window:

                return True

            sliding_window.add(num)
            #print(sliding_window)

        return False

