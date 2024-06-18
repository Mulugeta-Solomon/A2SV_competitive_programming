class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isInbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        
        def dfs(row, col):
            # base case
            if not isInbound(row, col) or grid[row][col] == 0: 
                return 1
                
            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1 # visited
            curr = 0
            for r, c in directions:
                newRow, newCol = row + r, col + c
                curr += dfs(newRow, newCol)
            
            return curr 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)
        
