class Solution:
    def fib(self, n: int, memo = {}) -> int:
        if n == 1 or n == 2:
            return 1
        if n < 1:
            return 0
        
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return memo[n]
        