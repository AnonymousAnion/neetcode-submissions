class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            if "+" == token:

                stack.append(stack.pop() + stack.pop())

            elif "-" == token:

                stack.append(-stack.pop() + stack.pop())

            elif "*" == token:

                stack.append(stack.pop() * stack.pop())

            elif "/" == token:

                divisor = stack.pop()
                numerator = stack.pop()
                val = abs(numerator) // abs(divisor)

                if numerator / divisor < 0:

                    val *= -1

                stack.append(val)

            else:

                stack.append(int(token))
        
        return stack.pop()