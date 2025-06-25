class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        directions, visited = [(0, 1), (0, -1), (1, 0), (-1, 0)], set()
        
        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col

        def dfs(r, c): # Recursive DFS 
            if (r, c) in visited:
                return 
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in visited and board[nr][nc] == 'O':
                    dfs(nr, nc)


        for r in range(row):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][col - 1] == 'O':
                dfs(r, col - 1)
        for c in range(col):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[row - 1][c] == 'O':
                dfs(row - 1, c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
        
