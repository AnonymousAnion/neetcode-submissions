# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def swap(i1: int, i2: int) -> None:

            tmp = pairs[i1]
            pairs[i1] = pairs[i2]
            pairs[i2] = tmp

        def qs(s: int, e: int) -> None:

            if e - s <= 0:

                return

            pivot = pairs[e]
            l = s

            # All elements less than the pivot will
            # be to the left
            for i in range(s, e):

                if pairs[i].key < pivot.key:

                    swap(l, i)
                    l += 1

            # All elements greater than or equal to the
            # pivot will be to the right
            swap(l, e) 

            # Sort elements to the left
            qs(s, l - 1)

            # Sort elements to the right
            qs(l + 1, e)

        qs(0, len(pairs) - 1)

        return pairs