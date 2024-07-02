class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        exits = set()
        rows, cols = len(maze), len(maze[0])

        def isInbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and maze[r][c] == ".":
        #             exits.add((r, c))
        
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, step = queue.popleft()
                    
                for direction in directions:
                    newRow, newCol = r + direction[0], c + direction[1]

                    if isInbound(newRow, newCol) and maze[newRow][newCol] != "+":
                        if (newRow == 0 or newCol == 0 or newRow == rows - 1 or newCol == cols - 1) :
                            return step + 1

                        queue.append((newRow, newCol, step + 1))
                        maze[newRow][newCol] = "+"

        return -1



