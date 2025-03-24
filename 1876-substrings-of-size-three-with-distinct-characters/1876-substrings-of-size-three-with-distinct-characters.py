class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l, r, result = 0, 2, 0

        while r < len(s):
            if len(set(s[l:r + 1])) == 3:
                result += 1    
            l += 1
            r += 1

        return result