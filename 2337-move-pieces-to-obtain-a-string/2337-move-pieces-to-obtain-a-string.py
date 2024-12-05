class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startIdx, targetIdx, n = 0, 0, len(start)

        while startIdx < n or targetIdx < n:
            while startIdx < n and start[startIdx] == '_':
                startIdx += 1
            
            while targetIdx < n and target[targetIdx] == '_':
                targetIdx += 1

            if startIdx == n or targetIdx == n:
                return (startIdx == n and targetIdx == n)
            
            if start[startIdx] != target[targetIdx] or (start[startIdx] == 'L' and startIdx < targetIdx) \
            or (start[startIdx] == 'R' and startIdx > targetIdx):
                return False
            
            startIdx += 1
            targetIdx += 1
        
        return True

