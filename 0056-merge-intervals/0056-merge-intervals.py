class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = []
        intervals.sort(key = lambda x : x[0])
        prev = intervals[0]
        
        for interval in intervals:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                result.append(prev)
                prev = interval
            
        result.append(prev)

        return result