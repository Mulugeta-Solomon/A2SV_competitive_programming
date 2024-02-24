class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        max_sum =  float('-inf')
        for row in range(1, m - 1):
            for col in range(1, n - 1):

                idxs = [(row, col), (row-1, col), (row+1, col), (row-1, col+1), 
                        (row-1, col-1), (row+1, col-1), (row+1, col+1)]
                curr_sum = 0
                
                for idx in idxs:
                    r, c = idx
                    curr_sum += grid[r][c]
                    
                max_sum = max(max_sum, curr_sum)
        
        return max_sum

        