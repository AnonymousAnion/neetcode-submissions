class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        word_index = 0

        number = []

        for char in abbr:

            if str.isdigit(char):

                if not number and char == "0":

                    return False

                number.append(char)

            else:

                if number:

                    word_index += int("".join(number))
                    number = []

                if word_index >= len(word) or word[word_index] != char:

                    return False

                word_index += 1

        if number:

            word_index += int("".join(number))
            number = []

        if word_index == len(word):

            return True

        return False