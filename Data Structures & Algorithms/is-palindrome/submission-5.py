import string

class Solution:

    def is_alphanumeric(self, char: str) -> bool:

        if len(char) > 1:

            raise ValueError("We only check whether a character is alphanumeric - not a string of greater than 1 length!")

        ASCII_VAL = ord(char)

        return (ord('A') <= ASCII_VAL <= ord('Z') or
         ord('a') <= ASCII_VAL <= ord('z') or
         ord('0') <= ASCII_VAL <= ord('9'))

    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not self.is_alphanumeric(s[l]):

                l += 1

            while r > l and not self.is_alphanumeric(s[r]):

                r -= 1

            if l < r:
                
                if s[l].lower() != s[r].lower():

                    return False

                l += 1
                r -= 1

        return True