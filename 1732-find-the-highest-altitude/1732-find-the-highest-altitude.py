class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum, result = [0] * (len(gain) + 1), 0

        for i in range(len(gain)):
            prefix_sum[i + 1] = prefix_sum[i] + gain[i]
            result = max(result, prefix_sum[i + 1])
        
        return result
        