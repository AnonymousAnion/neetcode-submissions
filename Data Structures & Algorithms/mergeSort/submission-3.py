# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if not pairs:

            return []

        def merge(s1, e1, s2, e2):

            nonlocal pairs
            l, r, c = s1, s2, 0

            combined = [0 for _ in range((e1 - s1 + 1) + (e2 - s2 + 1))]

            while l <= e1 and r <= e2:

                if pairs[l].key <= pairs[r].key:

                    combined[c] = pairs[l]
                    l += 1

                else:

                    combined[c] = pairs[r]
                    r += 1

                c += 1

            while l <= e1:

                combined[c] = pairs[l]
                l += 1
                c += 1

            while r <= e2:

                combined[c] = pairs[r]
                r += 1
                c += 1

            c = 0

            for i in range(s1, s1 + len(combined)):

                pairs[i] = combined[c]
                c += 1
        
        s = 0
        e = len(pairs) - 1

        def divide(s, e):

            if e - s == 0:

                return

            m = s + (e - s) // 2
            s1 = s
            e1 = m
            s2 = m + 1
            e2 = e

            divide(s1, e1)
            divide(s2, e2)
            merge(s1, e1, s2, e2)

        divide(s, e)

        return pairs