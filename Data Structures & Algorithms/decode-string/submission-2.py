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

                num = ""

                while stack and stack[-1].isdigit():

                    num = stack.pop() + num

                stack.append(int(num) * current_string)

        return "".join(stack)