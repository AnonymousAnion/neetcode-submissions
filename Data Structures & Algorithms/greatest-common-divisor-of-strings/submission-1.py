class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        print(str1.split("AB"))

        largest_string = ""

        if len(str1) < len(str2):

            smallest = str1
            largest = str2

        else:

            smallest = str2
            largest = str1

        for i in range(1, len(smallest) + 1):

            substring = smallest[:i]
            all_matched = True

            for s in largest.split(substring):

                if s != "":

                    all_matched = False
                    break

            for s in smallest.split(substring):

                if s != "":

                    all_matched = False
                    break

            if all_matched:

                largest_string = substring

        return largest_string