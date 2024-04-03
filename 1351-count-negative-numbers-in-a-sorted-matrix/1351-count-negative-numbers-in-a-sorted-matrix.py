class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        n, m, count = len(grid), len(grid[0]), 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] < 0:
                    count += 1
        
        return count