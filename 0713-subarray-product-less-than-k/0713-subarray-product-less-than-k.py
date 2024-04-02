class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left, max_subarr, window_prod = 0, 0, 1
                                                
        for right in range(len(nums)):      
            window_prod *= nums[right]

            while window_prod >= k and left <= right:
                window_prod /= nums[left]
                left += 1


            max_subarr += right - left + 1
        
        return max_subarr
        