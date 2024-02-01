class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()                # speed = O(nlogn)  space = O(1)
        max_sum = 0
        is_even = True if len(piles)%2 == 0 else False
        for idx in range(len(piles)-1, len(piles)//3 - 1, -1):
            if is_even:
                if idx % 2 == 0:
                    max_sum += piles[idx]
            else:
                if idx % 2 != 0:
                    max_sum += piles[idx]
        return max_sum  
        