import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        case_insensitive_letters = []

        for letter in s:

            if letter.isalnum():

                case_insensitive_letters.append(letter.lower())

        cleaned_string = "".join(case_insensitive_letters)

        #print("Cleaned String: ", cleaned_string)

        for i in range(0, len(cleaned_string)//2):

            if cleaned_string[i] != cleaned_string[len(cleaned_string) - 1 - i]:

                return False

        return True
        