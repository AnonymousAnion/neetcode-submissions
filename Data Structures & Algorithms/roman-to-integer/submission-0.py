class Solution:
    def romanToInt(self, s: str) -> int:
        
        val_mappings ={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        i = len(s) - 1

        while i >= 0:

            char = s[i]
            current = val_mappings[char]
            total += current

            # print("i: ", i)
            # print("{0}: {1}".format(char, current))

            subtraction = 0
            prev_index = 1

            # print("Current: ", current)
            # print("Prev Value:")

            while i - prev_index >= 0 and val_mappings[s[i - prev_index]] < current:

                # print("Prev char {0}: {1}".format(s[i - prev_index], val_mappings[s[i - prev_index]]))
                subtraction += val_mappings[s[i - prev_index]]
                prev_index += 1

            # print("Prev Index {0}: {1}".format(s[i - prev_index], i - prev_index))
            i = i - (prev_index - 1)

            # print("Adjusted i: ", i)

            total -= subtraction
            i -= 1

            # print("Subtraction: ", subtraction)
            # print("Total: ", total)

        return total
