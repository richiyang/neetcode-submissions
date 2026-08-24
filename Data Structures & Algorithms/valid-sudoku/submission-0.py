class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        def squareFinder(row, col):
            r = row // 3
            c = col // 3
            return r + c * 3
        
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == '.':
                    continue
                
                square = squareFinder(row, col)
                
                if cur in rows[row] or cur in cols[col] or cur in squares[square]:
                    return False
                
                rows[row].add(cur)
                cols[col].add(cur)
                squares[square].add(cur)
        
        return True
                    