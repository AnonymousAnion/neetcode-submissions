from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or t == "":

            return ""

        l: int = 0
        min_window = len(s) + 1
        query_freqs = Counter(t)
        freqs = Counter()
        frequencies_met = 0
        res = (0, 0)

        for r, char in enumerate(s):

            freqs.update(char)

            if char in query_freqs and freqs[char] == query_freqs[char]:

                frequencies_met += 1

            while frequencies_met == len(query_freqs):

                l_char: str = s[l]

                window_length = (r - l) + 1

                if window_length < min_window:

                    res = (l, r)
                    min_window = window_length

                freqs[l_char] -= 1

                if freqs[l_char] < query_freqs[l_char]:

                    frequencies_met -= 1

                l += 1
            
        if min_window > len(s):

            return ""

        return s[res[0]:res[1] + 1]