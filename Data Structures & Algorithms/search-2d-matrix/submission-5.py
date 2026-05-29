class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        col = -1

        # find col
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                if m < len(matrix) -1 and matrix[m + 1][0] > target:
                    col = m
                    break
                l = m + 1
            else:
                return True

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[col][m] > target:
                r = m - 1
            elif matrix[col][m] < target:
                l = m + 1
            else:
                return True
        
        return False