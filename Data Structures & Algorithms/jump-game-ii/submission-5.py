class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Fundamentally greedy BFS
        # for the nodes reachable by the current level of nodes
        # take the maximum distance they can reach to determine
        # the nodes at the next level. The BFS depth of each level
        # is the number of jumps required to reach that level

        dist = nums[0]
        min_jumps = 0
        index = 1

        while index < len(nums):

            max_dist = 0

            for i in range(index, min(dist + index, len(nums))):

                if nums[i] > max_dist:

                    offset = dist + index - 1 - i
                    max_dist = max(max_dist, nums[i] - offset)

            index = index + dist
            min_jumps += 1
            dist = max_dist

        return min_jumps