class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order = {char: i for i, char in enumerate(order)}

        def word_compare(word1: str, word2: str) -> bool:

            nonlocal order

            for i in range(min(len(word1), len(word2))):

                order1 = order[word1[i]]
                order2 = order[word2[i]]

                if order1 < order2:

                    return -1

                elif order2 < order1:

                    return 1

            if len(word1) < len(word2):

                return -1

            elif len(word2) < len(word1):

                return 1

            return 0 # Same word

        for i, word in enumerate(words):

            if i < len(words) - 1:

                next_word = words[i + 1]
                comparison = word_compare(word, next_word)

                if comparison > 0:

                    return False

        return True