class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        max_sum =  max(self.hourglass_sum(grid, row, col) 
                    for row in range(1, m-1) 
                    for col in range(1, n-1))
        # for row in range(1, m - 1):
        #     for col in range(1, n - 1):

        #         idxs = [(row, col), (row-1, col), (row+1, col), (row-1, col+1), 
        #                 (row-1, col-1), (row+1, col-1), (row+1, col+1)]
        #         curr_sum = 0
                
        #         for idx in idxs:
        #             r, c = idx
        #             curr_sum += grid[r][c]
                    
        #         max_sum = max(max_sum, curr_sum)
        
        return max_sum
    @staticmethod
    def hourglass_sum(grid: List[List[int]], i: int, j: int) -> int:
        return grid[i - 1][j - 1] + grid[i - 1][j] + \
                grid[i - 1][j + 1] + grid[i][j] + \
                grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]

        