class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        s = 1
        e = num

        while s <= e:

            m = s + (e - s) // 2
            square = m * m

            if square > num:

                e = m - 1

            elif square < num:

                s = m + 1

            else:

                return True

        return False


        