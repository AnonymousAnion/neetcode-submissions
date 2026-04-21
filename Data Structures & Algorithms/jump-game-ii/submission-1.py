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

            #print("Index: ", index)
            #print("dist: ", dist)

            max_dist = 0

            for i in range(index, min(dist + index, len(nums))):

                #print("num: ", nums[i])

                if nums[i] > max_dist:

                    max_dist = nums[i]


            index = index + dist
            min_jumps += 1
            dist = max_dist

            #print("min jumps: ", min_jumps)

        return min_jumps