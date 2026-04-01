class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) > 1:

            # print("OG Array")
            # print(nums)
            # print("Halves: ")
            # print(nums[:len(nums)//2])
            # print(nums[len(nums)//2:])

            arr1 = self.sortArray(nums[:len(nums)//2])
            arr2 = self.sortArray(nums[len(nums)//2:])

            combined = []

            r = 0

            for num in arr1:

                while r < len(arr2) and num >= arr2[r]:

                    combined.append(arr2[r])
                    r += 1
                    
                combined.append(num)

            for i in range(r, len(arr2)):

                combined.append(arr2[i])

            return combined

        else:

            # print(nums)

            return nums        