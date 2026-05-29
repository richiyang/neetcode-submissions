class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

        # t, b = 0, len(matrix) - 1

        # # find col
        # while t <= b:
        #     m = (t + b) // 2
        #     if matrix[m][0] > target:
        #         b = m - 1
        #     elif matrix[m][-1] < target:
        #         t = m + 1
        #     else:
        #         break

        # if not (t <= b):
        #     return False

        # col = (t + b) // 2
        # l, r = 0, len(matrix[0]) - 1

        # while l <= r:
        #     m = (l + r) // 2
        #     if matrix[col][m] > target:
        #         r = m - 1
        #     elif matrix[col][m] < target:
        #         l = m + 1
        #     else:
        #         return True
        
        # return False