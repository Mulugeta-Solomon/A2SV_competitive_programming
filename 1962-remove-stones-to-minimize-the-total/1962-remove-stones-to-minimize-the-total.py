class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = []

        for pile in piles:
            heappush(heap, -pile)
        
        while k > 0:
            pile = heappop(heap)
            heappush(heap, math.floor(pile / 2))
            k -= 1
        
        return -1 * sum(heap)
