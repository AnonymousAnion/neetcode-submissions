class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        unique_window_chars = Counter()
        most_frequent: int = 0
        l: int = 0
        max_length: int = 0

        for r, char in enumerate(s):

            unique_window_chars[char] += 1
            most_frequent = max(most_frequent, unique_window_chars[char])
            window_length: int = r - l + 1

            while window_length - most_frequent > k:
            
                removed_char = s[l]
                unique_window_chars[removed_char] -= 1
                l += 1
                window_length = r - l + 1

            max_length = max(max_length, window_length)

        return max_length