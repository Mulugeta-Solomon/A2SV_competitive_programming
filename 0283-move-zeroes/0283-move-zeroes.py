class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder, seeker = 0, 1

        while seeker < len(nums):
            if nums[seeker] != 0 and nums[holder] == 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]

            if nums[holder] != 0:
                holder += 1
                
            seeker += 1
            