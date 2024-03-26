class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left, min_subarr, window_sum = 0, float('inf'), 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_subarr = min(min_subarr, right - left + 1)
                window_sum -= nums[left]
                left += 1
        

        
        return 0 if min_subarr == float('inf') else min_subarr
            

