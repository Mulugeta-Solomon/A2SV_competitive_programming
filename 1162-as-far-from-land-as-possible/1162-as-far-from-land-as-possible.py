class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),  len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()

        def isInbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # start from multiple source
                    queue.append((r, c, 1))
                    visited.add((r, c))

        result = -1

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, distance = queue.popleft()
 
                for direction in directions:
                    newRow, newCol = r + direction[0], c + direction[1]

                    if isInbound(newRow, newCol) and (newRow, newCol) not in visited:
                        result = max(result, distance)
                        queue.append((newRow, newCol, distance + 1))
                        visited.add((newRow, newCol))
        
        return result