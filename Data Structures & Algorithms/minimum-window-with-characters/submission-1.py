from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def contains_counts(subset: Counter, total: Counter) -> bool:

            for key in subset:

                if key not in total:

                    return False

                if subset[key] > total[key]:

                    return False

            return True

        if len(t) > len(s):

            return ""

        l = 0
        r = len(s) - 1
        min_window = len(s) + 1
        relevant_chars = set(t)
        relevant_window = deque()
        query_freqs = Counter(t)
        freqs = Counter()

        for i, char in enumerate(s):

            if char in relevant_chars:

                relevant_window.append((char, i ))
                freqs.update(char)

            while contains_counts(query_freqs, freqs) and len(relevant_window) >= len(t):

                front_char, front_i = relevant_window[0]
                end_char, end_i = relevant_window[-1]
                window_length = end_i - front_i + 1

                if window_length < min_window:

                    l = front_i
                    r = end_i
                    min_window = window_length

                removed_char, removed_index = relevant_window.popleft()
                freqs[removed_char] -= 1
            
        if min_window > len(s):

            return ""

        return s[l:r + 1]