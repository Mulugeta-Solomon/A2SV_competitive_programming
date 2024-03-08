class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right, left = 0, 1

        while left < len(nums):
            if nums[left] != 0:   
                while right < left:
                    if nums[right] == 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
                    right += 1 

            left += 1
           
        

