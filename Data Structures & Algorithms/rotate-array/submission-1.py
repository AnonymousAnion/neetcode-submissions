import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        ALLOWED_MOVES = len(nums) if (len(nums) % 2 == 1) else len(nums) // math.gcd(k, len(nums))
        initial_indices = [0]

        if len(nums) % 2 == 0:

            initial_indices = list(range(0, math.gcd(k, len(nums)), 1))

        print("Initial Indices: ")
        print(initial_indices)

        for index in initial_indices:

            moves = 0
            prev_index = 0
            temp = nums[index]
            prev_temp = 0

            while moves < ALLOWED_MOVES:

                new_index = (index + k) % len(nums)

                temp = nums[new_index]

                print("Index: ", index)
                print("New Index: ", new_index)
                print("Temp: ", temp)

                nums[new_index] = nums[index] if moves < 1 else prev_temp
                prev_temp = temp
                prev_index = index
                index = new_index

                # print(nums)
                # print("Prev Temp: ", prev_temp)

                moves += 1