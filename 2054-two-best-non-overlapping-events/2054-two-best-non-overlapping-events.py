class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        result, n = 0, len(events)
        events.sort(key = lambda x:x[0]) # key=lambda x:x[0] 

        suffixMax = [0] * n
        suffixMax[-1] = events[-1][2]

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(events[i][2], suffixMax[i + 1])

        def binarysearch(left, right):
            idx, curr = -1, left - 1

            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[curr][1]:
                    idx = mid 
                    right = mid - 1
                else:
                    left = mid + 1
            
            return idx

        for i in range(n):
            left, right = i + 1, n - 1
            curr = binarysearch(left, right)

            if curr != -1:
                result = max(result, events[i][2] + suffixMax[curr])
            
            result =  max(result, events[i][2])
             
        return result 