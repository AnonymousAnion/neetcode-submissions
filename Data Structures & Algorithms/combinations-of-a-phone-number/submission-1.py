class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combinations = []
        mappings = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def add_combos(letters: str) -> None:

            nonlocal combinations

            if not combinations:

                for letter in letters:

                    combinations.append([letter])

            else:
                newComb = []

                for combo in combinations:

                    for letter in letters:

                        newComb.append(combo.copy())
                        newComb[-1].append(letter)

                combinations = newComb

        for digit in digits:

            add_combos(mappings[digit])

        for i in range(len(combinations)):

            combinations[i] = "".join(combinations[i])

        return combinations