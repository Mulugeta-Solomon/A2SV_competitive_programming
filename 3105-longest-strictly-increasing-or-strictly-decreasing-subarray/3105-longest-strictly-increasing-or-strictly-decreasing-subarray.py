class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec, result = 1, 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                result = max(result, inc)
                inc = 1
    
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dec += 1
            else:
                result = max(result, dec)
                dec = 1
        
        result = max(result, inc, dec)
        return result 
