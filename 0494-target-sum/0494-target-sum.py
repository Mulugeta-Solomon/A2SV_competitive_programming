class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(index, total):
            if index < 0 and total == target:
                return 1
            if index < 0:
                return 0
            
            if (index, total) in memo:
                return memo[(index, total)]

            pos = dp(index - 1, total + nums[index])
            neg = dp(index - 1, total - nums[index])

            memo[(index, total)] = pos + neg 
            # print(memo)
            return pos + neg
        
        memo = {}

        return dp(len(nums) - 1, 0)
