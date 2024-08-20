class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = [0] * len(prices)
        buy = prices[0]
        
        for i in range(len(prices)):
            profit = max(0, prices[i] - buy)
            memo[i] = memo[i-1] + profit
            buy = prices[i]

        return memo[-1]
                
