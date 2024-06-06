class Solution:
    def minimumSteps(self, s: str) -> int:
        
        count, result = 0, 0
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1

            else:
                result += count 
        
        return result

        