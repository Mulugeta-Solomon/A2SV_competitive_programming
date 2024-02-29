class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        look_up = {}
        unsorted_nums = nums.copy()
       
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        for idx, value in enumerate(nums):
            if value not in look_up:
                look_up[value] = idx
        
        answer = [look_up[num] for num in unsorted_nums]
        return answer
                
        