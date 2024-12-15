class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def gains(passes, total):
            return ((passes + 1) / (total + 1)) - passes / total
        
        heap = []

        for passes, total in classes:
            heappush(heap, (-gains(passes, total), passes, total))
        
        for _ in range(extraStudents):
            gain, passes, total = heappop(heap)
            heappush(heap, (-gains(passes + 1, total + 1), passes + 1, total + 1))
        
        result = 0
        while heap:
            gain, passes, total = heappop(heap)
            result += (passes / total)
        
        return result / len(classes)
