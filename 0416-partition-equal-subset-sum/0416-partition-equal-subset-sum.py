class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        def dp(total, index):
            if index >= len(nums) or total < 0:
                return False
            
            if (total, index) in memo:
                return memo[(total, index)]
            
            if total == 0:
                return True
            
            if index + 1 < len(nums) and (dp(total - nums[index], index + 1) or dp(total, index + 1)):
                return True
            
            memo[(total, index)] = False
            return memo[(total, index)]
        
        target = sum(nums) // 2
        memo = {}

        return dp(target, 0)
        