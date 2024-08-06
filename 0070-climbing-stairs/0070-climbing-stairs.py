class Solution:
    def dp(self, n, memo):
        if n < 2:
            return 1
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)

        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        
        return self.dp(n, memo)
    
        