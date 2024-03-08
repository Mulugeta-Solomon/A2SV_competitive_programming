class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        look_up = {}
        unsorted_nums = nums.copy()
       
        nums.sort()
        
        for idx, value in enumerate(nums):
            if value not in look_up:
                look_up[value] = idx
        
        answer = [look_up[num] for num in unsorted_nums]
        return answer
                
        