class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        maxHeap = []

        for left, right in intervals:
            if maxHeap and left > maxHeap[0]:
                heappop(maxHeap)
            
            heappush(maxHeap, right)

        return len(maxHeap)
        