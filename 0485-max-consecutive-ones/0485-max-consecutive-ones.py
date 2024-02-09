class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_consecutive_ones = float('-inf')
        counter = 0
        for num in nums:
            if num != 1:
                counter = 0
            else:
                counter += 1
            max_consecutive_ones = max(max_consecutive_ones, counter)
        
        return max_consecutive_ones
        