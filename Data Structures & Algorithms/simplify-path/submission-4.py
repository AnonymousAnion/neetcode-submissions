class Solution:
    def simplifyPath(self, path: str) -> str:

        directories = path.split("/")
        stack = []

        for directory in directories:

            if directory == "..":

                if stack: stack.pop()

                continue

            if directory != "." and directory != "":

                stack.append(directory)


        return "/" + "/".join(stack)