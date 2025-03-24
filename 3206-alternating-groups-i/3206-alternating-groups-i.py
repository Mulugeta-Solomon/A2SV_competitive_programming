class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        colors += colors[:2]
        l, r, result = 0, 2, 0

        while r < len(colors):
            if colors[r] == colors[l] and colors[r] != colors[r - 1]:
                result += 1
            r += 1
            l += 1
            
        return result
        