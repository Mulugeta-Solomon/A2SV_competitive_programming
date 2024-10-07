class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum, result = 0, 0

        for i in range(len(gain)):
            prefix_sum += gain[i]
            result = max(result, prefix_sum)
        
        return result
        