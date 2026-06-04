class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:

            if "C" == op:

                stack.pop()

            elif "D" == op:

                stack.append(stack[-1] * 2)

            elif "+" == op:

                stack.append(stack[-1] + stack[-2])

            else:

                stack.append(int(op))

        return sum(stack)