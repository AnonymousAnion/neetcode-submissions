class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        

        g.sort()
        s.sort()
        g_index = 0
        s_index = 0
        num_satisfied = 0

        while g_index < len(g) and s_index < len(s):

            while s_index < len(s) and g[g_index] > s[s_index]:

                s_index += 1

            if s_index < len(s) and g[g_index] <= s[s_index]:

                num_satisfied += 1
                s_index += 1
            
            g_index += 1

        return num_satisfied