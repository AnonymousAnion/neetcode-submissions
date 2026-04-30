class Solution:

    def is_palindrome(self, s: str, l: int, r: int) -> bool:

        while l < r:

            if s[l] != s[r]:

                return False
            
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:

        palindromic_substrings = []
        cur_subs = []
        
        def substring_builder(i: int) -> None:

            if i >= len(s):

                palindromic_substrings.append(cur_subs.copy())
                return

            for j in range(i, len(s)):

                if self.is_palindrome(s, i, j):

                    cur_subs.append(s[i:j + 1])
                    substring_builder(j + 1)
                    cur_subs.pop()

        substring_builder(0)

        return palindromic_substrings