class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        left, right, result = 0, len(s) - 1, 0

        while left < right:
            if s[left] == '1' and s[right] == '0':
                result += (right - left)
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                continue
            
            if s[left] == '0':
                left += 1
            if s[right] == '1':
                right -= 1
        
        return result
            
            