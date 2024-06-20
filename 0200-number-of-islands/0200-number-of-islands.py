class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isInbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        
        def dfs(row, col):
            # base case
            if not isInbound(row, col) or grid[row][col] != '1': 
                return 

            grid[row][col] = '0' # visited
            for r, c in directions:
                newRow, newCol = row + r, col + c
                dfs(newRow, newCol)
        
        island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    island += 1
                    dfs(row, col)
        
        return island