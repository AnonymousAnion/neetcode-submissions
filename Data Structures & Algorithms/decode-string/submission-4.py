class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:

            if char != "]":

                stack.append(char)

            else:

                current_string = ""

                while stack and stack[-1] != "[":

                    current_string = stack.pop() + current_string
                
                stack.pop() # Remove '['

                num = 0
                power = 1

                while stack and stack[-1].isdigit():

                    num = power * int(stack.pop()) + num
                    power *= 10

                stack.append(int(num) * current_string)

        return "".join(stack)