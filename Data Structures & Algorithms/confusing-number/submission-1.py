class Solution:
    def confusingNumber(self, n: int) -> bool:

        rotations: Dict[str, str] = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        num_string: str = str(n)

        # Form rotated string
        rotated_string = deque()

        for digit in num_string:

            if digit not in rotations:

                return False

            else:

                rotated_string.appendleft(rotations[digit])

        # Check that the rotated and original string are unequal
        for i in range(len(num_string)):

            if num_string[i] != rotated_string[i]:

                return True

        return False