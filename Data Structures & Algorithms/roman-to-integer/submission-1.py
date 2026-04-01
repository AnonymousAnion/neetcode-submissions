class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        prev_char = "I"

        for i, char in enumerate(reversed(s)):

            if roman[char] >= roman[prev_char]:

                total += roman[char]

            else:

                total -= roman[char]

            prev_char = char

        return total
