from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):

            return ""

        l = 0
        r = len(s) - 1
        min_window = len(s) + 1
        relevant_chars = set(t)
        relevant_window = deque()
        query_freqs = Counter(t)
        freqs = Counter()
        frequencies_met = 0

        for i, char in enumerate(s):

            if char in relevant_chars:

                relevant_window.append((char, i ))
                freqs.update(char)

                if freqs[char] == query_freqs[char]:

                    frequencies_met += 1

            while frequencies_met == len(query_freqs):

                front_char, front_i = relevant_window[0]
                end_char, end_i = relevant_window[-1]
                window_length = end_i - front_i + 1

                if window_length < min_window:

                    l = front_i
                    r = end_i
                    min_window = window_length

                removed_char, removed_index = relevant_window.popleft()
                freqs[removed_char] -= 1

                if freqs[removed_char] < query_freqs[removed_char]:

                    frequencies_met -= 1
            
        if min_window > len(s):

            return ""

        return s[l:r + 1]