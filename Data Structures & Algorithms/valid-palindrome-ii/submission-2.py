class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        errors = 0
        ALLOWED_ERRORS = 1

        while l < r:

            if s[l] != s[r]:

                errors += 1

                if s[l + 1] == s[r] and s[l] == s[r - 1]:

                    if s[l + 1] == s[r - 2]:

                        r -= 1

                    else:

                        l += 1

                elif s[l + 1] == s[r]:
                    
                    l += 1

                elif s[l] == s[r - 1]:

                    r -= 1
                
                else:

                    return False

            l += 1
            r -= 1

            if errors > ALLOWED_ERRORS:

                return False

        return True