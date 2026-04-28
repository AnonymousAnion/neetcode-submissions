class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        permutations = []
        current_permutation = []
        opens = 0
        closes = 0

        def insert_parentheses(length: int) -> None:

            nonlocal opens
            nonlocal closes
            nonlocal current_permutation
            nonlocal permutations

            if length == 2 * n:

                permutations.append("".join(current_permutation))
                return

            # Add open parenthesis, if possible.
            if opens < n:

                current_permutation.append("(")
                opens += 1
                insert_parentheses(length + 1)
                current_permutation.pop()
                opens -= 1

            # Add closed parenthesis, if possible.
            if closes < n and opens - closes > 0:

                current_permutation.append(")")
                closes += 1
                insert_parentheses(length + 1)
                current_permutation.pop()
                closes -= 1

        insert_parentheses(0)

        return permutations