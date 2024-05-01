class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = True if n < 0 else False 
        n = abs(n)
        
        if n <= 0:
            return 1
        
        if n%2 == 0:
            x = x * x
            n = n // 2
         
        return x * self.myPow(x, n-1) if not flag else (1/(x * self.myPow(x, n-1)))
        