class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        combinations = []
        cur_combo = []
        cur_sum = 0
        
        def combo(i: int):

            nonlocal combinations
            nonlocal cur_combo
            nonlocal cur_sum

            if cur_sum == target:

                combinations.append(cur_combo.copy())
                return

            if cur_sum > target or i >= len(candidates):

                return

            cur_combo.append(candidates[i])
            cur_sum += candidates[i]

            combo(i + 1)

            cur_combo.pop()
            cur_sum -= candidates[i]

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:

                i += 1

            combo(i + 1)

        combo(0)

        return combinations