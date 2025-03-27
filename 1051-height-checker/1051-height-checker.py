class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, result = sorted(heights), 0
        
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                result += 1
        
        return result