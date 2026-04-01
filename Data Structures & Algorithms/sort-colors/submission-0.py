class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Bucketing Technique: In one pass
        # store the frequency of each number
        freqs = Counter(nums)
        MIN_NUM = 0
        MAX_NUM = 2
        count = 0

        for i in range(MIN_NUM, MAX_NUM + 1):

            freq = freqs[i]

            for j in range(0, freq):

                nums[count] = i
                count += 1

        return nums