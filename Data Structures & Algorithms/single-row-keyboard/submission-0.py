class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        keyboard_mappings = {key: index for index, key in enumerate(keyboard)}

        i = 0
        total = 0

        for char in word:

            j = keyboard_mappings[char]
            total += abs(j - i)
            i = j

        return total