class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1

        prev, curr = 0, 1

        for i in range(2, n + 1):
            curr, prev  = prev + curr, curr
            
        return curr