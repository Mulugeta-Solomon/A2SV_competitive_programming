class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        suffix_sum, prefix_sum, result = [0] * len(nums), [0] * len(nums), 0
        suffix_sum[-1], prefix_sum[0] = nums[-1], nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        
        for i in range(len(nums) - 1):
            if prefix_sum[i] >= suffix_sum[i + 1]:
                result += 1
        
        return result