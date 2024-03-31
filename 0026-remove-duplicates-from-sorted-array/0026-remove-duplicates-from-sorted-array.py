class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, right = 0, 1
        
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            else:
                right += 1
        
        return left + 1
                