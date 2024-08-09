class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(n):         
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1

            if memo[n] != -1:
                return memo[n]

            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
        
            return memo[n]

        memo = [-1] * (n + 1)

        return dp(n)
        