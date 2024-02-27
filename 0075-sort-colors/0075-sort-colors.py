class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right, mid, left = 0, 0, len(nums)-1
        while mid <= left:
            if nums[mid] == 0:
                nums[right], nums[mid] = nums[mid], nums[right]
                right += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[left] = nums[left], nums[mid]
                left -= 1
            
        