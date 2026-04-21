# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(s1, e1, s2, e2) -> None:

            combined = []

            l = s1
            r = s2

            while l <= e1 and r <= e2:

                if pairs[l].key <= pairs[r].key:

                    combined.append(pairs[l])
                    l += 1

                else:

                    combined.append(pairs[r])
                    r += 1

            while l <= e1:

                combined.append(pairs[l])
                l += 1

            while r <= e2:

                combined.append(pairs[r])
                r += 1

            for c in range(0, len(combined)):

                pairs[s1 + c] = combined[c]

        def divide(s, e) -> None:

            if e - s <= 0:

                return

            m = s + (e - s) // 2

            divide(s, m)
            divide(m + 1, e)

            merge(s, m, m + 1, e)

        divide(0, len(pairs) - 1)

        return pairs