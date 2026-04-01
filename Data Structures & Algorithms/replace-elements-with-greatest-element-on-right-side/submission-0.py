class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatest_value = -1

        for i in range(len(arr) - 1, -1, -1):

            val = arr[i]
            arr[i] = greatest_value
            greatest_value = max(greatest_value, val)

        return arr