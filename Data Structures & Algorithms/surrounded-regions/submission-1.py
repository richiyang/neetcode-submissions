class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(board), len(board[0])
        connectedO = set()

        def dfs(x, y):
            nonlocal connectedO
            
            if (x < 0 or x >= n or 
                y < 0 or y >= m or
                board[x][y] != 'O'):
                return

            board[x][y] = '#'
            
            for i, j in directions:
                dfs(x + i, y + j)
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        

                


            
