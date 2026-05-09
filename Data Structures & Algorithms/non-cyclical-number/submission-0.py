class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_sqaures(num: int) -> int:

            total = 0

            while num > 0:

                total += (num % 10) ** 2
                num //= 10

            return total
        
        visited = set()
        num = sum_of_sqaures(n)

        while num not in visited:

            if num == 1:

                return True

            visited.add(num)

            num = sum_of_sqaures(num)

        return False