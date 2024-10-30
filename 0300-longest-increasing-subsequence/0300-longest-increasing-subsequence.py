class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis, result = [1] * len(nums), 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
                    result = max(result, lis[i])
        
        return result