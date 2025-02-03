class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        if not row or not col:
            return 

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        
        def check(x, y):
            return 1 <= x < row - 1 and 1 <= y < col - 1 and board[x][y] == 'O'
        
        for r in range(row):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][col - 1] == 'O':
                queue.append((r, col - 1))
        for c in range(col):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[row - 1][c] == 'O':
                queue.append((row - 1, c))

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if check(nr, nc):
                        queue.append((nr, nc))

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O': 
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'        