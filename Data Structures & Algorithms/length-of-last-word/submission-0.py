class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        
        for i in range(len(s) - 1, -1, -1):

            char = s[i]

            while char != " " and i - count >= 0:

                count += 1
                char = s[i - count]


            if count > 0:

                return count

        return ""