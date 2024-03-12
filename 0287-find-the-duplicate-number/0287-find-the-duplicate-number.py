class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        left, right = 0, 1

        while right < len(nums):
            if nums[right] == nums[left]:
                return nums[left]
            
            left += 1
            right += 1
        