class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(index, total):
            if index >= len(nums) and total == target:
                return 1
            if index >= len(nums):
                return 0
            
            if (index, total) in memo:
                return memo[(index, total)]

            pos = dp(index + 1, total + nums[index])
            neg = dp(index + 1, total - nums[index])

            memo[(index, total)] = pos + neg 

            return pos + neg
        
        memo = {}

        return dp(0, 0)
