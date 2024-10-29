class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        direction = [(-1, 1), (0, 1), (1, 1)]
        result = 0

        def isInbound(x, y):
            return 0 <= x < n and 0 <= y < m
        
        @cache
        def dfs(row, col, count):
            if not isInbound(row, col):
                return 
            
            result = count
            for r, c in direction:
                newRow, newCol = row + r, col + c
                if isInbound(newRow, newCol) and grid[newRow][newCol] > grid[row][col]:
                    curr = dfs(newRow, newCol, count + 1)
                    result = max(result, curr)
            
            return result
                
        for i in range(n):
            curr = dfs(i, 0, 0)
            result = max(result, curr)

        
        return result



