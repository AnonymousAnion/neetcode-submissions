class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_triangle = []

        for row in range(numRows):

            pascal_triangle.append([])

            for col in range(row + 1):

                if col == 0 or col == row:

                    pascal_triangle[-1].append(1)

                else:
                    
                    pascal_sum = pascal_triangle[-2][col - 1] + pascal_triangle[-2][col]
                    pascal_triangle[-1].append(pascal_sum)

        return pascal_triangle