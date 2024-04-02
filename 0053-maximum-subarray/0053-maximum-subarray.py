class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum, prefix_sum, min_ = float('-inf'), 0, 0

        for right in range(len(nums)):
            min_ = min(min_, prefix_sum)
            prefix_sum += nums[right]
            max_sum = max(max_sum, prefix_sum - min_)
            print(prefix_sum, min_, max_sum)
        
        return max_sum