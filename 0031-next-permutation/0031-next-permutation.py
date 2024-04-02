class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        right = len(nums) - 2

        while right >= 0:
            if nums[right] < nums[right+1]:
                break
            right -= 1
        
        if right < 0:
            nums[:] = nums[::-1]
        else:
            for left in range(len(nums) - 1, right, -1):
                if nums[left] > nums[right]:
                    break
            
            nums[right], nums[left] = nums[left], nums[right]

            nums[right+1:] = nums[right+1:][::-1]