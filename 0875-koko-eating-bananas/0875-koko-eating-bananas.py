class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, sum(piles)
        k = -1
        while left <= right:
            mid = left + (right - left) // 2

            if self.canFinish(piles, mid, h): # can she finish within hour
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k 
    
    def canFinish(self, piles: List[int], capacity: int, time: int) -> bool:
        curr_cap, curr_time = 0, 0

        for i in range(len(piles)):

            curr_time -= (-piles[i] // capacity)
        
        return curr_time <= time

