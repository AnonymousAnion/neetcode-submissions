class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        current = []
        freqs = Counter(nums)

        def dfs() -> None:

            if len(nums) == len(current):

                permutations.append(current.copy())
                #return

            for num in freqs.keys():

                if freqs[num] > 0:

                    current.append(num)
                    freqs[num] -= 1
                    dfs()
                    current.pop()
                    freqs[num] += 1

        dfs()

        return permutations