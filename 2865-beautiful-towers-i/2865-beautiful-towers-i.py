class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        max_sum = float('-inf')

        for peakIdx in range(len(heights)):
            result = heights[peakIdx]
            curr = heights[peakIdx]
            
            for i in range(peakIdx + 1, len(heights)):
                curr = min(curr, heights[i])
                result += curr
            
            curr = heights[peakIdx]

            for i in range(peakIdx - 1, -1, -1):
                curr = min(curr, heights[i])
                result += curr
            
            max_sum = max(max_sum, result)
        
        return max_sum