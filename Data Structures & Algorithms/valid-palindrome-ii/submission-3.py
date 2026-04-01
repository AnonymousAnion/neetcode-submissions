class Solution:

    def validPalindrome(self, s: str, l = 0, r = 0, ALLOWED_ERRORS = 1) -> bool:

        # def is_palindrome(left, right) -> bool:

        #     while left < right:

        #         if s[left] != s[right]:

        #             return False

        #         left += 1
        #         right -= 1

        #     return True
        
        if 0 == r:

            r = len(s) - 1

        while l < r:

            if s[l] != s[r]:

                if ALLOWED_ERRORS - 1 >= 0:

                    return self.validPalindrome(s, l + 1, r, ALLOWED_ERRORS - 1) or self.validPalindrome(s, l, r - 1, ALLOWED_ERRORS - 1)

                else:

                    return False #is_palindrome(l + 1, r) or is_palindrome(l, r - 1)

            l += 1
            r -= 1

        return True