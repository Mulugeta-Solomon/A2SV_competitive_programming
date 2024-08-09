class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(amount):
            if amount == 0:
                return 0
            
            if memo[amount] != -1:
                return memo[amount]

            min_coins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    result = dp(amount - coin)
                    if result >= 0:
                        min_coins = min(min_coins, result + 1)
                        # print(min_coins, coin, amount)
            memo[amount] = min_coins
            # print(memo)
            return memo[amount]
        
        memo = [-1] * (amount + 1)
        ans = dp(amount)
        if ans == float('inf'):
            return -1
        
        return ans