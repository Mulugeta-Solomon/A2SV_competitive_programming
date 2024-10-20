class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        rightMax = [0] * len(nums)
        rightMax[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])

        left, right, result = 0, 0, 0

        while right < len(nums):

            while right < len(nums) and nums[left] <= rightMax[right]:
                right += 1

            result = max(result, right - left - 1)
            left += 1
            right = left + result + 1

        return result 