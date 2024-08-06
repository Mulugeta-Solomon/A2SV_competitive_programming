class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        prefix_sum[1] = nums[1]

        for i in range(2, len(nums)):
            prefix_sum[i] = prefix_sum[i-2] + nums[i]
        
        print(prefix_sum)

        return max(prefix_sum[-1], prefix_sum[-2])
        