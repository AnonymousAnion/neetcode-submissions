class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq1 = Counter(s)
        freq2 = Counter(t)

        print(len(freq1))
        print(len(freq2))

        if len(freq1) != len(freq2):

            return False

        for key in freq1:

            if key not in freq2:

                return False

            else:

                if freq1[key] != freq2[key]:

                    return False

        return True