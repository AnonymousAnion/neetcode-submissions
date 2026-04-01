class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # N choose K problem
        
        curCombs = []
        combinations = []

        def helper(i: int) -> None:

            nonlocal curCombs
            nonlocal combinations

            if len(curCombs) == k:

                combinations.append(curCombs.copy())
                return

            if i > n:

                return

            for j in range(i, n + 1):

                curCombs.append(j)
                helper(j + 1)
                curCombs.pop()

        helper(1)

        return combinations