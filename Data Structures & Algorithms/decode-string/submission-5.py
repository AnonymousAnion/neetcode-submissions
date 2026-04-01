class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:

            #print("Current char: ", char)

            if "]" == char:

                # Process string within brackets
                current_string = ""

                while stack and stack[-1] != "[":

                    current_string = stack.pop() + current_string

                stack.pop() # Remove open bracket "["

                #print("Pre-multiplication current string: ", current_string)

                # Process Number
                num = 0
                power = 1

                while stack and stack[-1].isdigit():

                    num += int(stack.pop()) * power
                    power *= 10

                #print("Number: ", num)
                    
                stack.append(num * current_string)

                #print("Post End Bracket Stack: ", stack)

            else:

                stack.append(char)
            
            #print("Stack on current iteration: ", stack)

        #print("Final Stack: ", stack)

        return "".join(stack)