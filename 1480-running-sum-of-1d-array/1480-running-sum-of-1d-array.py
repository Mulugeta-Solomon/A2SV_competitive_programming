class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result, sum = [], 0

        for right in range(len(nums)):
            sum += nums[right]
            result.append(sum)
        
        return result