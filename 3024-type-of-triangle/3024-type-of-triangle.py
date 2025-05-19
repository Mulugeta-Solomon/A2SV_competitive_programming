class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] >= nums[2] and nums[0] + nums[2] >= nums[1] and nums[1] + nums[2] >= nums[0]:
            size = len(set(nums))

            if size == 3:
                return 'scalene'
            if size == 2:
                return 'isosceles'

            return 'equilateral'
        return 'none' 
         
