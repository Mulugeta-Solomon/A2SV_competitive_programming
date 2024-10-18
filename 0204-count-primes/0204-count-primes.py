class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        prime = [True] * n 
        i = 2

        while i * i <= n:
            if prime[i]:
                j = i * i
                while  j < n:
                    prime[j] = False
                    j += i
            i += 1
        
        return sum(prime[2:])
                





