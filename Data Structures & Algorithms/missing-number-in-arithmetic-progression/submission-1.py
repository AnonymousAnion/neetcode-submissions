class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        # Could find missing index in O(n)
        # missing number is simply 
        # diff = last (max) - first (min) // (last_index + 1)
        # Binary search for the index where insertion would create that diff
        # Value at index i should be first + diff * i. If it's less than or equal
        # we increase search index (less shouldn't occur). It it's greater then
        # we decrease search index.

        diff = (arr[-1] - arr[0]) // (len(arr))

        l = 1
        r = len(arr) - 1
        minimum_ordered_index = 0

        while l <= r:

            m = (l + r) // 2
            expected_val = arr[0] + diff * m

            if diff > 0: # Ascending

                if arr[m] <= expected_val:

                    l = m + 1

                elif arr[m] > expected_val:

                    r = m - 1

            else: # Descending

                if arr[m] >= expected_val:

                    l = m + 1

                elif arr[m] < expected_val:

                    r = m - 1


        return arr[r] + diff