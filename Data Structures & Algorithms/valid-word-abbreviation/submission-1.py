class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        word_index = 0

        number = []

        for char in abbr:

            #print("char: ", char)
            #print("word index: ", word_index)

            if str.isdigit(char):

                if not number and char == "0":

                    return False

                number.append(char)

            else:

                if number:

                    word_index += int("".join(number))
                    number = []

                #print("adj word index: ", word_index)

                if word_index >= len(word) or word[word_index] != char:

                    return False

                word_index += 1

            #print("word index: ", word_index)

        if number:

            word_index += int("".join(number))
            number = []

        if word_index == len(word):

            return True

        return False