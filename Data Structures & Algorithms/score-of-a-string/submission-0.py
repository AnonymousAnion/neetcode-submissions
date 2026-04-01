class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0
        prev_char = ""

        for char in s:

            if prev_char != "":

                score += abs(ord(char) - ord(prev_char))
                
            prev_char = char

        return score