class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minimum_length_word = min(len(word) for word in strs)
        prefix_chars = [strs[0][c] for c in range(minimum_length_word)]

        print(minimum_length_word)
        print(prefix_chars)

        for word in strs:

            count = 0

            for i in range(minimum_length_word):

                char = word[i]

                if char != prefix_chars[i]:

                    count = minimum_length_word - i
                    minimum_length_word = i
                    break

            for removals in range(min(len(prefix_chars), count)):

                prefix_chars.pop()

        return "".join(prefix_chars)