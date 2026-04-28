class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        permutations = []
        current_permutation = []

        def insert_parentheses(opens: int, closes: int) -> None:

            if opens == n == closes:

                permutations.append("".join(current_permutation))
                return

            # Add open parenthesis, if possible.
            if opens < n:

                current_permutation.append("(")
                insert_parentheses(opens + 1, closes)
                current_permutation.pop()

            # Add closed parenthesis, if possible.
            if closes < opens:

                current_permutation.append(")")
                insert_parentheses(opens, closes + 1)
                current_permutation.pop()

        insert_parentheses(0, 0)

        return permutations