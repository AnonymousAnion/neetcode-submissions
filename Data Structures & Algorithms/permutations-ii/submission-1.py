class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations = [[]]
        unique = set()

        for num in nums:

            next_nums = []

            for p in permutations:
                
                i = 0

                while i < len(p) + 1:

                    while i < len(p) and nums[i] == num:

                        i += 1

                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    hash = "".join(map(str, p_copy))

                    if hash not in unique:

                        next_nums.append(p_copy)
                        unique.add(hash)

                    i += 1

            permutations = next_nums
            unique = set()

        return permutations