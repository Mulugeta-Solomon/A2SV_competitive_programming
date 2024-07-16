class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jump = 0
        for curr in nums:
            if jump < 0:
                return False 
                     
            jump = max(jump, curr)
            jump -= 1

        return True

