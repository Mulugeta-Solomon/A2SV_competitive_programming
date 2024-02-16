class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        look_up = {}

        for idx, num in enumerate(nums):
            look_up[num] = idx

        for operation in operations:
            num, replacement = operation[0], operation[1]

            if num in look_up:
                idx = look_up[num]
                nums[idx] = replacement
                
                look_up[replacement] = look_up[num]
                  
        return nums
        