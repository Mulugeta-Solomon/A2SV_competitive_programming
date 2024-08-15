class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dp(idx1, idx2):
            if idx2 == len(t):
                return 1

            if idx1 == len(s):
                return 0
            
            if memo[idx1][idx2] != -1:
                return memo[idx1][idx2] 

            memo[idx1][idx2] = dp(idx1 + 1, idx2)

            if s[idx1] == t[idx2]:
                memo[idx1][idx2] += dp(idx1 + 1, idx2 + 1)
            
            return memo[idx1][idx2]
        
        
        memo = [[-1] * len(t) for _ in range(len(s))]
        dp(0, 0)

        return memo[0][0]
        