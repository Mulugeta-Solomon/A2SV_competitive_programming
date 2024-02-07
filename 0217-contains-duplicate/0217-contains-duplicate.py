class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        look_up = {}

        for num in nums:
            if num in look_up:
                look_up[num] += 1
            else:
                look_up[num] = 1
        
        #print(look_up)

        for key, value in look_up.items():
            if value > 1:
                return True
        
        return False
        