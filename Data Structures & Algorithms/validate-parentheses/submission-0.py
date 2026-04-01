class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:

            if char == ")":

                if len(stack) > 0 and stack.pop() == "(":

                    continue

                return False

            elif char == "}":

                if len(stack) > 0 and stack.pop() == "{":

                    continue

                return False

            elif char == "]":

                if len(stack) > 0 and stack.pop() == "[":

                    continue

                return False

            else:

                stack.append(char)

        if len(stack) > 0:

            return False


        return True