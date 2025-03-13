class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, result = 0, 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                result += 1
                continue
                
            if g[i] > s[j]:
                j += 1
        
        return result 