class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = [[]]

        for num in nums:

            next_perms = []

            for p in permutations:

                for i in range(0, len(p) + 1):

                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    next_perms.append(p_copy)

            permutations = next_perms

        return permutations