class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        colors += colors[:k-1]
        left, right, result = 0, 1, 0

        while right < len(colors):
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue
            
            right += 1
            if right - left < k:
                continue
            
            result += 1
            left += 1

        return result
        
        