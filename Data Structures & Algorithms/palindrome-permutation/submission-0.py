class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        freqs = Counter(s)
        odd_count = 0

        for freq in freqs:

            if freqs[freq] % 2 == 1:

                odd_count += 1

                if odd_count > 1:

                    return False

        return True