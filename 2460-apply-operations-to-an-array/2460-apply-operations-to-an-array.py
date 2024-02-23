class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        zeros = [num for num in nums if num == 0]
        nums = [num for num in nums if num != 0]       
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i+1, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        
        return nums + zeros

        