class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        indegree = [[0 for _ in range(col)] for _ in range(row)]
        
        def inbound(x, y):
            return 0 <= x < row and 0 <= y < col

        def bfs(queue):
            result = 0
            while queue:
                size = len(queue)
                result += 1
                for _ in range(size):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if inbound(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                            indegree[nr][nc] -= 1
                            if not indegree[nr][nc]:
                                queue.append((nr, nc))
                                                      
            return result 
   
        for r in range(row):
            for c in range(col):
                for (dr, dc) in directions:
                    nr, nc = r + dr, c + dc
                    if inbound(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                        indegree[nr][nc] += 1
        
        queue = deque()
        for r in range(row):
            for c in range(col):
                if not indegree[r][c]:
                    queue.append((r, c))


        result = bfs(queue)
        
        return result