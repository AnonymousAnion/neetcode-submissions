class Solution:
    def countSubstrings(self, s: str) -> int:

        T = [[False for _ in range(len(s))] for _ in range(len(s))]

        for offset in range(0, len(s)):

            for i in range(0, len(s) - offset):

                j = i + offset

                if 0 == j - i:

                    T[i][j] = True

                elif 1 == j - i:

                    T[i][j] = s[i] == s[j]

                else:

                    T[i][j] = (s[i] == s[j]) and T[i + 1][j - 1]

        total_palindromes = 0

        for i in range(len(s)):

            for j in range(i, len(s)):

                if T[i][j]:

                    total_palindromes += 1

        return total_palindromes