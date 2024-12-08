class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = []

        for event in events:
            times.append([event[0], 1, event[2]]) # 1 start time 
            times.append([event[1] + 1, 0, event[2]]) # 0 end time 
        
        result, max_val = 0, 0
        times.sort()

        for time in times:
            if time[1]:
                result = max(result, time[2] + max_val)
            else:
                max_val = max(max_val, time[2])
        
        return result 