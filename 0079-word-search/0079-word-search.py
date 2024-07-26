class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def isInbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        queue = deque()
        queue.append((board[0][0], (0, 0)))
        visited = set()
        visited.add((0, 0))
        check = []
        if board[0][0] in word:
            check.append(board[0][0])

        while queue:
            size = len(queue)
            for _ in range(size):
                node, (row, col) = queue.popleft()

                for r, c in directions:
                    newRow, newCol = row + r, col + c

                    if isInbound(newRow, newCol) and (newRow, newCol) not in visited:
                        queue.append((board[newRow][newCol],(newRow, newCol)))
                        visited.add((newRow, newCol))
                        if board[newRow][newCol] in word:
                            check.append(board[newRow][newCol])
        
        check = Counter(check)
        word = Counter(word)

        for letter, val in word.items():
            if check[letter] < val:
                return False
        return True
        



