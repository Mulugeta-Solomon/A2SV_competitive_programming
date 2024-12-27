class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left, result = values[0], 0

        for i in range(1, len(values)):
            curr_right = values[i] - i 
            result = max(result, curr_right + max_left) # curr_right(j) + max_left(i) = values[i] + values[j] + i - j
            curr_left = values[i] + i
            max_left = max(max_left, curr_left)
        
        return result