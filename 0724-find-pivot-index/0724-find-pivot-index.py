class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_sum, total = 0, sum(nums)

        for i in range(len(nums)):
            if prefix_sum == total - (prefix_sum + nums[i]):
                return i
            prefix_sum += nums[i]
        
        return -1