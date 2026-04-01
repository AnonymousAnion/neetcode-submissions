# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if 0 == len(pairs):

            return []
        
        states = [pairs.copy()]

        def swap(i1, i2) -> None:

            tmp = pairs[i1]
            pairs[i1] = pairs[i2]
            pairs[i2] = tmp

        for i in range(1, len(pairs)):

            j = i - 1

            # Check if need to sort and bring smaller value toward front
            while j >= 0 and pairs[j + 1].key < pairs[j].key:

                swap(j, j + 1)
                j -= 1

            states.append(pairs.copy())

        return states


        