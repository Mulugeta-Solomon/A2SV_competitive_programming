class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        peakIdx, tower = None, float('-inf')

        for i, height in enumerate(heights):
            if tower <= height:
                tower = height 
                peakIdx = i
        
        result = heights[peakIdx]
        curr = heights[peakIdx]
        for i in range(peakIdx + 1, len(heights)):
            curr = min(curr, heights[i])
            result += curr
        
        curr = heights[peakIdx]

        for i in range(peakIdx - 1, -1, -1):
            curr = min(curr, heights[i])
            result += curr
        
        return result