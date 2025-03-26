class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val, prefix_sum = float('inf'), 0
        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)
        
        return 1 if min_val > 0 else abs(min_val) + 1