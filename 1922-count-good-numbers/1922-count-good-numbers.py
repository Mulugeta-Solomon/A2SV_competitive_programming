class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        num_even, num_odd = n//2 + n%2, n//2
        
        return (self.helper( 5, num_even, MOD) * self.helper(4, num_odd, MOD)) % MOD
    
    def helper(self, x: int, n: int, MOD: int) -> int:
        if n == 0:
            return 1
        
        if n%2 == 0:
            x = (x * x) % MOD
            n = n//2

        return (x * self.helper(x, n-1, MOD)) % MOD







        