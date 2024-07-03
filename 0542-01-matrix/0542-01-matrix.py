class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(mat), len(mat[0])

        def isInbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1 # not checked yet
        
        result = [[0] * cols for _ in range(rows)]

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                for direction in directions:
                    newRow, newCol = r + direction[0], c + direction[1]

                    if isInbound(newRow, newCol) and mat[newRow][newCol] == -1:
                        queue.append((newRow, newCol))
                        mat[newRow][newCol] = 1 # mark visited and update the info
                        result[newRow][newCol] = result[r][c] + 1
        
        return result