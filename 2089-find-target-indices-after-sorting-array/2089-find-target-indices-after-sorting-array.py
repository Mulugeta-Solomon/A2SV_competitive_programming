class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        less_than_equal = 0
        only_less = 0

        for num in nums:
            if num <= target:
                less_than_equal += 1
            if num < target:
                only_less += 1
        
        return list(range(only_less, less_than_equal))
        