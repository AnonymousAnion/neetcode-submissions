class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):

            return False

        s1_freqs = Counter(s1)
        window = s2[0:len(s1)]
        freqs = Counter(window)

        for i in range(0, len(s2) + 1 - len(s1)):

            print(i)

            if freqs == s1_freqs:

                return True

            freqs[s2[i]] -= 1

            print("Next num index: ", str(i + len(s1)))

            if i+len(s1) >= len(s2):

                break

            if s2[i+len(s1)] in freqs:

                freqs[s2[i+len(s1)]] += 1

            else:

                freqs[s2[i+len(s1)]] = 1

        return False
        