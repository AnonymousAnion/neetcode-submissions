class Solution:
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        
        aggregate_shift = 0

        for shift in shifts:

            #print("Shift: ", shift)

            magnitude = shift[1]

            if shift[0] == 0:

                aggregate_shift -= magnitude

            else:

                aggregate_shift += magnitude

            #print("Aggregate Shift: ", aggregate_shift)
            if aggregate_shift < 0:

                aggregate_shift = -(abs(aggregate_shift) % len(s))

            else:

                aggregate_shift = aggregate_shift % len(s)
            #print("Normalized Aggregate Shift: ", aggregate_shift)

        shifted = ["" for _ in range(len(s))]

        #print(shifted)

        for i, char in enumerate(s):

            #print("i: ", i)
            #print("char: ", char)
            #print("aggregate shift: ", aggregate_shift)

            new_index = i + aggregate_shift

            if new_index >= 0:

                new_index %= len(s)
                #print("New index: ", new_index)
                shifted[new_index] = char

            else:

                #print("neg")
                new_index = len(s) + new_index
                #print("New index: ", new_index)
                shifted[new_index] = char

        #print(shifted)

        return "".join(shifted)