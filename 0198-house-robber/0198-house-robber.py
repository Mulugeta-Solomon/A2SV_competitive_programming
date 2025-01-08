class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(index):
            if index >= len(nums):
                return 0
            if memo[index] != -1:
                return memo[index]

            result = nums[index] + dp(index + 2)
            result = max(result, dp(index + 1))
            memo[index] = result

            return result
        
        return dp(0)