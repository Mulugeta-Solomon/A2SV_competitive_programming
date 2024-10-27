class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        result = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    result += dp[i][j]
        
        return result