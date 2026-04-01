class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        combo_index = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:

            if nums1[m] > nums2[n]:

                nums1[combo_index] = nums1[m]
                m -= 1

            else:

                nums1[combo_index] = nums2[n]
                n -= 1

            combo_index -= 1

        # Only need to worry about left overs for the
        # 2nd array. Any elements in nums1 less than
        # all elements in nums2 will already be in the
        # correct position!
        while n >= 0:

            nums1[combo_index] = nums2[n]
            n -= 1
            combo_index -= 1