class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l = 0
        max_length = 0

        for r, char in enumerate(s):

            while char in charSet:

                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            max_length = max(max_length, (r - l) + 1)

        return max_length
        