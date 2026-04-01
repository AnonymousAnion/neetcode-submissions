class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        
        for i in range(len(temperatures) - 1, -1, -1):

            temp = temperatures[i]

            #print("Temp: ", temp)

            count = 0

            while count < len(stack) and stack[-(count + 1)] <= temp:

                count += 1


            if count < len(stack):

                temperatures[i] = count + 1

            else:

                temperatures[i] = 0

            stack.append(temp)

            #print(stack)

        return temperatures
            