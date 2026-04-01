class Solution:

    def validWordSquare(self, words: List[str]) -> bool:
        
        for j in range(0, len(words)):

            word = words[j]

            for i in range(0, len(word)):

                char = word[i]

                if i >= len(words) or j >= len(words[i]):

                    return False

                col_char = words[i][j]

                if char != col_char:

                    return False

        return True


