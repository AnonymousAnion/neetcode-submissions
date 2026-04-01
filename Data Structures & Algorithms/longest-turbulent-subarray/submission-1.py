class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # Simplify - we only care about the sign of deltas
        deltas = [0]

        for i in range(1, len(arr)):

            delta = arr[i] - arr[i-1]

            if delta > 0:

                delta = 1

            elif delta < 0:

                delta = -1

            deltas.append(delta)

        #print(deltas)

        prev_sign = 0
        current_sum = 1
        lts = 1 # Longest Turbulent Subarray (LTS)

        for i in range(1, len(deltas)):

            num = deltas[i]

            if 0 == num:

                current_sum = 1
                prev_sign = 0
                continue

            diff = abs(num - prev_sign)

            if 0 == prev_sign or diff > 1:

                current_sum += 1
                prev_sign = num

            else:

                current_sum = 2
                prev_sign = num


            lts = max(lts, current_sum)

            # print("{0}: {1}".format(num, diff))
            # print("Current Sum: ", current_sum)
            # print("LTS: ", lts)

        return lts