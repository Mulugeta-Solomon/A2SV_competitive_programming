class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        if n == 1 and intervals[0][0] >= intervals[0][1]:
            return [0]
        if n == 1 and intervals[0][0] < intervals[0][1]:
            return [-1]

        start_idx = [[intervals[i][0], i] for i in range(n)]
        ends = [intervals[i][1] for i in range(n)]
        
        start_idx.sort()
        result = [-1] * n 

        for i in range(n):
            result[i] = self.binarySearch(start_idx, ends[i])
        
        return result 
    
    def binarySearch(self, start: List[List[int]], target: int) -> int:

        if start[-1][0] < target:
            return -1

        left, right = 0, len(start)
        while left <= right:
            mid = left + (right - left) // 2
            if start[mid][0] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return start[left][1]

