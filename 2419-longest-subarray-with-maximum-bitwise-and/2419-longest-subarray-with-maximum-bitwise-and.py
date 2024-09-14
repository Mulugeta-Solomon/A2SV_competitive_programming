class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        result, count, max_val = 0, 0, max(nums)

        for num in nums:
            if num == max_val:
                count += 1
            else:
                count = 0
            
            result = max(result, count)
        
        return result
        