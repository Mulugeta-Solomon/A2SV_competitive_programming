class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp, last_day, i = [0] * (days[-1] + 1), days[-1], 0
        
        for day in range(1, last_day + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(dp[day - 1] + costs[0], 
                              dp[max(0, day - 7)] + costs[1], 
                              dp[max(0, day - 7)] + costs[2])
        
        return dp[last_day]
