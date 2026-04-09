class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # comb = nums1 + nums2
        # comb.sort()
        # print("Combined array for debugging: ", comb)
        # print("Length: ", len(comb))
        # med = comb[len(comb) // 2]
        # if len(comb) % 2 == 0: med = (comb[len(comb) // 2] + comb[(len(comb) // 2) + 1]) / 2
        # print("Median: ", med)
        
        # Do a sort of two pronged binary search
        # Find the median of each array and then take a weighted average?
        # The median of a sorted array is the middle value if there are an odd
        # number of elements or the average of the two middle values if there
        # are an even number of elements.

        # Compare medians. Min median becomes min of range while the max median becomes
        # the max of the range - therefore, we can eliminate half the work!
        # At each step we recalculate the new medians and repeat!
        # Base case is when an array has shrunk down to a single element.

        def sorted_median(s: int, e: int, arr: List[int]) -> float:

            if not arr:

                return 0

            m = s + (e - s) // 2

            if (e - s) % 2 == 1: # Even length array

                return m, (arr[m] + arr[m + 1]) / 2

            else:

                return m, arr[m]

        def median(arr: List[int], s: int = 0, e: int = None) -> float:

            if not arr:

                return 0.0

            if not e:

                e = len(arr) - 1

            m = s + (e - s) // 2

            if (e - s) % 2 == 1: # Even length array

                return (arr[m] + arr[m + 1]) / 2

            else:

                return arr[m]

        s1 = 0
        e1 = len(nums1) - 1
        s2 = 0
        e2 = len(nums2) - 1

        if not nums1 and not nums2:

            return 0

        elif not nums1:

            return median(nums2)

        elif not nums2:

            return median(nums1)

        while e1 - s1 > 0 and e2 - s2 > 0:

            m1, med1 = sorted_median(s1, e1, nums1)
            m2, med2 = sorted_median(s2, e2, nums2)

            # print("Nums 1:")
            # print(nums1[s1:e1 + 1])
            # print("m1: ", m1)
            # print("median 1: ", med1)

            # print("Nums 2:")
            # print(nums2[s2:e2 + 1])
            # print("m2: ", m2)
            # print("median 2: ", med2)

            if med2 > med1:

                #print("med2 > med1")

                chop = max(1, min(e2 - m2, m1 - s1))
                e2 -= chop
                s1 += chop

            else:

                #print("med1 >= med2")

                chop = max(1, min(e1 - m1, m2 - s2))
                e1 -= chop
                s2 += chop

        # print("Nums 1:")
        # print(nums1[s1:e1 + 1])

        # print("Nums 2:")
        # print(nums2[s2:e2 + 1])

        def median_after_insertion(arr, start, end, new_val) -> float:

            length = end - start + 2
            og_m, og_med = sorted_median(start, end, arr)

            # print("og_m: ", og_m)
            # print("og_med: ", og_med)
            # print("length: ", length)

            if length % 2 == 1: # Odd

                if new_val > og_med:

                    # median shifts 1 to the right
                    if og_m + 1 > end or new_val < arr[og_m + 1]:

                        return new_val

                    return arr[og_m + 1]

                elif new_val < og_med:

                    # median shifts 1 to the left
                    if new_val > arr[og_m]:

                        return new_val

                    return arr[og_m]

                else:

                    return og_med

            else:

                if new_val > og_med:

                    # median shifts 1 to the right
                    if og_m + 1 > end or new_val < arr[og_m + 1]:

                        return (new_val + og_med) / 2

                    return (arr[og_m + 1] + og_med) / 2

                elif new_val < og_med:

                    # median shifts 1 to the left
                    if og_m - 1 < s1 or new_val > arr[og_m - 1]:

                        return (new_val + og_med) / 2

                    return (arr[og_m - 1] + og_med) / 2

                else:

                    return og_med

        # binary insert whichever one is length one into the other
        # then take the median
        if e2 - s2 == 0 and e1 - s1 == 0:

            return (nums1[s1] + nums2[s2]) / 2

        elif e2 - s2 == 0: # Insert last nums2 value into nums1 which is of length >= 2

            return median_after_insertion(nums1, s1, e1, nums2[s2])

        else: # Insert last nums1 value into nums2 which is of length >= 2

            return median_after_insertion(nums2, s2, e2, nums1[s1])