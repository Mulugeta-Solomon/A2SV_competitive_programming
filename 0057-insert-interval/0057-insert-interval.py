class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        result, prev, i, flag = [], -1, 0, False, 
        start, end = newInterval
        print(start, end)
        while i < len(intervals):
            left = i
            if not flag and (start < intervals[i][0] and end < intervals[i][0]):
                result.append(newInterval)
                result.append(intervals[i])
                flag = True
                i += 1
                continue

            if not flag and (intervals[i][0] <= start <= intervals[i][1] or start < intervals[i][0]):
                right = i
                while right < len(intervals) and end >= intervals[right][1]:
                    right += 1
                
                if right >= len(intervals) or intervals[right][0] > end:
                    result.append([min(start,intervals[left][0]), max(end, intervals[right - 1][1])])
                    i = right
                else:
                    result.append([min(start,intervals[left][0]), max(end, intervals[right][1])])
                    i = right + 1
                flag = True
            else:
                result.append(intervals[i])
                i += 1

        if not flag:
            result.append(newInterval)
        
        return result