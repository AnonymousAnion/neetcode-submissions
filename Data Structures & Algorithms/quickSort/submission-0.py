# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def qs(s: int, e: int) -> None:

            if e - s <= 0: # single element subarray

                return

            pivot = pairs[e] # select last element as pivot
            left = s # pointer for left side

            # Partition: elements smaller than pivot on left side
            for i in range(s, e):

                if pairs[i].key < pivot.key:

                    tmp = pairs[left]
                    pairs[left] = pairs[i]
                    pairs[i] = tmp
                    left += 1

            # left will be the minimal index of values
            # greater than or equal to the pivot.
            # Move the pivot in-between left and right sides.
            # Definitionally all values to the right are
            # therefore greater than or equal to the pivot
            # while all values to the left are less than the
            # pivot. Therefore, we've accomplished, at minimum,
            # putting one element in its correct sorted location
            # in O(n) time.
            pairs[e] = pairs[left]
            pairs[left] = pivot

            # Quick sort left side
            # Left includes up to before the pivot
            # which is already in its sorted position
            qs(s, left - 1)

            # Quick sort right side
            qs(left + 1, e)

        qs(0, len(pairs) - 1)

        return pairs