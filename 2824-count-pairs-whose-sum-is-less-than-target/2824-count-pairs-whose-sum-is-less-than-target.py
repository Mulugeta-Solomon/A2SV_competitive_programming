class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:

            if nums[right] + nums[left] >= target:
                right -= 1
            else:
                count += right - left 
                left += 1
        
        return count
