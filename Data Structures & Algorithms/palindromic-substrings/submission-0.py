class Solution:
    def countSubstrings(self, s: str) -> int:

        T = [[False for _ in range(len(s))] for _ in range(len(s))]

        #print(T)
        
        for offset in range(0, len(s)):

            for i in range(0, len(s) - offset):

                j = i + offset

                #print("({0},{1})".format(i, j))

                if 0 == j - i:

                    T[i][j] = True

                elif 1 == j - i:

                    T[i][j] = s[i] == s[j]

                else:

                    T[i][j] = (s[i] == s[j]) and T[i + 1][j - 1]

        #     print()

        # print("Final Table: ")
        # print(T)

        total_palindromes = 0

        for i in range(len(s)):

            for j in range(i, len(s)):

                total_palindromes += int(T[i][j])

        return total_palindromes