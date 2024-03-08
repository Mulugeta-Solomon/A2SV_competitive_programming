class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder, seeker = 0, 1

        while seeker < len(nums):
            if nums[seeker] != 0:
                
                while holder < seeker:
                    if nums[holder] == 0:
                        nums[holder], nums[seeker] = nums[seeker], nums[holder]
                        break
                    holder += 1
            
            seeker += 1
            
           
        

