class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookUp = {}

        for num in nums:
            lookUp[num]= lookUp.get(num, 0) + 1
        
        minHeap = []
        for num, freq in lookUp.items():
            heappush(minHeap, (-freq, num))
        
        result = []

        while minHeap:
            result.append(heappop(minHeap)[1])
            if len(result) == k:
                return result 
            