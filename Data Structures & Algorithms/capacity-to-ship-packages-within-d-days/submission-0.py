class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        required_weight = max(weights)
        max_cap = sum(weights)
        weight_capacity = max_cap

        l = required_weight
        r = max_cap

        while l <= r:

            w = l + (r - l) // 2

            # Compute required days for this
            # weight capacity

            current_weight = 0
            total_days = 1

            for weight in weights:

                if current_weight + weight > w:

                    total_days += 1
                    current_weight = 0

                current_weight += weight

            if total_days > days:

                l = w + 1

            else:

                r = w - 1
                weight_capcity = min(weight_capacity, w)

        return weight_capcity