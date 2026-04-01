class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(t) < len(s):

            return False

        elif 0 == len(s):

            return True
        
        i = 0

        for j, char in enumerate(t):

            if char == s[i]:

                i += 1

                if i >= len(s):

                    return True

        return False