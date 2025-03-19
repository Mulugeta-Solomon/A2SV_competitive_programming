class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr, result = 1, 0
        
        while n > 0:
            n -= curr
            if n >= 0:
                result += 1
            curr += 1

        return result