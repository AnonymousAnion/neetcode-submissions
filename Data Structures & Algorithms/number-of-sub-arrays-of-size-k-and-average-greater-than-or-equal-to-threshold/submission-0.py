class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        sum_threshold = k * threshold

        current_sum = sum(arr[0:k])

        if current_sum >= sum_threshold:

            count += 1

        for i in range(k, len(arr)):

            num = arr[i]
            old_num = arr[i - k]
            current_sum = current_sum - old_num + num

            if current_sum >= sum_threshold:

                count += 1

        return count