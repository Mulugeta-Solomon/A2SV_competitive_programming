class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                prices[stack.pop()] -= price

            stack.append(i)
        
        return prices 
