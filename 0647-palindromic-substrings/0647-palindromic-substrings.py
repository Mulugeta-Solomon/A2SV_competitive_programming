class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def pali(left, right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
                
            return result 
        
        result = 0
        for i in range(len(s)):
            result += pali(i, i)
            result += pali(i, i+1)
        
        return result

