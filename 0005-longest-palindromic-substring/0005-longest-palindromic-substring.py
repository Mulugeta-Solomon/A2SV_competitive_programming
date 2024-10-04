class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxLen, maxStr = 1, s[0]
        for left in range(len(s) - 1):
            for right in range(left + 1, len(s)):
                if right - left + 1 > maxLen and s[left:right + 1] == s[left:right + 1][::-1]:
                    maxLen, maxStr = right - left + 1, s[left:right + 1]
        
        return maxStr