class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        right = len(needle)

        for left in range(len(haystack) - len(needle) + 1):
            if haystack[left:right] == needle:
                return left

            right += 1
        
        return -1  