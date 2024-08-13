class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dp(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            left = dp(i, j - 1)
            up = dp(i - 1, j)
            
            memo[i][j] = left + up 

            return memo[i][j]

        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        return dp(m - 1, n - 1)