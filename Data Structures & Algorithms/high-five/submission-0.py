class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        items.sort(key=lambda x: (x[0], -x[1]))

        solution = []
        n = len(items)
        i = 0
        while i < n:
            id = items[i][0]
            sum_val = 0
            for k in range(i, i + K):
                sum_val += items[k][1]
            while i < n and items[i][0] == id:
                i += 1
            solution.append([id, sum_val // K])

        return solution