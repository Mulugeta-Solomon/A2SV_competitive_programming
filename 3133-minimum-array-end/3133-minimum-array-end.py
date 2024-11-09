class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        result, curr, pos = x, n - 1, 1

        while curr:
            if not (x & pos):
                result = result | (curr & 1) * pos
                curr = curr >> 1
            pos = pos << 1
        
        return result
