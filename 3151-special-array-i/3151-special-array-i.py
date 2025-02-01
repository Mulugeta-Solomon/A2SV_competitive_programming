class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)):
            if nums[i-1] % 2 == 0 and nums[i] % 2 != 0:
                continue
            elif nums[i-1] % 2 != 0 and nums[i] % 2 == 0:
                continue
            else:
                return False
        
        return True
        