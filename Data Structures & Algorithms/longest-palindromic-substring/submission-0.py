class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""
        max_palindrome = 0

        for i in range(len(s)):

            # Check for palindrome growth from one letter
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                palindrome_length = r - l + 1

                if palindrome_length > max_palindrome:

                    max_palindrome = palindrome_length
                    longest_palindrome = s[l:r + 1]

                l -= 1
                r += 1

            # Check for Palindrome growth from two letters
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                palindrome_length = r - l + 1

                if palindrome_length > max_palindrome:

                    max_palindrome = palindrome_length
                    longest_palindrome = s[l:r + 1]

                l -= 1
                r += 1

        return longest_palindrome