class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap, count, result = [], 0, sum(gifts)

        for gift in gifts:
            heappush(heap, -gift)
        
        while count < k:
            curr = -heappop(heap)
            push = floor(sqrt(curr))
            heappush(heap, -push)
            count += 1
            result -= (curr - push) 
 
        return result 
                   