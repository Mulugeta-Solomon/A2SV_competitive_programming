class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dictionary = set(wordDict)
        n = len(s)

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                subs = s[j:i]
                if subs in dictionary:
                    dp[i] = min(dp[i], dp[j])
            dp[i] = min(dp[i], dp[i - 1] + 1)
        
        return True if dp[-1] == 0 else False