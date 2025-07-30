class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] --> number of distinct ways to climp to the ith stair 
        # base case 
            # dp[1] = 1
            # dp[2] = 2
        # recurrence relation 
            # dp[i] = dp[i - 1] + dp[i - 2]
        # memo

        memo = {}

        def dp(i):
            if i < 3:
                return i
            
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)


            return memo[i]

        result = dp(n)
        print(memo)
        return result



    
        