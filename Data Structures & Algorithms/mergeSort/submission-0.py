# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], s: int = 0, e: Optional[int] = None) -> List[Pair]:

        if e is None:

            e = len(pairs) - 1

        if e - s <= 0:

            return pairs

        m = (s + e) // 2

        # Merge Sort Left
        self.mergeSort(pairs, s, m)

        # Merge Sort Right
        self.mergeSort(pairs, m + 1, e)

        def merge(arr, s, m, e) -> None:

            # Left sorted in non-decreasing order
            # Right sorted in non-decreasing order
            # merge them within subarry
            left = arr[s: m + 1]
            right = arr[m + 1: e + 1]

            l = 0
            r = 0
            combined_index = s

            while l < len(left) and r < len(right):

                if left[l].key <= right[r].key:
                    
                    arr[combined_index] = left[l]
                    l += 1

                else:

                    arr[combined_index] = right[r]
                    r += 1

                combined_index += 1

            while l < len(left):

                arr[combined_index] = left[l]
                l += 1
                combined_index += 1

            while r < len(right):

                arr[combined_index] = right[r]
                r += 1
                combined_index += 1

        merge(pairs, s, m, e)

        return pairs