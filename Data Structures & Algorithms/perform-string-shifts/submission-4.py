class Solution:
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        
        left_shifts = 0

        for direction, amount in shifts:

            if direction == 1: # right

                amount = - amount

            left_shifts += amount

        left_shifts %= len(s)

        return s[left_shifts:] + s[:left_shifts]