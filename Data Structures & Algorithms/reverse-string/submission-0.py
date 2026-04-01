class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        def swap(i1, i2):

            temp = s[i1]
            s[i1] = s[i2]
            s[i2] = temp

        while l < r:

            swap(l, r)

            l += 1
            r -= 1
        