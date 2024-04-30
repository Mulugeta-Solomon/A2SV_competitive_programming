class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        if n < 1:
            return 0
        
        return self.fib(n-1) + self.fib(n-2)
        