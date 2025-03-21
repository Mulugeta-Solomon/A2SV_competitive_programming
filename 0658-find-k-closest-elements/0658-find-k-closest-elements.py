class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i, num in enumerate(arr):
            heappush(heap, (abs(num - x), i))

        result = []
        while k > 0:
            val, i = heappop(heap)
            result.append(arr[i])
            k -= 1
        
        result.sort()
    
        return result