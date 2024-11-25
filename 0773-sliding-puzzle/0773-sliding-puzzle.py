class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        graph = [[1, 3], [1, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        board = ''.join([str(board[row][col]) for row in range(len(board)) for col in range(len(board[0]))])
        result, target = 0, '123450'
        queue = deque([(board.index('0'), board, result)])
        visited = set([board])

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, board, result = queue.popleft()
                
                if board == target:
                    return result 
                
                board_arr = list(board)
                for neighbor in graph[curr]:
                    newBoard = board_arr[:]
                    newBoard[curr], newBoard[neighbor] = newBoard[neighbor], newBoard[curr]
                    newBoard = ''.join(newBoard)
                    if newBoard not in visited:
                        queue.append([neighbor, newBoard, result + 1])
                        visited.add(newBoard)

        return -1