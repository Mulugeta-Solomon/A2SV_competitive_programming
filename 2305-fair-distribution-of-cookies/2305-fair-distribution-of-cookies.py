class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        distribution = [0] * k
        self.ans = float('inf')
        n = len(cookies)

        if n == k:
            return max(cookies)
        
        def backtrack(start):
            if start == n:
                self.ans = min(self.ans, max(distribution))
                return 
            
            if max(distribution) >= self.ans:
                return 
            
            for i in range(k):
                distribution[i] += cookies[start]
                backtrack(start + 1)
                distribution[i] -= cookies[start]
        
        backtrack(0)
        return self.ans
            

        