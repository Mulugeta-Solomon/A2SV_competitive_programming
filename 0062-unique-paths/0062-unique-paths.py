class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j - 1]

        return memo[-1][-1] 