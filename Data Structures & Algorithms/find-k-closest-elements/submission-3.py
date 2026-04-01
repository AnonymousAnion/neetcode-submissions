class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # Binary search to find where x would go. O(log(n))
        def binary_search(l = 0, r = len(arr) - 1, target = x):

            while l <= r:

                m = l + (r - l) // 2

                if target > arr[m]:

                    l = m + 1

                elif target < arr[m]:

                    r = m -1

                else:

                    return m

            return r + 1

        x_index = binary_search()

        if x_index == 0:

            return arr[:k]

        elif x_index == len(arr):

            return arr[len(arr) - k:]

        # Expanding window around x within the sorted array
        # from 0 to k, decide whether to expand left or expand
        # right. O(n)
        l = x_index
        r = x_index
        while k > 0:

            if r < len(arr):

                if l > 0:

                    if abs(arr[l - 1] - x) <= abs(arr[r] - x):

                        l -= 1

                    else:

                        r += 1
                
                else:

                    r += 1

            else:

                if l >= 0:

                    l -= 1

            k -= 1

        return arr[l:r]