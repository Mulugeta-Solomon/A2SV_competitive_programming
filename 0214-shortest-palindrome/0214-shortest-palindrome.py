class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False 
                left, right = left + 1, right - 1
            return True
        
        for right in reversed(range(len(s))):
            if isPalindrome(s, 0, right):
                return s[right + 1:][::-1] + s

        return ''      