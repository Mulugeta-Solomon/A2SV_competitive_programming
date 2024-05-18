class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count, window_sum = 0, 0

        while left < right:

            curr_sum = nums[left] + nums[right]
            
            if curr_sum > k:
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                count += 1
                right -= 1
                left += 1
        
        return count
