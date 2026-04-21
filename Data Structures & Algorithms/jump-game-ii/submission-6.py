class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Fundamentally greedy BFS
        # for the nodes reachable by the current level of nodes
        # take the maximum distance they can reach to determine
        # the nodes at the next level. The BFS depth of each level
        # is the number of jumps required to reach that level

        min_jumps = 0
        l = 1
        r = 1 + nums[0]

        while l < len(nums):

            farthest_index = l

            for i in range(l, min(r, len(nums))):

                farthest_index = max(farthest_index, i + nums[i] + 1)

            l = r
            min_jumps += 1
            r = farthest_index

        return min_jumps