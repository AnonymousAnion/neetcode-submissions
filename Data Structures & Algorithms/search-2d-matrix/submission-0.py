class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Binary search for the row
        def row_binary_search(l = 0, r = len(matrix) - 1) -> List[int]:

            while l <= r:

                m = l + (r - l) // 2
                middle_row = matrix[m]

                if target > middle_row[-1]:

                    l = m + 1

                elif target < middle_row[0]:

                    r = m - 1

                else:

                    # Target should be within row, if present.
                    return middle_row

            return [] # Return empty array if target can't be within matrix's rows

        def col_binary_search(row: List[int]) -> bool:

            l = 0
            r = len(row) - 1

            while l <= r:

                m = l + (r - l) // 2

                if target > row[m]:

                    l = m + 1

                elif target < row[m]:

                    r = m - 1

                else:

                    return True

            return False

        candiate_row = row_binary_search()

        if not candiate_row:

            return False

        # Binary search for the column

        return col_binary_search(candiate_row)