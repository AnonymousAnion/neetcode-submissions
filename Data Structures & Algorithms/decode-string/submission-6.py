class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:

            if "]" == char:

                # Process string within brackets
                current_string = ""

                while stack and stack[-1] != "[":

                    current_string = stack.pop() + current_string

                stack.pop() # Remove open bracket "["

                # Process Number
                num = 0
                power = 1

                while stack and stack[-1].isdigit():

                    num += int(stack.pop()) * power
                    power *= 10
                    
                stack.append(num * current_string)

            else:

                stack.append(char)

        return "".join(stack)