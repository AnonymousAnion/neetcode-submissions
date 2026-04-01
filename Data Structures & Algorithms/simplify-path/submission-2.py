class Solution:
    def simplifyPath(self, path: str) -> str:

        directories = []
        last_slash = 0
        
        for i, char in enumerate(path + "/"):

            if char == "/":

                current = path[last_slash:i]

                if current == "..":

                    if directories: directories.pop()

                elif current != "" and current != ".":

                    directories.append(current)

                last_slash = i + 1

        return "/" + "/".join(directories)




            