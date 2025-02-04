class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result, curr = float('-inf'), nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                result = max(result, curr)
                curr = nums[i]
        
        result = max(result, curr)

        return result


