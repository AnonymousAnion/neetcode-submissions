class Solution:
    def countSubstrings(self, s: str) -> int:

        def count_palindromes_from_indices(even: bool) -> int:

            total_palindromes: int = 0

            for i in range(len(s)):

                l: int = i
                r: int = i + 1 if even else i

                while l >= 0 and r < len(s):

                    if s[l] == s[r]:

                        total_palindromes += 1
                        l -= 1
                        r += 1

                    else:

                        break

            return total_palindromes

        odd_length_palindromes: int = count_palindromes_from_indices(False)
        even_length_palindromes: int = count_palindromes_from_indices(True)

        return odd_length_palindromes + even_length_palindromes