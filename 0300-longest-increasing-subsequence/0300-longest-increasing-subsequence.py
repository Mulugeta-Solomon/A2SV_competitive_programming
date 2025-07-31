class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dp(prev, index):
            if index == len(nums):
                return 0
            
            if memo[prev][index] != -1:
                return memo[prev][index]
            
            result = dp(prev, index + 1)

            if prev == -1 or nums[prev] < nums[index]:
                result =  max(result, dp(index, index + 1) + 1)
            
            memo[prev][index] = result 

            return memo[prev][index]  

        memo = [[-1] * (len(nums) + 1) for _ in range(len(nums))]
        
        return dp(-1, 0)


        