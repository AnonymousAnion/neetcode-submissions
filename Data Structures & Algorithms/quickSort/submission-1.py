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

            pivot = pairs[e]
            l = s

            for i in range(s, e):

                if pairs[i].key < pivot.key:

                    # Swap pairs[i] and pairs[l]
                    tmp =  pairs[i]
                    pairs[i] = pairs[l]
                    pairs[l] = tmp

                    l += 1

            # left is the min index of elements
            # greater than or equal to the pivot.
            # Therefore, we swap the pivot to this
            # position to have all elements located
            # at less than this position less than the
            # pivot and all elements located at greater
            # than this position greater than or equal
            # to the pivot.
            pairs[e] = pairs[l]
            pairs[l] = pivot

            # Sort left
            qs(s, l - 1)

            # Sort right
            qs(l + 1, e)

        qs(0, len(pairs) - 1)

        return pairs

