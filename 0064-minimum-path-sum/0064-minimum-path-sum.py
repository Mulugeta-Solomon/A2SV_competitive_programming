class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def dp(row, col):
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            
            if memo[row][col] != -1:
                return memo[row][col]
            
            memo[row][col] = grid[row][col] + min(dp(row + 1, col), dp(row, col + 1))

            return memo[row][col]
            
        
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]

        return dp(0, 0)


        