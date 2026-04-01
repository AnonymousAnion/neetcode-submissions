class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #print("OG Digits: ", digits)
        
        increment = True

        for i in range(len(digits) - 1, -1, -1):

            digit = digits[i]

            if increment:

                digit += 1

            #print("Digit: ", digit)

            if digit < 10:

                digits[i] = digit
                increment = False

            else:

                digits[i] = 0
                increment = True

        if increment: # Need a new digit

            digits.insert(0, 1)

        return digits