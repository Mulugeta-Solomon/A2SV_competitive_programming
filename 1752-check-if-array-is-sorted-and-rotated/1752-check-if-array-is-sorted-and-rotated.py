class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if nums[i] > nums[0]:
                    pivot += 1
                continue
    
            if nums[i] > nums[i + 1]:
                pivot += 1
        
        return pivot <= 1