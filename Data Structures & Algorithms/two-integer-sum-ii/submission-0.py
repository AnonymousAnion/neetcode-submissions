class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        summation = numbers[left] + numbers[right]

        while left != right and summation != target:

            if summation > target:

                right -= 1

            else:

                left += 1

            summation = numbers[left] + numbers[right]

            #print("({0},{1})".format(left, right))

        return [left + 1, right + 1]


        