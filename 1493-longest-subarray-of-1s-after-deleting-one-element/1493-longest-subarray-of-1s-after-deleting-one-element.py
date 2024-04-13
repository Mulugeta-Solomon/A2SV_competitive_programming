class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        prefix_sum, suffix_sum = [0] * len(nums), [0] * len(nums)
        prefix_sum[0], suffix_sum[len(nums) - 1] = nums[0], nums[len(nums) - 1]

        for left in range(1, len(nums)):
            if nums[left] != 0:
                prefix_sum[left] = prefix_sum[left-1] + nums[left]
            else:
                prefix_sum[left] = 0
        
        for right in range(len(nums) - 2, -1, -1):
            if nums[right] != 0:
                suffix_sum[right] = suffix_sum[right+1] + nums[right]
            else:
                suffix_sum[right] = 0

        max_subarr = float('-inf')
        for i in range(len(nums)):
            left = prefix_sum[i-1] if i > 0 else 0
            right = suffix_sum[i+1] if i < len(nums) - 1 else 0
            max_subarr = max(max_subarr, left + right)
        
        return max_subarr
            
            

        


