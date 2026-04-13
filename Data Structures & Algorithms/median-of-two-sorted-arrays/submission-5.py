class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        big, small = nums1, nums2

        if len(nums2) > len(nums1):

            big, small = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(small) - 1

        while True:

            m = l + (r - l) // 2
            j = half - 2 - m

            small_left = small[m] if m >= 0 else float("-infinity")
            small_right = small[m + 1] if m + 1 < len(small) else float("infinity")
            big_left = big[j] if j >= 0 else float("-infinity")
            big_right = big[j + 1] if j + 1 < len(big) else float("infinity")

            if small_left <= big_right and big_left <= small_right:

                if total % 2:

                    return min(small_right, big_right)

                else:

                    return (min(small_right, big_right) + max(small_left, big_left)) / 2

            elif small_left > big_right:

                r = m - 1

            else:

                l = m + 1
