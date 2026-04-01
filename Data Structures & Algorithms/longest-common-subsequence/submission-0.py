class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ROWS = len(text1) + 1
        COLS = len(text2) + 1

        lcs = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(1, ROWS):

            for j in range(1, COLS):

                match = 0

                if text1[i - 1] == text2[j - 1]:

                    match = 1

                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], lcs[i - 1][j - 1] + match)

        return lcs[-1][-1]