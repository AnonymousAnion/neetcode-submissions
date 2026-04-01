import string

class Solution:

    def is_alphanumeric(self, char: str) -> bool:

        if len(char) > 1:

            raise ValueError("We only check whether a character is alphanumeric - not a string of greater than 1 length!")

        ASCII_VAL = ord(char)

        if 48 <= ASCII_VAL <= 57 or 65 <= ASCII_VAL <= 90 or 97 <= ASCII_VAL <= 122:
            
            return True

        return False

    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:

            while l < len(s) and not self.is_alphanumeric(s[l]):

                l += 1

            while r >= 0 and not self.is_alphanumeric(s[r]):

                r -= 1

            if 0 > l or l >= len(s) or 0 > r or r >= len(s):

                break

            if s[l].lower() == s[r].lower():

                l += 1
                r -= 1

            else:

                return False

        return True