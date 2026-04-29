class Solution:

    def is_palindrome(self, s: str) -> bool:

        i = 0

        while i < len(s) // 2:

            if s[i] != s[len(s) - 1 - i]:

                return False

            i += 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        
        cur_subs = [s[0]]
        cur_pals = [True]

        palindromic_substrings = []

        def substring_builder(i: int) -> None:

            nonlocal cur_subs
            nonlocal cur_pals

            if i == len(s):

                if cur_pals[-1]:

                    palindromic_substrings.append(cur_subs.copy())

                return

            char = s[i]

            # Case 1: Add character to last substring.
            # This should happen regardless of whether
            # the last substring is a palindrome because
            # it may become a palindrome later.
            cur_subs[-1] += char
            cur_pals[-1] = self.is_palindrome(cur_subs[-1])
            substring_builder(i + 1)
            cur_subs[-1] = cur_subs[-1][:len(cur_subs[-1]) - 1]
            cur_pals[-1] = self.is_palindrome(cur_subs[-1])

            # Case 2: Add character as a new substring.
            # This should only occur if the last substring
            # is a palindrome.
            if cur_pals[-1]:

                cur_subs.append(char)
                cur_pals.append(True)
                substring_builder(i + 1)
                cur_subs.pop()
                cur_pals.pop()

        substring_builder(1)

        return palindromic_substrings