class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heap = []

        for num in nums:
            heappush(heap, num)
        
        result = 1
        while heap:
            curr = heappop(heap)
            if curr <= 0:
                continue

            if curr > result:
                return result
            if curr == result:
                result += 1
            
    
        return result
            