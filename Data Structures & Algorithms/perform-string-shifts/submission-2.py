class Solution:
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        
        aggregate_shift = 0

        for shift in shifts:

            magnitude = shift[1]

            if shift[0] == 0:

                aggregate_shift -= magnitude

            else:

                aggregate_shift += magnitude

        if aggregate_shift < 0:

            aggregate_shift = -(abs(aggregate_shift) % len(s))

        else:

            aggregate_shift = aggregate_shift % len(s)

        shifted = ["" for _ in range(len(s))]

        for i, char in enumerate(s):

            new_index = i + aggregate_shift

            if new_index >= 0:

                new_index %= len(s)
                shifted[new_index] = char

            else:

                new_index = len(s) + new_index
                shifted[new_index] = char

        return "".join(shifted)