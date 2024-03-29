class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum, prefix_sum = float('-inf'), 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum)

            if prefix_sum < 0:
                prefix_sum = 0
        
        return max_sum
