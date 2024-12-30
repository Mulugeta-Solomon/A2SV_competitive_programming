class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD, dp = 10**9 + 7, [0] * (high + 1)
        dp[0] = 1

        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= MOD
        
        return sum(dp[low:high + 1]) % MOD