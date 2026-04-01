class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        combined = []

        while i < len(word1) and i < len(word2):

            combined.append(word1[i])
            combined.append(word2[i])
            i += 1

        while i < len(word1):

            combined.append(word1[i])
            i += 1

        while i < len(word2):

            combined.append(word2[i])
            i += 1

        return "".join(combined)