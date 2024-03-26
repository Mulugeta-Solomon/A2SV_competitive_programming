class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]
            nums[right] = sum
        
        return nums