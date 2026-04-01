import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        valid_chars = []

        for char in s:

            if char.isalnum():

                valid_chars.append(char.lower())

        s = "".join(valid_chars)

        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] == s[r]:

                l += 1
                r -= 1

            else:

                return False


        return True